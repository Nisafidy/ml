# Module 4 - Construction et prédiction d'un score socio-économique

## 1. Présentation générale

Ce projet met en place une chaîne de traitement de données socio-économiques à partir de l'enquête EPM 2021-2022 à Madagascar. L'objectif du module est de préparer des données au niveau du ménage et de l'individu, de construire des indicateurs liés au revenu et aux conditions de vie, puis de produire un score individuel (`score_individuel_epm`) pouvant être estimé par un modèle de machine learning.

Le travail est organisé en quatre étapes principales :

1. explorer et comprendre les données brutes ;
2. créer des variables utiles à partir des informations sur l'emploi, le logement et les impôts ;
3. construire une base de modélisation et une cible socio-économique ;
4. entraîner, évaluer et sauvegarder un modèle de prédiction.

Les notebooks constituent actuellement le coeur du projet. Les fichiers `src/preprocess.py`, `src/train.py`, `src/predict.py` et `src/api.py` sont prévus pour transformer le travail exploratoire en application réutilisable, mais ils sont encore vides dans l'état actuel du dépôt.

## 2. Organisation des données

### Données brutes

Le dossier `data/raw/` contient les sources utilisées :

- `EMPL_complet.csv` : informations individuelles sur l'emploi et les travailleurs ;
- `metier.csv` : référentiel des métiers et salaires moyens en ariary ;
- `variable.csv` : dictionnaire des variables et de leurs descriptions ;
- `00_MDG_EPM2122_HHINFO.dta` : informations générales sur les ménages ;
- `11_MDG_EPM2122_LOGE.dta` : caractéristiques du logement et accès à l'énergie ;
- `21_MDG_EPM2122_IMPO.dta` : informations relatives aux impôts et taxes.

Les fichiers `.dta` sont des fichiers Stata. Ils sont lus avec `pandas.read_stata`, tandis que les fichiers CSV sont lus avec `pandas.read_csv`.

### Données produites

Deux fichiers sont enregistrés dans `data/processed/` :

- `df_eda_revenus.csv` : table préparée au niveau du ménage pour l'analyse du logement, de l'énergie et des revenus ;
- `df_features_score.csv` : table finale destinée à la modélisation du score individuel.

Le dossier `reports/figures/` contient également des visualisations produites pendant l'analyse exploratoire, notamment la répartition des ménages par tranche de revenu.

## 3. Analyse exploratoire des données

### 3.1 Chargement et contrôle initial

Le notebook `01_EDA.ipynb` commence par charger les bibliothèques `pandas`, `numpy`, `matplotlib`, `seaborn` et `os`. Le fichier `EMPL_complet.csv` est ensuite importé afin de :

- connaître le nombre de lignes et de colonnes ;
- examiner les premières observations ;
- vérifier les types de données ;
- mesurer le nombre et le pourcentage de valeurs manquantes ;
- calculer des statistiques descriptives pour les variables numériques.

Cette étape permet de repérer les colonnes utiles et d'identifier les problèmes de qualité de données avant les transformations.

### 3.2 Utilisation du dictionnaire des variables

Le fichier `variable.csv` est utilisé comme dictionnaire de correspondance entre les noms codés des variables et leurs descriptions. Les espaces inutiles sont supprimés, puis un dictionnaire Python est créé avec la forme :

```python
{nom_de_variable: description}
```

Une fonction d'aide permet ensuite de retrouver le libellé d'une variable comme `q4a_17`, `q4a_19` ou `q4a_46a`. Cette étape est importante, car les enquêtes contiennent de nombreuses variables dont le nom seul ne suffit pas à comprendre le contenu.

### 3.3 Analyse de la population active

La population active est approchée à partir de la variable `q4a_17`, qui indique le nombre d'emplois ou d'activités professionnelles. Les individus dont cette variable est renseignée sont conservés dans une table `actifs`.

Les variables de profession et de revenu sont ensuite recherchées de manière ciblée :

- `q4a_19` est inspectée pour étudier les codes de profession ;
- les colonnes contenant `sal`, `rev`, `inc`, `ing` ou `dép` sont recherchées pour localiser les montants ;
- le dictionnaire des variables est consulté pour confirmer le sens des colonnes candidates.

Cette recherche exploratoire a permis de préparer l'estimation d'un salaire lorsque le revenu direct n'est pas suffisamment disponible.

### 3.4 Estimation des salaires par métier

Le fichier `metier.csv` est transformé en dictionnaire associant un métier à un salaire moyen en ariary. La fonction `estimer_salaire_metier` applique plusieurs règles, dans l'ordre suivant :

1. rechercher une correspondance exacte ou partielle avec le référentiel des métiers ;
2. appliquer une règle sectorielle pour des mots-clés liés à l'agriculture, au commerce, au transport, au BTP, à l'éducation ou à l'administration ;
3. utiliser une valeur nationale par défaut de `196359` ariary si aucune correspondance n'est trouvée ou si la profession est absente.

Le résultat est stocké dans `salaire_impute_v2`. Il s'agit d'une imputation et non d'un revenu observé : cette distinction doit être conservée lors de l'interprétation des résultats.

### 3.5 Agrégation au niveau du ménage

Les salaires imputés des actifs sont regroupés par `idHH`. Deux variables sont calculées :

- `revenu_total_menage` : somme des salaires imputés des actifs du ménage ;
- `nb_actifs_menage` : nombre d'actifs recensés dans le ménage.

Ces variables sont fusionnées avec la base principale. Les ménages sans actif identifié reçoivent la valeur zéro pour ces deux indicateurs.

Le revenu total est ensuite découpé en cinq tranches fixes :

| Catégorie | Intervalle de revenu estimé |
| --- | --- |
| Q1 - Très faible | moins de 200 000 ariary |
| Q2 - Faible | 200 000 à 350 000 ariary |
| Q3 - Moyen | 350 000 à 500 000 ariary |
| Q4 - Élevé | 500 000 à 1 000 000 ariary |
| Q5 - Très élevé | plus de 1 000 000 ariary |

Les ménages sans revenu actif sont classés dans `Non renseigné / Sans actif`. Une visualisation en barres présente ensuite les effectifs et les pourcentages de chaque catégorie.

## 4. Analyse du logement, de l'énergie et des impôts

### 4.1 Création des cibles liées à l'éclairage

Les données du fichier `11_MDG_EPM2122_LOGE.dta` sont utilisées pour créer des indicateurs à partir de `q11_38`, la source principale d'éclairage :

- `target_reseau` vaut 1 pour le réseau ou le générateur, et 0 sinon ;
- `target_eclairage_propre` vaut 1 pour le réseau, le générateur ou le solaire, et 0 pour les sources traditionnelles ;
- `type_eclairage` regroupe les ménages en trois catégories : `Réseau`, `Solaire` et `Traditionnel`.

Les distributions de ces variables sont examinées globalement et par milieu de résidence. Les taux sont calculés avec `hhweight` afin de tenir compte du poids statistique des ménages.

### 4.2 Harmonisation des identifiants

Les fichiers provenant de différentes sources ne stockent pas toujours `idHH` avec le même type ou le même format. Une fonction de normalisation :

- convertit l'identifiant en chaîne de caractères ;
- supprime les espaces ;
- retire un éventuel suffixe `.0` issu d'un import numérique ;
- complète l'identifiant avec des zéros jusqu'à une longueur de 12 caractères.

La clé obtenue, `idHH_clean`, est utilisée pour réaliser les fusions entre les tables de logement, de ménage et d'emploi. La fusion HHINFO/LOGE est contrôlée avec `validate='1:1'` afin de vérifier qu'elle respecte la relation attendue entre les ménages.

### 4.3 Variables de logement

Plusieurs caractéristiques sont inspectées ou conservées pour la future modélisation :

- région, district et commune ;
- milieu urbain ou rural ;
- type de bâtiment ;
- nombre de pièces ;
- matériau des murs, du toit et du sol ;
- accès à l'électricité et type d'éclairage.

Le nombre de pièces (`q11_02a`) est imputé par la médiane lorsqu'il est manquant. Les valeurs supérieures à 15 sont plafonnées afin de limiter l'effet des valeurs extrêmes. Les variables catégorielles sont converties en chaînes puis en catégories Pandas.

### 4.4 Intégration des impôts

Les montants `q21_021`, `q21_022`, `q21_023` et `q21_024` sont convertis en valeurs numériques. Les valeurs manquantes sont remplacées par zéro, puis additionnées dans `impot_total_menage`.

Un indicateur binaire `paie_impot_flag` est créé :

- 1 si le montant total est supérieur à zéro ;
- 0 sinon.

Ces deux variables sont fusionnées avec la table principale sur `idHH`. Les ménages sans correspondance reçoivent également zéro après la fusion.

## 5. Construction de la cible socio-économique

Le notebook `02_feature_engineering.ipynb` prépare une cible appelée `score_individuel_epm`, comprise théoriquement entre 0 et 100. Le score combine cinq piliers :

| Pilier | Poids |
| --- | ---: |
| Revenu | 35 % |
| Formalité de l'emploi | 20 % |
| Qualification | 15 % |
| Éducation | 15 % |
| Équipement et accès aux services | 15 % |

Chaque pilier est normalisé entre 0 et 1 avec une transformation min-max :

```text
score_normalise = (valeur - minimum) / (maximum - minimum)
```

Pour le revenu, une transformation logarithmique `log1p` est appliquée avant la normalisation afin de réduire l'effet des salaires très élevés. Les valeurs négatives et les valeurs manquantes sont ramenées à zéro avant cette transformation.

Le score final est calculé par :

```text
score_individuel_epm = 100 * (
    0.35 * pilier_revenu
  + 0.20 * pilier_formalite
  + 0.15 * pilier_qualification
  + 0.15 * pilier_education
  + 0.15 * pilier_equipement
)
```

Les variables disponibles sont détectées par recherche de noms : salaire ou `q4a_68a` pour le revenu, `q4a_08` ou `q4a_12` pour la formalité, `q4a_00` ou `q1_0x` pour la qualification, et `q11_` ou `edu` pour l'éducation.

Lorsque les variables attendues ne sont pas trouvées, des valeurs par défaut sont utilisées. Dans la version actuelle, cette solution permet de poursuivre le pipeline, mais elle réduit la portée interprétable des piliers concernés. Les valeurs par défaut devront être remplacées par des règles métier validées avant une utilisation définitive du score.

## 6. Préparation de la base de machine learning

Après la fusion entre les données d'emploi et les informations du ménage, les variables de production retenues sont :

- `idHH_clean` : identifiant technique du ménage ;
- `salaire_mensuel` : salaire traité ou imputé ;
- `hhmilieu2` : milieu de résidence ;
- `hhreg` : région ;
- `q4a_02` : code ou catégorie de métier ;
- `score_individuel_epm` : cible à prédire.

La variable `salaire_traite` est renommée en `salaire_mensuel`. Les individus dont le métier `q4a_02` est manquant sont retirés, le milieu de résidence manquant est remplacé par son mode et le métier est converti en chaîne de caractères.

La table finale est exportée dans `data/processed/df_features_score.csv`. Cet export constitue la matrice de travail du modèle.

## 7. Entraînement des modèles

Le code d'entraînement prévu dans le notebook de feature engineering suit les étapes suivantes :

1. charger `df_features_score.csv` ;
2. séparer les variables explicatives `X` et la cible `y` ;
3. exclure `idHH_clean` de l'apprentissage ;
4. encoder les variables catégorielles avec `pd.get_dummies(drop_first=True)` ;
5. séparer les données en un ensemble d'entraînement de 80 % et un ensemble de test de 20 % avec `random_state=42` ;
6. entraîner deux modèles de régression.

Les modèles comparés sont :

- `RandomForestRegressor`, avec 100 arbres et une profondeur maximale de 12 ;
- `XGBRegressor`, avec 100 estimateurs, un taux d'apprentissage de 0,08 et une profondeur maximale de 6.

La comparaison repose sur trois métriques :

- **MAE** : erreur absolue moyenne, plus elle est faible, meilleur est le modèle ;
- **RMSE** : racine de l'erreur quadratique moyenne, plus sensible aux grandes erreurs ;
- **R2** : part de la variance expliquée par le modèle, meilleure lorsqu'elle est proche de 1.

Le modèle XGBoost est ensuite sélectionné comme meilleur modèle dans le code prévu et sauvegardé avec `joblib`.

## 8. Évaluation et prédiction

L'évaluation prévue recharge le modèle et recalcule les variables encodées. Deux graphiques sont produits :

1. un nuage de points comparant les scores réels et prédits, avec la diagonale idéale ;
2. un histogramme des résidus `réel - prédit`, accompagné d'une estimation de densité.

La classe `SocioEconomicScoreModule` fournit ensuite deux opérations :

### Prédiction individuelle

`predict_individual_score` reçoit les caractéristiques d'un travailleur sous la forme d'un dictionnaire. Elles sont transformées en DataFrame, encodées avec `get_dummies`, puis réalignées sur les colonnes attendues par le modèle. Le score retourné est borné entre 0 et 100.

### Agrégation familiale

`compute_family_score` calcule un score de ménage pondéré par les salaires :

```text
family_score = somme(score_i * salaire_i) / somme(salaire_i)
```

Si aucun travailleur n'est fourni, le résultat est 0. Si la somme des salaires vaut zéro, une moyenne arithmétique des scores individuels est utilisée pour éviter une division par zéro.

## 9. État actuel et points à finaliser

Le projet contient une base solide de préparation et d'exploration, mais plusieurs éléments doivent être finalisés avant une mise en production :

- les notebooks `03_model_training.ipynb` et `04_evaluation.ipynb` sont vides ;
- les scripts du dossier `src/` ne contiennent pas encore le pipeline opérationnel ;
- les métriques d'entraînement ne sont pas conservées dans un fichier de résultats ;
- le modèle mentionné dans le code (`score_individuel_model.pkl`) ne correspond pas exactement aux fichiers visibles dans `models/` (`final_model.pkl` et `scaler.pkl`) ;
- la cible est en partie construite à partir de règles et d'imputations, et non d'une mesure directement observée ;
- certaines composantes du score utilisent encore des valeurs constantes par défaut lorsque les variables ne sont pas détectées ;
- l'encodage utilisé à l'entraînement et celui utilisé à la prédiction devront être figés dans un pipeline afin de garantir les mêmes colonnes ;
- une validation croisée, une analyse des biais par région et milieu, ainsi qu'une comparaison avec un modèle de référence seraient utiles avant de conclure sur la qualité du modèle.

## 10. Conclusion

Le travail réalisé permet de passer de fichiers d'enquête hétérogènes à une base structurée pour l'analyse socio-économique. Les principales contributions sont l'harmonisation des identifiants ménages, l'intégration de plusieurs sources EPM, l'estimation des revenus à partir des métiers, la construction d'indicateurs de logement et d'impôts, et la définition d'un score individuel pondéré.

La prochaine étape consiste à transformer les cellules de notebook en scripts reproductibles, à enregistrer le modèle et les colonnes d'encodage dans des artefacts cohérents, puis à valider les performances et l'interprétation du score sur un jeu de test indépendant.