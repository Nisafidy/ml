
1) Information générerale sur EPM
Dimensions du jeu de données : 67969 lignes et 175 colonnes.
--- Informations Générales (Types & Valeurs manquantes) ---
<class 'pandas.DataFrame'>
RangeIndex: 67969 entries, 0 to 67968
Columns: 175 entries, idHH to q4c_09
dtypes: float64(33), int64(5), object(13), str(124)
memory usage: 90.7+ MB
--- Statistiques Descriptives ---
count	mean	std	min	25%	50%	75%	max
idHH	67969.0	70570.278480	40572.650167	101.0	35508.00	70611.0	105806.0	140612.0
hhgrap	67969.0	705.637908	405.726244	1.0	355.00	706.0	1058.0	1406.0
hhnum	67969.0	6.487634	3.466611	1.0	3.00	6.0	10.0	12.0
q1_0x	67969.0	3.046301	1.961319	1.0	2.00	3.0	4.0	19.0
q4a_00	67969.0	1.589548	0.836973	1.0	1.00	1.0	2.0	15.0
q4a_14	0.0	NaN	NaN	NaN	NaN	NaN	NaN	NaN
q4a_17	23886.0	1.095370	0.313452	1.0	1.00	1.0	1.0	4.0
q4a_19	23870.0	6909.792208	2054.601676	9.0	6111.00	7111.0	9133.0	9700.0
q4a_19a	23872.0	70.280370	674.851066	0.0	6.00	7.0	9.0	9333.0
q4a_19b	23869.0	1.949684	0.879933	0.0	1.00	2.0	2.0	9.0
q4a_19c	23865.0	1.970459	1.357430	0.0	1.00	1.0	3.0	9.0
q4a_19d	23847.0	1.382522	1.692282	0.0	0.00	1.0	2.0	9.0
q4a_23a	22925.0	28.731298	32.857510	0.0	1.00	10.0	47.0	99.0
q4a_23b	22920.0	2.648298	2.610931	0.0	1.00	1.0	4.0	9.0
q4a_23c	22898.0	2.444187	2.907095	0.0	1.00	1.0	2.0	9.0
q4a_34	1780.0	24.397191	17.429021	0.0	15.00	30.0	30.0	300.0
q4a_44	1837.0	37.911813	35.290066	1.0	7.00	30.0	60.0	245.0
q4a_49	23886.0	22019.630746	1409.046605	11112.0	22222.00	22222.0	22222.0	22222.0
q4a_54	2137.0	6669.455311	1935.165723	110.0	6121.00	6210.0	9111.0	9333.0
q4a_54a	2132.0	6.481707	1.972391	0.0	6.00	6.0	9.0	9.0
q4a_54b	2137.0	2.047730	1.502983	1.0	1.00	2.0	2.0	9.0
q4a_54c	2137.0	1.629387	1.060103	1.0	1.00	1.0	2.0	9.0
q4a_54d	2132.0	1.243433	1.790881	0.0	0.00	1.0	1.0	9.0
q4a_56a	2137.0	13.588676	26.695848	1.0	1.00	1.0	7.0	99.0
q4a_56b	2137.0	2.738418	2.399943	0.0	1.00	1.0	4.0	9.0
q4a_56c	2134.0	2.542643	2.422703	0.0	1.00	2.0	3.0	9.0
q4a_59	2140.0	5.240654	4.856282	0.0	2.00	3.0	9.0	78.0
q4a_64a	12.0	865.666667	2876.758572	3.0	15.00	20.0	62.5	10000.0
q4a_66a	11.0	1391.636364	3220.541329	3.0	10.00	30.0	90.0	10000.0
q4a_70	782.0	5.191816	1.538756	1.0	4.00	6.0	6.0	7.0
q4a_71	782.0	6.746803	2.955900	0.0	5.00	6.0	8.0	24.0
q4a_82	30.0	11.766667	9.023660	1.0	5.25	8.5	17.5	40.0
q4a_91	5630.0	3.700533	1.816854	1.0	2.00	3.0	5.0	7.0
q4a_94	2447.0	5.318758	2.208969	1.0	3.00	7.0	7.0	7.0
q4c_06a2	620.0	43.872581	33.157697	1.0	10.00	47.0	64.0	99.0
q4c_06a3	620.0	2.624194	2.884261	0.0	1.00	1.0	4.0	9.0
q4c_06a4	620.0	2.458065	3.302202	0.0	0.00	1.0	3.0	9.0
q4c_09	659.0	0.575114	0.641796	0.0	0.00	1.0	1.0	8.0


--- LIBELLÉS DES COLONNES CLÉS ---
idhh       -> ID Ménage
q4a_17     -> # emplois ou activités professionnelles
q4a_19     -> CITP
q4a_23a    -> NOMACa
q4a_46a    -> Montant salaire

--- POPULATION ET ÉCHANTILLON ---
Nombre total d'individus dans la base : 67969
Nombre d'actifs identifiés (q4a_17)   : 23886 (35.1%)
Colonnes potentielles pour le salaire dans df : ['q4a_46b', 'q4a_46c']

2) Traitement de la partie Métier.

================================================================================
EXPLORATION DES VALEURS UNIQUES - MÉTIERS
================================================================================
✅ metiers_extraits.csv : 67969 lignes
✅ metier.csv : 89 lignes

================================================================================
📋 ANALYSE DE metier.csv (SOURCE DE RÉFÉRENCE)
================================================================================

📌 Structure de metier.csv :
<class 'pandas.DataFrame'>
RangeIndex: 89 entries, 0 to 88
Data columns (total 6 columns):
 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   secteur               89 non-null     str  
 1   metier                89 non-null     str  
 2   salaire_min_ariary    89 non-null     int64
 3   salaire_max_ariary    89 non-null     int64
 4   salaire_moyen_ariary  89 non-null     int64
 5   type                  89 non-null     str  
dtypes: int64(3), str(3)
memory usage: 4.3 KB
None

📌 Aperçu des métiers de référence :
        secteur                               metier  salaire_moyen_ariary
0       General         Salaire minimum non agricole                262680
1       General             Salaire minimum agricole                266500
2       General        Salaire moyen national estimé                196359
3   Agriculture                     Ouvrier agricole                225000
4   Agriculture                      Chef de culture                500000
5   Agriculture  Responsable d'exploitation agricole                850000
6     Industrie                 Ouvrier non qualifié                200000
7     Industrie                     Ouvrier qualifié                375000
8     Industrie                Superviseur d'atelier                600000
9     Industrie            Technicien de maintenance                500000
10    Industrie                 Ingénieur production               1100000
11          BTP                       Maine d'oeuvre                200000
12          BTP                                Maçon                325000
13          BTP                 Électricien bâtiment                425000
14          BTP                             Plombier                425000
15          BTP                     Chef de chantier                850000
16          BTP                Conducteur de travaux               1300000
17    Transport                            Chauffeur                425000
18    Transport                              Livreur                325000
19    Transport       Receveur / assistant transport                265000

📌 Statistiques :
  - Nombre total de métiers : 89
  - Nombre de secteurs : 19
  - Salaires - Min : 162,000
  - Salaires - Max : 7,500,000
  - Salaires - Moyen : 1,315,252

📋 LISTE COMPLÈTE DES MÉTIERS DE RÉFÉRENCE :
------------------------------------------------------------
  1. Salaire minimum non agricole             (General)
  2. Salaire minimum agricole                 (General)
  3. Salaire moyen national estimé            (General)
  4. Ouvrier agricole                         (Agriculture)
  5. Chef de culture                          (Agriculture)
  6. Responsable d'exploitation agricole      (Agriculture)
  7. Ouvrier non qualifié                     (Industrie)
  8. Ouvrier qualifié                         (Industrie)
  9. Superviseur d'atelier                    (Industrie)
 10. Technicien de maintenance                (Industrie)
 11. Ingénieur production                     (Industrie)
 12. Maine d'oeuvre                           (BTP)
 13. Maçon                                    (BTP)
 14. Électricien bâtiment                     (BTP)
 15. Plombier                                 (BTP)
 16. Chef de chantier                         (BTP)
 17. Conducteur de travaux                    (BTP)
 18. Chauffeur                                (Transport)
 19. Livreur                                  (Transport)
 20. Receveur / assistant transport           (Transport)
 21. Responsable logistique                   (Transport)
 22. Vendeur                                  (Commerce)
 23. Caissier                                 (Commerce)
 24. Commercial terrain                       (Commerce)
 25. Chef de vente                            (Commerce)
 26. Responsable commercial                   (Commerce)
 27. Serveur                                  (Hôtellerie)
 28. Barman                                   (Hôtellerie)
 29. Réceptionniste                           (Hôtellerie)
 30. Chef de réception                        (Hôtellerie)
 31. Responsable hôtelier                     (Hôtellerie)
 32. Cuisinier                                (Restauration)
 33. Aide-cuisinier                           (Restauration)
 34. Chef cuisinier                           (Restauration)
 35. Agent administratif                      (Administration)
 36. Secrétaire                               (Administration)
 37. Comptable                                (Administration)
 38. Chef comptable                           (Administration)
 39. Assistant de direction                   (Administration)
 40. Directeur administratif                  (Administration)
 41. Instituteur public                       (Éducation)
 42. Enseignant privé                         (Éducation)
 43. Professeur de lycée                      (Éducation)
 44. Formateur                                (Éducation)
 45. Aide-soignant                            (Santé)
 46. Infirmier                                (Santé)
 47. Médecin généraliste                      (Santé)
 48. Médecin spécialiste                      (Santé)
 49. Pharmacien                               (Santé)
 50. Dentiste                                 (Santé)
 51. Développeur junior                       (Technologie)
 52. Développeur confirmé                     (Technologie)
 53. Développeur senior                       (Technologie)
 54. Data Analyst                             (Technologie)
 55. Data Scientist                           (Technologie)
 56. Ingénieur DevOps / Cloud                 (Technologie)
 57. Chef de projet IT                        (Technologie)
 58. Product Manager                          (Technologie)
 59. UI Designer                              (Technologie)
 60. UX Designer                              (Technologie)
 61. Community Manager                        (Technologie)
 62. SEO / SEA Specialist                     (Technologie)
 63. Caissier banque                          (Finance)
 64. Comptable bancaire                       (Finance)
 65. Analyste financier                       (Finance)
 66. Auditeur                                 (Finance)
 67. Trader                                   (Finance)
 68. Gestionnaire de crédit                   (Finance)
 69. Chef comptable                           (Finance)
 70. Agent public débutant                    (Fonction publique)
 71. Cadre administratif public               (Fonction publique)
 72. Cadre supérieur public                   (Fonction publique)
 73. Garde de sécurité                        (Sécurité)
 74. Agent de sécurité confirmé               (Sécurité)
 75. Responsable sécurité                     (Sécurité)
 76. Couturier                                (Artisanat)
 77. Menuisier                                (Artisanat)
 78. Coiffeur                                 (Artisanat)
 79. Mécanicien                               (Artisanat)
 80. Journaliste                              (Communication)
 81. Rédacteur web                            (Communication)
 82. Graphiste                                (Communication)
 83. Photographe                              (Communication)
 84. Agent immobilier                         (Immobilier)
 85. Gestionnaire immobilier                  (Immobilier)
 86. Responsable patrimoine                   (Immobilier)
 87. Chargé de projet                         (NGO_Association)
 88. Coordinateur de programme                (NGO_Association)
 89. Directeur de programme                   (NGO_Association)

================================================================================
📋 ANALYSE DE q4a_18 (MÉTIER PRINCIPAL)
================================================================================

📌 Statistiques :
  - Nombre total de valeurs uniques : 7502
  - Pourcentage de remplissage : 35.1%

📋 PREMIÈRES 50 VALEURS UNIQUES :
------------------------------------------------------------
  1. %PANDRY OMBY
  2. 0MBIASA
  3. 0MBIASY
  4. 0PERATEUR DE SAISIE
  5. 0PERATEUR ECONOMIQUE
  6. 0PERATEUR INFORMATIQUE
  7. 0RGANISATEUR PETANQUE (CONCOURS)
  8. 3EME ADJOINT AU CHEF DE DISTRICT
  9. 3EME ADJOINT MAIRE
 10. ACCEIL D'UN BUNLALOW
 11. ACCEUIL
 12. ACCOMPAGNATEUR ECONOMIQUE
 13. ACCOUCHEUSE TRADITIONNELLE
 14. ACCUEIL
 15. ADJOINT ADMINISTRATIF
 16. ADJOINT FOKONTANY
 17. ADJOINT FOKOTANY
 18. ADJOINT PRESIDENT FOKONTANY
 19. ADJOINT SEFOMPOKOTANY
 20. ADJOINT STATISTIQUE
 21. ADJOINT TECHNIQUE BTP
 22. ADJOUINT TECHNIQUE DEA EAUX ET FORET
 23. ADJUDANT CHEF
 24. ADMINISTRATIF FINANCIER SISCO BETROKA
 25. ADMINISTRATION
 26. AFERA NA VATO
 27. AGANT COMMUNAURAIRE
 28. AGEANT CONNECTO
 29. AGENCE DE CONSEIL DE LA SANTE
 30. AGENT
 31. AGENT ADMINISTRATIF OTIV
 32. AGENT BATIMENT
 33. AGENT CADRE JIRAMA
 34. AGENT CAUMMUNAUTAIRE
 35. AGENT CHARGE D'ETUDE ET CONTROLE EN GENIE CIVIL
 36. AGENT COMMERCIAL
 37. AGENT COMMERCIAL CANAL+
 38. AGENT COMMERCIALE
 39. AGENT COMMERCILE
 40. AGENT COMMUNAUTAIRE
 41. AGENT COMPTABLE
 42. AGENT COMPTABLE CHAMBRE DE COMMERCE
 43. AGENT COMPTOIRE PHARMACIE
 44. AGENT D'ACCEUIL
 45. AGENT D'ACCEUIL AU CHU ANDROVA
 46. AGENT D'ACCOMPAINNEMENT
 47. AGENT D'ACCUEIL
 48. AGENT D'ASSURENCE
 49. AGENT DE BARRIERE AO MPANAO LAVAGE TOMOBILE
 50. AGENT DE CHANTIER

📋 DERNIÈRES 50 VALEURS UNIQUES :
------------------------------------------------------------
7453. VERIFICATEUR DE GIROFLE
7454. VERIFICATEUR DE LA VANILLE
7455. VERIFICATEUR ETIQUETE COMMUN
7456. VETERINAIRE
7457. VETERNAIRE
7458. VICE PRESIDENT FOKONTANY
7459. VIDéASTE
7460. VOATAVO
7461. VOLO VOANJO
7462. VOLY FARY
7463. VOLY LA VANILLE
7464. VOLY LAISO
7465. VOLY LAISOA
7466. VOLY MANGAHAZO
7467. VOLY OVY MADINIKA
7468. VOLY TRAKA
7469. VOLY VANILLE
7470. VOLY VARY
7471. VOLY VARY SY LA VANILLE
7472. VOMIERAN NY FOKONTANY
7473. WEBMASTER
7474. ZAITRA
7475. ZANDARIMARIA
7476. agent d execution
7477. comissionaire vanille,cafe
7478. couturière
7479. fambolena
7480. fambolena madinika (ovy)
7481. gardien
7482. inspecteure de police
7483. karamaina manao mecanicien electronique
7484. mamboly vary
7485. manao travail(mamboly amin'olona)
7486. maçon
7487. maçons (sarakatsaha)
7488. mividy dia mivarotra trondromaina
7489. mpajono
7490. mpamboly
7491. mpamboly vary
7492. mpampianatra @ epp
7493. mpampianatra fram
7494. mpivarotra
7495. mpivarotra @ epicerie
7496. mpivarotra lamba
7497. saraka an-tsaha
7498. saraka antsaha
7499. sarakantaha
7500. sarakatsaha
7501. sarankatsaha
7502. ²MANAMPY NY RENINY AMIN'NY ASA FAMBOLENA

================================================================================
📋 ANALYSE DE q4a_541 (MÉTIER SECONDAIRE)
================================================================================

📌 Statistiques :
  - Nombre total de valeurs uniques : 948
  - Pourcentage de remplissage : 3.1%

📋 PREMIÈRES 50 VALEURS UNIQUES :
------------------------------------------------------------
  1. 0MBIASA
  2. ADJOINT MAIRE
  3. ADJOINT PRESIDENT FOKOTANY
  4. AGENT COMMUNAUTAIRE
  5. AGENT COMUNNAUTAIRE
  6. AIDE MACON
  7. AIDE MANOEUVRE
  8. AIDE MULTISERVICE
  9. ANIMATEUR CECALINE
 10. ANIMATEUR D'EVENEMENT
 11. ARTISANS (MANDRARY TSIHY
 12. BOANA MARO
 13. CHARPENTIER
 14. CHAUFFEUR VOITURE DE LOCATION
 15. CHEF FOKONTANY
 16. CHEF QUARTIER
 17. COIFFEUSE
 18. COLLECTEUR,CANEL,JIROFO,CAFE,VARY
 19. COMMISIONAIRE VANILLE
 20. COMMISSIONNAIRE DE VANILLE
 21. CONSEILLER COMMUNALE
 22. CONSEILLER MUNICIPALE
 23. CORDOONATRICE ALIANCE FRANCAISE
 24. CUISINIER
 25. CUISINIERE
 26. DEMARCHEUR
 27. DEMARCHEUR CONFECTION
 28. DEMARCHEUR NY SAPHIRE
 29. DEMARCHEUR VATO SAFIRA
 30. DJ
 31. DOCKER
 32. DOKERA
 33. ELECTRICIEN
 34. ELECTRICIEN MPANAMBOATRA TELE SY RADIO SIMBA
 35. ELEVEUR BETAIL
 36. ELEVEUR DE BETAIL DESTINE AU MARCHE
 37. EPICERIE
 38. EXPLOITANT ET VENDEUR DU BOZAKA
 39. FAMBOLEM-BARY
 40. FAMBOLENA
 41. FAMBOLENA COLA
 42. FAMBOLENA HARICOT VERT SOJA PETIT POIS
 43. FAMBOLENA KATSAKA
 44. FAMBOLENA MANGAHAZO
 45. FAMBOLENA MANGAHAZO, OVY
 46. FAMBOLENA OVY MADINIKA
 47. FAMBOLENA SY FIVAROTANA ANANAS
 48. FAMBOLENA TSAKOTSAKO
 49. FAMBOLENA VANILLE
 50. FAMBOLENA VARY

📋 DERNIÈRES 50 VALEURS UNIQUES :
------------------------------------------------------------
899. SARAKANTSAHA
900. SARAKANTSAHA (MIKARAMA MANETSA)
901. SARAKANTSAHA (mikarama miava vary)
902. SARAKANTSAHA FA MIKARAMA AMINY OMBINY
903. SARAKANTSAHA MANOSIKA SARCLEUSE
904. SARAKANTSAHA MIASA TANY
905. SARAKANTSAHA MIASA TANY NA MIAVA VARY
906. SARAKANTSAHA MIAVA PARAKY
907. SARAKANTSAHA MIAVA VARY
908. SARAKANTSAHA MIAVA VARY AMINY SARCLEUSE
909. SARAKANTSAHA MIAVA VARY TANANA
910. SARAKANTSAHA MIJINJA VARY
911. SARAKANTSAHA(amin'ny Omby sy angady tanana)
912. SARAKANTSAHA(miasa tany mangahazo)
913. SARAKATSAHA
914. SARAKATSAHA (MIHAVA VARY)
915. SARAKATSAHA MANOSAIKA SARCLEUSE
916. SARAKATSAHA MANOSIKA SARCLEUSE
917. SARAKATSAHA MIADY OVY
918. SARAKATSAHA MIADY VOANJO
919. SARAKATSAHA MIASA AMINY ANGADIN'OMBY
920. SARAKATSAHA MIASA TANY
921. SARAKATSAHA MIAVA PARAKY
922. SARAKATSAHA MIAVA VARY
923. SARAKATSAHA MIAVA VARY AMINY SARCLEUSE
924. SARAKATSAHA MIAVA VARY TANANA
925. SARAKATSAHA MIJINJA VARY
926. SARAKATSAHA MIKARAMA AMIN'NY OMBY
927. SARAKATSAHA MITANGO KATSAKA
928. SARAKATSAHA MITAOM-BARY
929. SARAKATSAHA MITAONA VARY
930. SARAKATSAHA MIVELY VARY
931. SARAKATSAHA NANETSA
932. SARAKATSAHA VARY
933. SARAKATSAHY
934. SARANKATSAHA
935. SARANKATSAHA MIASA TANANA
936. SASALAMBA
937. SERVICE TAXI VILLE
938. SERVICE VENTE
939. TAXI MOTO
940. TRAITEUR
941. TRANSPORTEUR TAXIBROUSSE
942. VENDEUSE
943. VENTE EN LIGNE
944. VENTE EN LIGNE RESAKA DECORATION LOCATION EVENEMEN
945. VOLY TONGOLO RAVINA
946. VOLY VARY MADINIKA
947. matsaka rano
948. mpivarotra glaçon

================================================================================
🔍 COMPARAISON ENTRE q4a_18 ET metier.csv
================================================================================

📌 Correspondances exactes :
  - q4a_18 : 31 valeurs correspondent exactement à metier.csv
  - Soit 0.4% des valeurs uniques

📋 Exemples de correspondances exactes :
  - chef de chantier
  - chauffeur
  - maçon
  - caissier
  - maçon
  - responsable logistique
  - livreur
  - comptable
  - cuisinier
  - serveur
  - chef comptable
  - coiffeur
  - vendeur
  - barman
  - maçon
  - menuisier
  - responsable commercial
  - maçon
  - agent immobilier
  - infirmier

================================================================================
🔍 ANALYSE DES MOTS-CLÉS DANS q4a_18
================================================================================

📌 Top 30 mots-clés les plus fréquents :
------------------------------------------------------------
  mivarotra            : 900 occurrences
  sy                   : 710 occurrences
  mamboly              : 467 occurrences
  mpivarotra           : 452 occurrences
  vary                 : 405 occurrences
  de                   : 313 occurrences
  manao                : 299 occurrences
  mpamboly             : 246 occurrences
  amin'ny              : 190 occurrences
  mpampianatra         : 178 occurrences
  manampy              : 176 occurrences
  ao                   : 153 occurrences
  @                    : 151 occurrences
  manamboatra          : 147 occurrences
  mpanao               : 147 occurrences
  ny                   : 146 occurrences
  mofo                 : 144 occurrences
  trano                : 117 occurrences
  mangahazo            : 112 occurrences
  chauffeur            : 111 occurrences
  aminy                : 111 occurrences
  fambolena            : 106 occurrences
  mikarama             : 106 occurrences
  mampianatra          : 97 occurrences
  vanille              : 96 occurrences
  lamba                : 91 occurrences
  entana               : 90 occurrences
  amin                 : 88 occurrences
  mpanamboatra         : 87 occurrences
  la                   : 87 occurrences

💾 Sauvegarde des résultats...
✅ Fichiers sauvegardés :
  - valeurs_uniques_q4a_18.txt
  - valeurs_uniques_q4a_541.txt
  - mots_cles_q4a_18.txt
  - q4a_18_uniques.csv
  - q4a_541_uniques.csv

================================================================================
✅ EXPLORATION TERMINÉE
================================================================================
import pandas as pd
salaire_par_secteur = df_metier.groupby('secteur')['salaire_moyen_ariary'].mean().to_dict()
print("\n📊 Salaires moyens par secteur :")
for secteur, salaire in salaire_par_secteur.items():
    print(f"  {secteur:<20} : {salaire:>10,.0f} Ariary")

# 3.3 Attribuer le salaire par secteur
df_empl['salaire_secteur'] = df_empl['secteur_nom'].map(salaire_par_secteur)

# 3.4 Si pas de secteur, utiliser la médiane
median_salaire = df_metier['salaire_moyen_ariary'].median()
df_empl['salaire_secteur'] = df_empl['salaire_secteur'].fillna(median_salaire)

print(f"\n✅ Salaire par secteur attribué à {df_empl['salaire_secteur'].notna().sum()} individus")

# ============================================================================
# 4. APPROCHE PAR MILIEU (URBAIN/RURAL)
# ============================================================================

print("\n" + "="*80)
print("AJUSTEMENT PAR MILIEU (URBAIN/RURAL)")
print("="*80)

# 4.1 Fusionner avec les données de logement
df_empl['idHH_clean'] = df_empl['idHH'].astype(str).str.zfill(12)
df_loge['idHH_clean'] = df_loge['idHH_clean'].astype(str).str.zfill(12)

df_empl = df_empl.merge(df_loge[['idHH_clean', 'hhmilieu2']], on='idHH_clean', how='left')

# 4.2 Ajuster le salaire par milieu
# Urbain = 1.3 * salaire secteur, Rural = 0.7 * salaire secteur
df_empl['salaire_ajuste'] = df_empl.apply(
    lambda row: row['salaire_secteur'] * 1.3 if row['hhmilieu2'] == 1 else row['salaire_secteur'] * 0.7,
    axis=1
)

print(f"\n📊 Salaires ajustés par milieu :")
print(f"  - Urbain (hhmilieu2=1) : {df_empl[df_empl['hhmilieu2']==1]['salaire_ajuste'].mean():.0f} Ariary")
print(f"  - Rural (hhmilieu2=2) : {df_empl[df_empl['hhmilieu2']==2]['salaire_ajuste'].mean():.0f} Ariary")

# ============================================================================
# 5. CONSTRUCTION DU FICHIER FINAL
# ============================================================================

print("\n" + "="*80)
print("CONSTRUCTION DU FICHIER FINAL")
print("="*80)

# 5.1 Créer le fichier final
df_final = pd.DataFrame({
    'idHH': df_empl['idHH'],
    'salaire_mensuel': df_empl['salaire_ajuste'].round(0).astype(int),
    'hhmilieu2': df_empl['hhmilieu2'].fillna(2),
    'hhreg': df_empl.get('hhreg', 33).fillna(33),
    'q4a_02': df_empl.get('q4a_02', 'Non').fillna('Non'),
    'score_individuel_epm': 0  # À calculer plus tard
})

# 5.2 Supprimer les doublons
df_final = df_final.drop_duplicates(subset=['idHH'], keep='first')

# 5.3 Statistiques finales
print("\n📊 Statistiques finales :")
print(df_final['salaire_mensuel'].describe())

# 5.4 Sauvegarder
output_path = '../data/processed/final_ml_ready.csv'
df_final.to_csv(output_path, index=False)
print(f"\n✅ Fichier sauvegardé : {output_path}")
print(f"   Dimensions : {df_final.shape}")

# ============================================================================
# 6. COMPARAISON AVEC LA MÉTHODE PRÉCÉDENTE
# ============================================================================

print("\n" + "="*80)
print("COMPARAISON AVEC LA MÉTHODE PRÉCÉDENTE")
print("="*80)

print("\n📊 Cette approche est plus honnête car :")
print("  1. Elle utilise le secteur (NOMAC) plutôt que des mots-clés")
print("  2. Elle ajuste par milieu (urbain/rural)")
print("  3. Elle ne crée pas de correspondances artificielles")
print("  4. Les salaires sont basés sur des données réelles (metier.csv)")

print("\n" + "="*80)
print("✅ PROCESSUS TERMINÉ")
print("="*80)
================================================================================
APPROCHE HONNÊTE POUR LE SALAIRE
================================================================================
✅ EMPL_complet : 67969 individus
✅ metier.csv : 89 métiers
✅ df_loge : 16871 ménages

================================================================================
ANALYSE DES SALAIRES RÉELS (q4a_54)
================================================================================

✅ 2137 individus ont un salaire réel (3.1%)

📊 Statistiques des salaires réels :
count    2137.000000
mean     6669.455311
std      1935.165723
min       110.000000
25%      6121.000000
50%      6210.000000
75%      9111.000000
max      9333.000000
Name: salaire_reel, dtype: float64


================================================================================
APPROCHE PAR SECTEUR (NOMAC)
================================================================================

📊 Distribution des secteurs :
secteur_nom
Agriculture       10597
Commerce           4249
Industrie          2810
Transport          1140
Services           1064
Hôtellerie          968
Éducation           968
Artisanat           838
Administration      671
Santé               273
Communication       116
Finance             106
Construction         27
Immobilier           23
Name: count, dtype: int64

📊 Salaires moyens par secteur :
  Administration       :  1,079,167 Ariary
  Agriculture          :    525,000 Ariary
  Artisanat            :    388,750 Ariary
  BTP                  :    587,500 Ariary
  Commerce             :    785,000 Ariary
  Communication        :    587,500 Ariary
  Finance              :  1,454,000 Ariary
  Fonction publique    :    766,667 Ariary
  General              :    241,846 Ariary
  Hôtellerie           :    763,373 Ariary
  Immobilier           :  1,100,000 Ariary
  Industrie            :    555,000 Ariary
  NGO_Association      :  1,350,000 Ariary
  Restauration         :    688,333 Ariary
  Santé                :    789,500 Ariary
  Sécurité             :    480,000 Ariary
  Technologie          :  4,854,167 Ariary
  Transport            :    516,250 Ariary
  Éducation            :    487,500 Ariary

✅ Salaire par secteur attribué à 67969 individus

================================================================================
AJUSTEMENT PAR MILIEU (URBAIN/RURAL)
================================================================================

📊 Salaires ajustés par milieu :
  - Urbain (hhmilieu2=1) : 844236 Ariary
  - Rural (hhmilieu2=2) : 435599 Ariary

================================================================================
CONSTRUCTION DU FICHIER FINAL
================================================================================
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[2], line 137
    133 df_final = pd.DataFrame({
    134     'idHH': df_empl['idHH'],
    135     'salaire_mensuel': df_empl['salaire_ajuste'].round(0).astype(int),
    136     'hhmilieu2': df_empl['hhmilieu2'].fillna(2),
--> 137     'hhreg': df_empl.get('hhreg', 33).fillna(33),
    138     'q4a_02': df_empl.get('q4a_02', 'Non').fillna('Non'),
    139     'score_individuel_epm': 0  # À calculer plus tard
    140 })

AttributeError: 'int' object has no attribute 'fillna'
import pandas as pd
df_final = pd.DataFrame({
    'idHH': df_empl['idHH'],
    'salaire_mensuel': df_empl['salaire_ajuste'].round(0).astype(int),
    'hhmilieu2': df_empl['hhmilieu2'].fillna(2).astype(int),
    'hhreg': df_empl['hhreg'].astype(int),
    'q4a_02': df_empl['q4a_02'],
    'score_individuel_epm': 0  # À calculer plus tard
})

# 5.3 Supprimer les doublons
df_final = df_final.drop_duplicates(subset=['idHH'], keep='first')

# 5.4 Statistiques finales
print("\n📊 Statistiques finales :")
print(df_final['salaire_mensuel'].describe())

print("\n📊 Distribution par milieu :")
print(df_final.groupby('hhmilieu2')['salaire_mensuel'].agg(['mean', 'std', 'count']))

# 5.5 Sauvegarder
output_path = '../data/processed/final_ml_ready.csv'
df_final.to_csv(output_path, index=False)
print(f"\n✅ Fichier sauvegardé : {output_path}")
print(f"   Dimensions : {df_final.shape}")

# ============================================================================
# 6. ANALYSE DE LA DISTRIBUTION
# ============================================================================

print("\n" + "="*80)
print("ANALYSE DE LA DISTRIBUTION")
print("="*80)

print("\n📊 Distribution des salaires par secteur :")
salaire_par_secteur_final = df_empl.groupby('secteur_nom')['salaire_ajuste'].mean().sort_values(ascending=False)
for secteur, salaire in salaire_par_secteur_final.head(10).items():
    print(f"  {secteur:<20} : {salaire:>10,.0f} Ariary")

# ============================================================================
# 7. VISUALISATION (optionnelle)
# ============================================================================

try:
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Distribution des salaires
    df_final['salaire_mensuel'].hist(bins=50, ax=axes[0], alpha=0.7, edgecolor='black')
    axes[0].set_title('Distribution des salaires')
    axes[0].set_xlabel('Salaire (Ariary)')
    axes[0].set_ylabel('Fréquence')
    axes[0].axvline(df_final['salaire_mensuel'].mean(), color='red', linestyle='--', 
                    label=f'Moyenne: {df_final["salaire_mensuel"].mean():.0f}')
    axes[0].axvline(df_final['salaire_mensuel'].median(), color='green', linestyle='--', 
                    label=f'Médiane: {df_final["salaire_mensuel"].median():.0f}')
    axes[0].legend()
    
    # Salaire par milieu
    df_final.boxplot(column='salaire_mensuel', by='hhmilieu2', ax=axes[1])
    axes[1].set_title('Salaire par milieu (1=Urbain, 2=Rural)')
    axes[1].set_xlabel('Milieu')
    axes[1].set_ylabel('Salaire (Ariary)')
    
    plt.tight_layout()
    plt.show()
except:
    print("⚠️ Visualisation non disponible")

print("\n" + "="*80)
print("✅ PROCESSUS TERMINÉ")
print("="*80)
================================================================================
APPROCHE HONNÊTE POUR LE SALAIRE - VERSION CORRIGÉE
================================================================================
✅ EMPL_complet : 67969 individus
✅ metier.csv : 89 métiers
✅ df_loge : 16871 ménages

================================================================================
ANALYSE DES SALAIRES RÉELS (q4a_54)
================================================================================

✅ 2137 individus ont un salaire réel (3.1%)

📊 Statistiques des salaires réels :
count    2137.000000
mean     6669.455311
std      1935.165723
min       110.000000
25%      6121.000000
50%      6210.000000
75%      9111.000000
max      9333.000000
Name: salaire_reel, dtype: float64

================================================================================
APPROCHE PAR SECTEUR (NOMAC)
================================================================================

📊 Distribution des secteurs :
secteur_nom
Agriculture       10597
Commerce           4249
Industrie          2810
Transport          1140
Services           1064
Hôtellerie          968
Éducation           968
Artisanat           838
Administration      671
Santé               273
Communication       116
Finance             106
Construction         27
Immobilier           23
Name: count, dtype: int64

📊 Salaires moyens par secteur (extrait) :
  Agriculture          :    525,000 Ariary
  Commerce             :    785,000 Ariary
  Industrie            :    555,000 Ariary
  Transport            :    516,250 Ariary
  Éducation            :    487,500 Ariary
  Santé                :    789,500 Ariary

✅ Salaire par secteur attribué à 67969 individus

================================================================================
AJUSTEMENT PAR MILIEU (URBAIN/RURAL)
================================================================================

📊 Salaires ajustés par milieu :
  - Urbain (hhmilieu2=1) : 844236 Ariary
  - Rural (hhmilieu2=2) : 435599 Ariary

================================================================================
CONSTRUCTION DU FICHIER FINAL
================================================================================

📊 Statistiques finales :
count    1.687100e+04
mean     6.236036e+05
std      2.683400e+05
min      2.721250e+05
25%      3.675000e+05
50%      5.495000e+05
75%      8.450000e+05
max      1.890200e+06
Name: salaire_mensuel, dtype: float64

📊 Distribution par milieu :
                    mean            std  count
hhmilieu2                                     
1          850666.471521  212385.663561   8076
2          415103.321433   76737.492865   8795

✅ Fichier sauvegardé : ../data/processed/final_ml_ready.csv
   Dimensions : (16871, 6)

================================================================================
ANALYSE DE LA DISTRIBUTION
================================================================================

📊 Distribution des salaires par secteur :
  Finance              :  1,824,358 Ariary
  Administration       :  1,248,520 Ariary
  Immobilier           :  1,200,435 Ariary
  Santé                :    894,477 Ariary
  Commerce             :    872,627 Ariary
  Hôtellerie           :    858,479 Ariary
  Construction         :    801,667 Ariary
  Services             :    745,667 Ariary
  Communication        :    666,509 Ariary
  Transport            :    586,895 Ariary


================================================================================
✅ PROCESSUS TERMINÉ
================================================================================
import pandas as pd
    ].mean()

    mediane = df_final[
        'salaire_mensuel'
    ].median()

    axes[0].axvline(
        moyenne,
        linestyle='--',
        label=f'Moyenne : {moyenne:,.0f}'
    )

    axes[0].axvline(
        mediane,
        linestyle='--',
        label=f'Médiane : {mediane:,.0f}'
    )

    axes[0].set_title(
        'Distribution des salaires'
    )

    axes[0].set_xlabel(
        'Salaire mensuel (Ariary)'
    )

    axes[0].set_ylabel(
        'Fréquence'
    )

    axes[0].legend()


    # ------------------------------------------------------------------------
    # Salaire par source
    # ------------------------------------------------------------------------

    df_final.boxplot(
        column='salaire_mensuel',
        by='source_salaire',
        ax=axes[1]
    )

    axes[1].set_title(
        'Salaire selon la source de l’estimation'
    )

    axes[1].set_xlabel(
        'Source'
    )

    axes[1].set_ylabel(
        'Salaire mensuel (Ariary)'
    )

    plt.suptitle('')

    plt.tight_layout()

    plt.show()


except Exception as e:

    print(
        f"\n⚠️ Visualisation non disponible : {e}"
    )


print("\n" + "=" * 80)
print("✅ PROCESSUS TERMINÉ")
print("=" * 80)
import pandas as pd
    'score_individuel_epm'
]

df_ml = df[cols_ml].copy()

# 3.3 Nettoyer les valeurs manquantes
df_ml['hhmilieu2'] = df_ml['hhmilieu2'].fillna(2).astype(int)
df_ml['hhreg'] = df_ml['hhreg'].fillna(33).astype(int)
df_ml['q4a_02'] = df_ml['q4a_02'].fillna('Non')
df_ml['metier_trouve'] = df_ml['metier_trouve'].fillna('Inconnu')
df_ml['salaire_mensuel'] = df_ml['salaire_mensuel'].fillna(df_ml['salaire_mensuel'].median())

# 3.4 Aperçu
print("\n📋 Aperçu du dataset ML :")
print(df_ml.head())

print("\n📊 Statistiques du score EPM dans le dataset ML :")
print(df_ml['score_individuel_epm'].describe())

# ============================================================================
# 4. SAUVEGARDE
# ============================================================================

output_path = '../data/processed/df_features_score_with_metier.csv'
df_ml.to_csv(output_path, index=False)
print(f"\n✅ Fichier sauvegardé : {output_path}")
print(f"✅ Dimensions : {df_ml.shape}")

# ============================================================================
# 5. VISUALISATION
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 5.1 Distribution du score
df_ml['score_individuel_epm'].hist(bins=50, ax=axes[0,0], alpha=0.7, edgecolor='black')
axes[0,0].set_title('Distribution du score EPM')
axes[0,0].set_xlabel('Score EPM')
axes[0,0].set_ylabel('Fréquence')
axes[0,0].axvline(df_ml['score_individuel_epm'].mean(), color='red', linestyle='--', 
                  label=f'Moyenne: {df_ml["score_individuel_epm"].mean():.2f}')
axes[0,0].axvline(df_ml['score_individuel_epm'].median(), color='green', linestyle='--', 
                  label=f'Médiane: {df_ml["score_individuel_epm"].median():.2f}')
axes[0,0].legend()

# 5.2 Score par milieu
df_ml.boxplot(column='score_individuel_epm', by='hhmilieu2', ax=axes[0,1])
axes[0,1].set_title('Score EPM par milieu (1=Urbain, 2=Rural)')
axes[0,1].set_xlabel('Milieu')
axes[0,1].set_ylabel('Score EPM')

# 5.3 Salaire vs Score
sns.scatterplot(data=df_ml, x='salaire_mensuel', y='score_individuel_epm', alpha=0.1, ax=axes[1,0])
axes[1,0].set_title('Salaire vs Score EPM')
axes[1,0].set_xlabel('Salaire mensuel (Ariary)')
axes[1,0].set_ylabel('Score EPM')

# 5.4 Score par métier (top 10)
top_metiers = df_ml['metier_trouve'].value_counts().head(10).index
df_top = df_ml[df_ml['metier_trouve'].isin(top_metiers)]
df_top.boxplot(column='score_individuel_epm', by='metier_trouve', ax=axes[1,1])
axes[1,1].set_title('Score EPM par métier (Top 10)')
axes[1,1].set_xlabel('Métier')
axes[1,1].set_ylabel('Score EPM')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

print("\n" + "="*80)
print("✅ PROCESSUS TERMINÉ")
print("="*80)
import pandas as pd
import numpy as np
from collections import Counter
import re

print("="*80)
print("EXTRACTION DES MÉTIERS NON MATCHÉS")
print("="*80)

# 1. Chargement
df = pd.read_csv('../data/processed/final_ml_ready.csv')
df_empl = pd.read_csv('../data/raw/EMPL_complet.csv', low_memory=False)

print(f"✅ final_ml_ready : {df.shape[0]} lignes")
print(f"✅ EMPL_complet : {df_empl.shape[0]} lignes")

# 2. Identifier les métiers non matchés
# On prend les lignes où source_salaire = 'global' (pas de match)
df_global = df[df['source_salaire'] == 'global'].copy()

print(f"\n📊 Métiers non matchés (source='global') : {len(df_global)} individus")

# 3. Récupérer q4a_18 pour ces individus
df_empl['idHH_clean'] = df_empl['idHH'].astype(str).str.zfill(12)
df_global = df_global.merge(df_empl[['idHH_clean', 'q4a_18']], on='idHH_clean', how='left')

# 4. Extraire les valeurs uniques de q4a_18 pour les non matchés
valeurs_uniques = df_global['q4a_18'].dropna().unique()
valeurs_uniques = [str(v).strip() for v in valeurs_uniques if str(v).strip() != '']

print(f"\n📋 {len(valeurs_uniques)} valeurs uniques de métiers non matchés")

# 5. Compter les occurrences
comptage = df_global['q4a_18'].value_counts()

# 6. Afficher les 100 plus fréquents
print("\n" + "="*80)
print("TOP 100 MÉTIERS NON MATCHÉS (les plus fréquents)")
print("="*80)

for i, (metier, count) in enumerate(comptage.head(100).items(), 1):
    if pd.notna(metier) and str(metier).strip() != '':
        print(f"{i:>3}. {metier:<50} ({count} occurrences)")

# 7. Analyser la langue
print("\n" + "="*80)
print("ANALYSE DE LA LANGUE")
print("="*80)

# Mots-clés malgaches
mg_keywords = ['mpi', 'mam', 'man', 'miv', 'var', 'famb', 'tany', 'vary', 'omby', 'akoho', 'lamba', 'trano', 'rano', 'katsaka', 'mofo', 'entana']
# Mots-clés français
fr_keywords = ['agent', 'vendeur', 'maçon', 'chauffeur', 'comptable', 'secretaire', 'secrétaire', 'electricien', 'plombier', 'menuiser']

mg_count = 0
fr_count = 0
mixte_count = 0

for metier in valeurs_uniques:
    metier_lower = metier.lower()
    is_mg = any(kw in metier_lower for kw in mg_keywords)
    is_fr = any(kw in metier_lower for kw in fr_keywords)
    
    if is_mg and is_fr:
        mixte_count += 1
    elif is_mg:
        mg_count += 1
    elif is_fr:
import pandas as pd
mixte_count = 0
autre_count = 0

for metier in valeurs_uniques:
    metier_lower = metier.lower()
    is_mg = any(kw in metier_lower for kw in mg_keywords)
    is_fr = any(kw in metier_lower for kw in fr_keywords)
    
    if is_mg and is_fr:
        mixte_count += 1
    elif is_mg:
        mg_count += 1
    elif is_fr:
        fr_count += 1
    else:
        autre_count += 1

total = len(valeurs_uniques)
print(f"\n📊 Répartition linguistique :")
print(f"  - Malgache pur : {mg_count} ({mg_count/total*100:.1f}%)")
print(f"  - Français : {fr_count} ({fr_count/total*100:.1f}%)")
print(f"  - Mixte : {mixte_count} ({mixte_count/total*100:.1f}%)")
print(f"  - Autre : {autre_count} ({autre_count/total*100:.1f}%)")

# 9. Sauvegarder en CSV pour analyse
df_export = pd.DataFrame({
    'metier_original': valeurs_uniques,
    'occurrences': [comptage.get(m, 0) for m in valeurs_uniques]
})
df_export = df_export.sort_values('occurrences', ascending=False)

# Ajouter une colonne avec les mots-clés détectés
def detecter_langue(metier):
    metier_lower = str(metier).lower()
    mg_detect = [kw for kw in mg_keywords if kw in metier_lower]
    fr_detect = [kw for kw in fr_keywords if kw in metier_lower]
    return {
        'malgache': ', '.join(mg_detect) if mg_detect else '',
        'francais': ', '.join(fr_detect) if fr_detect else ''
    }

langue_info = df_export['metier_original'].apply(detecter_langue)
df_export['mots_malgache'] = langue_info.apply(lambda x: x['malgache'])
df_export['mots_francais'] = langue_info.apply(lambda x: x['francais'])

df_export.to_csv('metiers_non_matchés.csv', index=False, encoding='utf-8-sig')
print(f"\n✅ Fichier sauvegardé : metiers_non_matchés.csv")

# 10. Afficher des exemples par catégorie
print("\n" + "="*80)
print("EXEMPLES PAR CATÉGORIE")
print("="*80)

# Malgache pur
mg_exemples = [m for m in valeurs_uniques if any(kw in m.lower() for kw in mg_keywords) and not any(kw in m.lower() for kw in fr_keywords)]
print(f"\n📌 Exemples de métiers en malgache pur ({len(mg_exemples)} trouvés) :")
for m in mg_exemples[:15]:
    print(f"  - {m}")

# Français
fr_exemples = [m for m in valeurs_uniques if any(kw in m.lower() for kw in fr_keywords) and not any(kw in m.lower() for kw in mg_keywords)]
print(f"\n📌 Exemples de métiers en français ({len(fr_exemples)} trouvés) :")
for m in fr_exemples[:15]:
    print(f"  - {m}")

# Mixte
mixte_exemples = [m for m in valeurs_uniques if any(kw in m.lower() for kw in mg_keywords) and any(kw in m.lower() for kw in fr_keywords)]
print(f"\n📌 Exemples de métiers mixtes ({len(mixte_exemples)} trouvés) :")
for m in mixte_exemples[:15]:
    print(f"  - {m}")

# 11. Afficher les métiers les plus fréquents non matchés
print("\n" + "="*80)
print("TOP 20 DES MÉTIERS NON MATCHÉS LES PLUS FRÉQUENTS")
print("="*80)
for i, (metier, count) in enumerate(comptage.head(20).items(), 1):
    if pd.notna(metier) and str(metier).strip() != '':
        print(f"{i:>3}. {metier:<50} ({count} occurrences)")

print("\n" + "="*80)
print("✅ EXTRACTION TERMINÉE")
print("="*80)
import pandas as pd
print(f"   (soit {cumul:,} individus sur {total_individus:,})")

# 3. Prendre seulement ces métiers
df_freq = df.head(n_metiers).copy()
print(f"✅ {len(df_freq)} métiers à traduire")

# 4. Ajouter les métiers en français déjà présents (ceux qui sont en français)
fr_keywords = ['agent', 'vendeur', 'maçon', 'chauffeur', 'comptable', 'secretaire', 
               'electricien', 'plombier', 'menuiser', 'ouvrier', 'cadre', 'directeur',
               'responsable', 'technicien', 'chef', 'conseiller', 'assistant']
df_fr = df[df['metier_original'].str.lower().str.contains('|'.join(fr_keywords), na=False)]
df_fr = df_fr[~df_fr['metier_original'].isin(df_freq['metier_original'])]
print(f"✅ {len(df_fr)} métiers en français déjà lisibles")

# 5. Fusionner
df_a_traduire = pd.concat([df_freq, df_fr]).drop_duplicates(subset=['metier_original'])
print(f"✅ Total à traiter : {len(df_a_traduire)} métiers")

# 6. Traduire
translator = Translator()
traductions = []
erreurs = 0

print("\n🔄 Début de la traduction...")

for i, row in tqdm(df_a_traduire.iterrows(), total=len(df_a_traduire), desc="Traduction"):
    metier = row['metier_original']
    try:
        translation = translator.translate(metier, src='mg', dest='fr')
        traductions.append({
            'metier_original': metier,
            'occurrences': row['occurrences'],
            'traduction_fr': translation.text,
            'est_malgache': True
        })
        time.sleep(0.5)
    except Exception as e:
        erreurs += 1
        traductions.append({
            'metier_original': metier,
            'occurrences': row['occurrences'],
            'traduction_fr': f"ERREUR: {str(e)[:30]}",
            'est_malgache': True
        })
        if erreurs <= 5:
            print(f"❌ Erreur sur '{metier}': {str(e)[:50]}")

# 7. Créer le DataFrame
df_traductions = pd.DataFrame(traductions)

# 8. Afficher les résultats
print("\n" + "="*80)
print("EXEMPLES DE TRADUCTION")
print("="*80)
for i in range(min(20, len(df_traductions))):
    row = df_traductions.iloc[i]
    print(f"{i+1:>2}. {row['metier_original']:<30} → {row['traduction_fr']}")

# 9. Sauvegarder
df_traductions.to_csv('traductions_metiers_frequents.csv', index=False, encoding='utf-8-sig')
print(f"\n✅ Sauvegardé : traductions_metiers_frequents.csv")

print(f"\n📊 Statistiques :")
print(f"  - Métiers traduits : {len(df_traductions)}")
print(f"  - Couverture : {df_traductions['occurrences'].sum() / total_individus * 100:.1f}% des individus")
print(f"  - Erreurs : {erreurs}")
import pandas as pd
import numpy as np
import re
from collections import Counter

print("="*80)
print("ÉTAPE 1 : EXTRAIRE LES MÉTIERS NON MATCHÉS")
print("="*80)

# 1. Chargement
df_empl = pd.read_csv('../data/raw/EMPL_complet.csv', low_memory=False)
df_metier = pd.read_csv('../data/raw/metier.csv')
df_final = pd.read_csv('../data/processed/final_ml_ready.csv')

print(f"✅ EMPL_complet : {df_empl.shape[0]} individus")
print(f"✅ metier.csv : {df_metier.shape[0]} métiers")

# 2. Nettoyer les ID et fusionner
df_empl['idHH_clean'] = df_empl['idHH'].astype(str).str.zfill(12)
df_final['idHH_clean'] = df_final['idHH'].astype(str).str.zfill(12)

df_merged = df_final.merge(df_empl[['idHH_clean', 'q4a_18']], on='idHH_clean', how='left')

# 3. Identifier les non matchés (source='global')
df_non_match = df_merged[df_merged['source_salaire'] == 'global'].copy()
print(f"\n📊 Non matchés : {len(df_non_match)} individus")

# 4. Compter les fréquences
freq_metiers = df_non_match['q4a_18'].value_counts()
freq_metiers = freq_metiers[freq_metiers.index.notna()]

print(f"\n📊 {len(freq_metiers)} métiers uniques non matchés")
print(f"\nTop 20 des métiers non matchés :")
for i, (metier, count) in enumerate(freq_metiers.head(20).items(), 1):
    print(f"{i:>2}. {metier:<40} ({count} occurrences)")
print("\n" + "="*80)
print("ÉTAPE 2 : EXTRAIRE LES RACINES (UNIQUEMENT CELLES DEMANDÉES)")
print("="*80)

# Racines demandées
racines_demandees = {
    'amboly': 'Ouvrier agricole',
    'mboly': 'Ouvrier agricole',
    'tsaha': 'Ouvrier agricole',
    'jono': 'Ouvrier agricole',
    'pianatra': 'Enseignant privé',
    'anatran': 'Enseignant privé',
}

print("✅ Racines autorisées :")
for r in racines_demandees:
    print(f"  - {r} → {racines_demandees[r]}")

# Fonction pour vérifier si un métier contient une des racines
def trouver_racine(metier):
    if pd.isna(metier):
        return None
    metier_lower = str(metier).lower()
    for racine in racines_demandees:
        if racine in metier_lower:
            return racine
    return None

# Appliquer
df_non_match['racine'] = df_non_match['q4a_18'].apply(trouver_racine)

n_avec_racine = df_non_match['racine'].notna().sum()
print(f"\n✅ Racines trouvées pour {n_avec_racine} individus ({n_avec_racine/len(df_non_match)*100:.1f}%)")

print("\n📊 Distribution des racines :")
print(df_non_match['racine'].value_counts())

# Voir quelques exemples
print("\n📋 Exemples de métiers avec leurs racines :")
for racine in racines_demandees:
    exemples = df_non_match[df_non_match['racine'] == racine]['q4a_18'].head(5).tolist()
    if exemples:
        print(f"\n  {racine} :")
        for ex in exemples:
            print(f"    - {ex}")
print("\n" + "="*80)
print("ÉTAPE 3 : MATCH AVEC metier.csv")
print("="*80)

# 1. Récupérer les salaires depuis metier.csv
metier_salaire = df_metier.set_index('metier')['salaire_moyen_ariary'].to_dict()

# 2. Mapper les racines vers les métiers de metier.csv
mapping_racine_metier = {
    'amboly': 'Ouvrier agricole',
    'mboly': 'Ouvrier agricole',
    'tsaha': 'Ouvrier agricole',
    'jono': 'Ouvrier agricole',
    'pianatra': 'Enseignant privé',
    'anatran': 'Enseignant privé',
}

# 3. Appliquer le mapping
df_non_match['metier_ref'] = df_non_match['racine'].map(mapping_racine_metier)
df_non_match['salaire_ref'] = df_non_match['metier_ref'].map(metier_salaire)

# 4. Vérifier
print(f"✅ {df_non_match['salaire_ref'].notna().sum()} individus ont un salaire depuis metier.csv")
print(f"\n📊 Salaire moyen par métier :")
print(df_non_match.groupby('metier_ref')['salaire_ref'].mean())
print("\n" + "="*80)
print("ÉTAPE 4 : ANALYSE DES MÉTIERS ENCORE NON MATCHÉS")
print("="*80)

# 1. Identifier les métiers qui n'ont pas encore de match
df_restant = df_non_match[df_non_match['racine'].isna()].copy()
print(f"📊 {len(df_restant)} individus encore non matchés")
print(f"📊 {df_restant['q4a_18'].nunique()} métiers uniques restants")

# 2. Compter les fréquences des métiers restants
freq_restant = df_restant['q4a_18'].value_counts()
freq_restant = freq_restant[freq_restant.index.notna()]

print("\n" + "="*80)
print("TOP 50 MÉTIERS ENCORE NON MATCHÉS")
print("="*80)

for i, (metier, count) in enumerate(freq_restant.head(50).items(), 1):
    print(f"{i:>3}. {metier:<50} ({count:>4} occ.)")

# 3. Statistiques
print("\n" + "="*80)
print("STATISTIQUES DES MÉTIERS RESTANTS")
print("="*80)

print(f"\n  - Individus restants : {len(df_restant):,}")
print(f"  - Métiers uniques restants : {df_restant['q4a_18'].nunique()}")
print(f"  - Top 10 métiers couvrent : {freq_restant.head(10).sum():,} individus ({freq_restant.head(10).sum()/len(df_restant)*100:.1f}%)")
print(f"  - Top 50 métiers couvrent : {freq_restant.head(50).sum():,} individus ({freq_restant.head(50).sum()/len(df_restant)*100:.1f}%)")

# 4. Afficher quelques exemples de métiers restants
print("\n" + "="*80)
print("EXEMPLES DE MÉTIERS RESTANTS (pour identifier de nouvelles racines)")
print("="*80)

print("\n📌 Métiers avec 'varotra' (vente) :")
varotra = [m for m in freq_restant.index if 'varotra' in str(m).lower()]
for m in varotra[:10]:
    print(f"  - {m}")

print("\n📌 Métiers avec 'lamba' (vêtement) :")
lamba = [m for m in freq_restant.index if 'lamba' in str(m).lower()]
for m in lamba[:10]:
    print(f"  - {m}")

print("\n📌 Métiers avec 'chauff' (conducteur) :")
chauff = [m for m in freq_restant.index if 'chauff' in str(m).lower()]
for m in chauff[:10]:
    print(f"  - {m}")

print("\n📌 Métiers avec 'mac' ou 'maçon' :")
mac = [m for m in freq_restant.index if 'mac' in str(m).lower() or 'maçon' in str(m).lower()]
for m in mac[:10]:
    print(f"  - {m}")

print("\n📌 Métiers avec 'gardien' ou 'secur' :")
secur = [m for m in freq_restant.index if 'gardien' in str(m).lower() or 'secur' in str(m).lower()]
for m in secur[:10]:
    print(f"  - {m}")

print("\n📌 Métiers avec 'domestique' ou 'menage' :")
dom = [m for m in freq_restant.index if 'domestique' in str(m).lower() or 'menage' in str(m).lower()]
for m in dom[:10]:
    print(f"  - {m}")
print("\n" + "="*80)
print("ÉTAPE 5 : MATCH AVEC LES NOUVELLES RACINES")
print("="*80)

# 1. Définir les nouvelles racines
nouvelles_racines = {
    'varotra': 'Vendeur',      # tout ce qui contient varotra
    'epicerie': 'Vendeur',     # tout ce qui contient epicerie
    'chauff': 'Chauffeur',     # tout ce qui contient chauff
    'mac': 'Maçon',            # tout ce qui contient mac
    'maçon': 'Maçon',          # tout ce qui contient maçon
    'camion': 'Conducteur de travaux',  # tout ce qui contient camion
}

print("✅ Nouvelles racines autorisées :")
for r in nouvelles_racines:
    print(f"  - {r} → {nouvelles_racines[r]}")

# 2. Appliquer le matching sur les métiers restants
# On travaille sur df_non_match (tous les non matchés)
# Mais on va créer une colonne pour suivre les nouveaux matchs

def trouver_nouvelle_racine(metier):
    if pd.isna(metier):
        return None
    metier_lower = str(metier).lower()
    for racine in nouvelles_racines:
        if racine in metier_lower:
            return racine
    return None

df_non_match['nouvelle_racine'] = df_non_match['q4a_18'].apply(trouver_nouvelle_racine)

# 3. Mapper vers les métiers de metier.csv
df_non_match['nouveau_metier'] = df_non_match['nouvelle_racine'].map(nouvelles_racines)

# 4. Compter
n_nouveau_match = df_non_match['nouveau_metier'].notna().sum()
print(f"\n✅ {n_nouveau_match} nouveaux individus matchés")

# 5. Distribution
print("\n📊 Distribution des nouveaux métiers :")
print(df_non_match['nouveau_metier'].value_counts())

# 6. Récupérer les salaires depuis metier.csv
metier_salaire = df_metier.set_index('metier')['salaire_moyen_ariary'].to_dict()
df_non_match['nouveau_salaire'] = df_non_match['nouveau_metier'].map(metier_salaire)

print("\n📊 Salaires des nouveaux métiers :")
print(df_non_match.groupby('nouveau_metier')['nouveau_salaire'].mean())

# 7. Afficher quelques exemples
print("\n📋 Exemples de nouveaux matchs :")
for racine in nouvelles_racines:
    exemples = df_non_match[df_non_match['nouvelle_racine'] == racine]['q4a_18'].head(5).tolist()
    if exemples:
        print(f"\n  {racine} → {nouvelles_racines[racine]} :")
        for ex in exemples:
            print(f"    - {ex}")
print("\n" + "="*80)
if lamba:
    print(f"\n📌 'lamba' (vêtement) - {len(lamba)} métiers :")
    for m in lamba[:10]:
        print(f"  - {m}")

# Métiers avec 'volamena' (or)
volamena = [m for m in freq_encore.index if 'volamena' in str(m).lower()]
if volamena:
    print(f"\n📌 'volamena' (or) - {len(volamena)} métiers :")
    for m in volamena[:10]:
        print(f"  - {m}")

# Métiers avec 'trano' (maison)
trano = [m for m in freq_encore.index if 'trano' in str(m).lower()]
if trano:
    print(f"\n📌 'trano' (maison/construction) - {len(trano)} métiers :")
    for m in trano[:10]:
        print(f"  - {m}")

# Métiers avec 'omby' ou 'kisoa' ou 'akoho' (élevage)
eleveur = [m for m in freq_encore.index if any(x in str(m).lower() for x in ['omby', 'kisoa', 'akoho', 'ondry'])]
if eleveur:
    print(f"\n📌 Élevage (omby/kisoa/akoho) - {len(eleveur)} métiers :")
    for m in eleveur[:10]:
        print(f"  - {m}")

# Métiers avec 'jardin' ou 'fambolena'
jardin = [m for m in freq_encore.index if any(x in str(m).lower() for x in ['jardin', 'fambolena'])]
if jardin:
    print(f"\n📌 Jardin / Fambolena - {len(jardin)} métiers :")
    for m in jardin[:10]:
        print(f"  - {m}")

# Métiers avec 'comptable' ou 'secretaire'
bureau = [m for m in freq_encore.index if any(x in str(m).lower() for x in ['comptable', 'secretaire', 'secretariat'])]
if bureau:
    print(f"\n📌 Bureau (comptable/secretaire) - {len(bureau)} métiers :")
    for m in bureau[:10]:
        print(f"  - {m}")

# Métiers avec 'infirm' ou 'dokera' ou 'sage'
sante = [m for m in freq_encore.index if any(x in str(m).lower() for x in ['infirm', 'dokera', 'sage', 'pharmac'])]
if sante:
    print(f"\n📌 Santé (infirmier/dokera/sage) - {len(sante)} métiers :")
    for m in sante[:10]:
        print(f"  - {m}")

# 5. Sauvegarder la liste des métiers restants pour référence (dans le notebook)
print("\n" + "="*80)
print("RÉSUMÉ DES MÉTIERS RESTANTS PAR CATÉGORIE")
print("="*80)

print(f"\n  - 'lamba' (vêtement) : {len(lamba)} métiers")
print(f"  - 'volamena' (or) : {len(volamena)} métiers")
print(f"  - 'trano' (construction) : {len(trano)} métiers")
print(f"  - Élevage (omby/kisoa/akoho) : {len(eleveur)} métiers")
print(f"  - Jardin / Fambolena : {len(jardin)} métiers")
print(f"  - Bureau (comptable/secretaire) : {len(bureau)} métiers")
print(f"  - Santé (infirmier/dokera/sage) : {len(sante)} métiers")

print("\n" + "="*80)
print("✅ ANALYSE TERMINÉE")
print("="*80)
print("\n" + "="*80)
        if mot_cle in metier_lower:
            return mot_cle
    return None

# 3. Appliquer sur les métiers encore restants
df_encore_restant['regle_trouvee'] = df_encore_restant['q4a_18'].apply(trouver_regle)
df_encore_restant['nouveau_metier'] = df_encore_restant['regle_trouvee'].map(nouvelles_regles)

n_match = df_encore_restant['nouveau_metier'].notna().sum()
print(f"\n✅ {n_match} nouveaux individus matchés")

# 4. Distribution
print("\n📊 Distribution des nouveaux métiers :")
print(df_encore_restant['nouveau_metier'].value_counts())

# 5. Récupérer les salaires depuis metier.csv
metier_salaire = df_metier.set_index('metier')['salaire_moyen_ariary'].to_dict()
df_encore_restant['nouveau_salaire'] = df_encore_restant['nouveau_metier'].map(metier_salaire)

print("\n📊 Salaires des nouveaux métiers :")
print(df_encore_restant.groupby('nouveau_metier')['nouveau_salaire'].mean())

# 6. Afficher des exemples
print("\n📋 Exemples de nouveaux matchs :")
for regle in ['comptable', 'infirmier', 'omby', 'gargotte']:
    exemples = df_encore_restant[df_encore_restant['regle_trouvee'] == regle]['q4a_18'].head(5).tolist()
    if exemples:
        print(f"\n  {regle} → {nouvelles_regles[regle]} :")
        for ex in exemples:
            print(f"    - {ex}")
print("\n" + "="*80)
for i, (metier, count) in enumerate(freq_restant.head(50).items(), 1):
    print(f"{i:>3}. {metier:<50} ({count:>4} occ.)")

# 4. Exemples pour identifier de nouvelles pistes
print("\n" + "="*80)
print("EXEMPLES PAR CATÉGORIE POUR IDENTIFIER DE NOUVELLES PISTES")
print("="*80)

# Métiers avec 'trano' (construction)
trano = [m for m in freq_restant.index if 'trano' in str(m).lower()]
if trano:
    print(f"\n📌 'trano' (construction) - {len(trano)} métiers :")
    for m in trano[:10]:
        print(f"  - {m}")

# Métiers avec 'volamena' (or)
volamena = [m for m in freq_restant.index if 'volamena' in str(m).lower()]
if volamena:
    print(f"\n📌 'volamena' (or) - {len(volamena)} métiers :")
    for m in volamena[:10]:
        print(f"  - {m}")

# Métiers avec 'lamba' (vêtement)
lamba = [m for m in freq_restant.index if 'lamba' in str(m).lower()]
if lamba:
    print(f"\n📌 'lamba' (vêtement) - {len(lamba)} métiers :")
    for m in lamba[:10]:
        print(f"  - {m}")

# Métiers avec 'mofo' (pain/boulangerie)
mofo = [m for m in freq_restant.index if 'mofo' in str(m).lower()]
if mofo:
    print(f"\n📌 'mofo' (pain/boulangerie) - {len(mofo)} métiers :")
    for m in mofo[:10]:
        print(f"  - {m}")

# Métiers avec 'entana' (marchandise/transport)
entana = [m for m in freq_restant.index if 'entana' in str(m).lower()]
if entana:
    print(f"\n📌 'entana' (marchandise/transport) - {len(entana)} métiers :")
    for m in entana[:10]:
        print(f"  - {m}")

# Métiers avec 'kitay' (bois)
kitay = [m for m in freq_restant.index if 'kitay' in str(m).lower()]
if kitay:
    print(f"\n📌 'kitay' (bois) - {len(kitay)} métiers :")
    for m in kitay[:10]:
        print(f"  - {m}")

# 5. Mise à jour : Gestionnaire → Gestionnaire de crédit
print("\n" + "="*80)
print("MISE À JOUR : Gestionnaire → Gestionnaire de crédit")
print("="*80)

# Vérifier si 'gestionnaire' existe dans les métiers de référence
if 'Gestionnaire de crédit' in metier_salaire:
    print("✅ 'Gestionnaire de crédit' trouvé dans metier.csv")
    
    # Mettre à jour les 'gestionnaire' déjà matchés
    masque_gestionnaire = df_encore_restant['nouveau_metier'] == 'Gestionnaire'
    df_encore_restant.loc[masque_gestionnaire, 'nouveau_metier'] = 'Gestionnaire de crédit'
    df_encore_restant.loc[masque_gestionnaire, 'nouveau_salaire'] = metier_salaire['Gestionnaire de crédit']
    
    n_gestionnaire = masque_gestionnaire.sum()
    print(f"✅ {n_gestionnaire} individus mis à jour vers 'Gestionnaire de crédit'")
else:
    print("❌ 'Gestionnaire de crédit' non trouvé dans metier.csv")

print("\n" + "="*80)
print("✅ BILAN TERMINÉ")
print("="*80)
print("\n" + "="*80)
for i, metier in enumerate(df_tech['q4a_18'].head(20).tolist(), 1):
    print(f"{i:>2}. {metier}")

# 3. Statistiques des métiers technologiques
print("\n📊 Top 10 des métiers technologiques :")
print(df_tech['q4a_18'].value_counts().head(10))

# 4. Ceux qui restent (pour le match avec secteurs généraux)
# On enlève les matchés (armée + technologie)
df_reste_a_traiter = df_final_restant[
    df_final_restant['metier_arme'].isna() & 
    ~df_final_restant['q4a_18'].isin(df_tech['q4a_18'])
].copy()

print("\n" + "="*80)
print("RESTANTS À TRAITER POUR SECTEURS GÉNÉRAUX")
print("="*80)

print(f"📊 {len(df_reste_a_traiter):,} individus restants")
print(f"📊 {df_reste_a_traiter['q4a_18'].nunique()} métiers uniques")

# Afficher les top 30 restants
freq_reste = df_reste_a_traiter['q4a_18'].value_counts()
print("\n📋 Top 30 métiers restants :")
for i, (metier, count) in enumerate(freq_reste.head(30).items(), 1):
    print(f"{i:>2}. {metier:<50} ({count:>4} occ.)")

print("\n" + "="*80)
print("RÉCAPITULATIF")
print("="*80)

print(f"\n  - Matchés (racines initiales) : {n_racines:,}")
print(f"  - Matchés (nouvelles racines) : {n_nouvelles:,}")
print(f"  - Matchés (règles suppl.) : {n_regles:,}")
print(f"  - Matchés (armée/police) : {n_arme:,}")
print(f"  - ⭐ Métiers technologiques identifiés : {len(df_tech):,} (à traiter séparément)")
print(f"  - Restants pour secteurs généraux : {len(df_reste_a_traiter):,}")

print("\n💡 PROCHAINES ÉTAPES :")
print("  1. Traiter les métiers technologiques avec metier.csv (secteur Technologie)")
print("  2. Attribuer aux restants : Salaire minimum non agricole / Salaire minimum agricole / Salaire moyen national estimé")
print("\n" + "="*80)
# On a df_encore_restant avec 'nouveau_metier' pour ceux matchés par règles
masque_regles = df_encore_restant['nouveau_metier'].notna()
for idx in df_encore_restant[masque_regles].index:
    df_final_complet.loc[idx, 'metier_trouve'] = df_encore_restant.loc[idx, 'nouveau_metier']
    df_final_complet.loc[idx, 'salaire_mensuel'] = df_encore_restant.loc[idx, 'nouveau_salaire']
    df_final_complet.loc[idx, 'source_salaire'] = 'mapping_regles_supplementaires'

# Armée/police
masque_arme = df_final_restant['metier_arme'].notna()
for idx in df_final_restant[masque_arme].index:
    df_final_complet.loc[idx, 'metier_trouve'] = df_final_restant.loc[idx, 'metier_arme']
    df_final_complet.loc[idx, 'salaire_mensuel'] = metier_salaire.get('Agent administratif', 400000)
    df_final_complet.loc[idx, 'source_salaire'] = 'mapping_armee_police'

# 2.3 Ajouter les profils technologiques
df_final_complet = pd.concat([df_final_complet, profils_tech], ignore_index=True)

# 2.4 Pour les autres (secteurs généraux) - ceux qui restent
# On va attribuer les salaires généraux
masque_restant = df_final_complet['metier_trouve'].isna()
n_restant = masque_restant.sum()
print(f"\n📊 Individus à attribuer aux secteurs généraux : {n_restant:,}")

# Attribution des salaires généraux (50/30/20)
salaires_generaux = [262680, 266500, 196359]  # Salaire min non agricole, Salaire min agricole, Salaire moyen national
np.random.seed(42)
generaux_attribues = np.random.choice(salaires_generaux, size=n_restant, p=[0.5, 0.3, 0.2])

df_final_complet.loc[masque_restant, 'salaire_mensuel'] = generaux_attribues
df_final_complet.loc[masque_restant, 'metier_trouve'] = 'Secteur général'
df_final_complet.loc[masque_restant, 'source_salaire'] = 'general'

# 2.5 Remplir les valeurs manquantes
df_final_complet['hhmilieu2'] = df_final_complet['hhmilieu2'].fillna(2).astype(int)
df_final_complet['hhreg'] = df_final_complet['hhreg'].fillna(33).astype(int)
df_final_complet['q4a_02'] = df_final_complet['q4a_02'].fillna('Non')
df_final_complet['score_individuel_epm'] = df_final_complet['score_individuel_epm'].fillna(0)

# 2.6 Supprimer les doublons
df_final_complet = df_final_complet.drop_duplicates(subset=['idHH_clean'], keep='first')

print(f"\n✅ Dataset final complet : {df_final_complet.shape}")

# 3. Afficher le DataFrame final
print("\n" + "="*80)
print("APERÇU DU DATASET FINAL")
print("="*80)

print("\n📋 10 premières lignes :")
print(df_final_complet[['idHH_clean', 'salaire_mensuel', 'metier_trouve', 'source_salaire']].head(10))

print("\n📋 10 profils technologiques ajoutés :")
print(df_final_complet[df_final_complet['source_salaire'] == 'technologie'][['idHH_clean', 'salaire_mensuel', 'metier_trouve', 'score_individuel_epm']])

# 4. Statistiques finales
print("\n" + "="*80)
print("STATISTIQUES FINALES")
print("="*80)

print(f"\n📊 Distribution des sources de salaire :")
print(df_final_complet['source_salaire'].value_counts())

print(f"\n📊 Distribution des métiers (top 15) :")
print(df_final_complet['metier_trouve'].value_counts().head(15))

print(f"\n📊 Statistiques des salaires :")
print(df_final_complet['salaire_mensuel'].describe())

print(f"\n📊 Statistiques du score EPM :")
print(df_final_complet['score_individuel_epm'].describe())

# 5. Sauvegarder
output_path = '../data/processed/df_features_score_final.csv'
df_final_complet.to_csv(output_path, index=False)
print(f"\n✅ Fichier sauvegardé : {output_path}")

print("\n" + "="*80)
print("✅ PROCESSUS TERMINÉ")
print("="*80)



3) feature engineering + ml train
====================================================================================================
🔎 AUDIT COMPLET DU DATASET
====================================================================================================

✅ Fichier chargé avec succès
📌 Dimensions : 67,969 lignes × 7 colonnes

====================================================================================================
1️⃣ APERÇU DES DONNÉES
====================================================================================================
idHH_clean	salaire_mensuel	hhmilieu2	hhreg	q4a_02	metier_trouve	score_individuel_epm
0	101	375,000.000	1	33	Non	Chauffeur	54.378
1	101	550,000.000	1	33	Oui	Vendeur	68.200
2	102	500,000.000	1	33	Non	Ouvrier agricole	51.249
3	102	650,000.000	1	33	Non	Ouvrier agricole	43.868
4	102	650,000.000	1	33	Non	Ouvrier agricole	53.868

📋 Noms des colonnes :
  1. idHH_clean
  2. salaire_mensuel
  3. hhmilieu2
  4. hhreg
  5. q4a_02
  6. metier_trouve
  7. score_individuel_epm

====================================================================================================
2️⃣ TYPES DE DONNÉES
====================================================================================================
colonne	type	valeurs_uniques	valeurs_manquantes	%_manquant
0	idHH_clean	int64	16871	0	0.000
1	salaire_mensuel	float64	39	0	0.000
2	hhmilieu2	int64	2	0	0.000
3	hhreg	int64	22	0	0.000
4	q4a_02	str	2	0	0.000
5	metier_trouve	str	62	0	0.000
6	score_individuel_epm	float64	176	0	0.000

====================================================================================================
3️⃣ TAILLE DU DATASET EN MÉMOIRE
====================================================================================================
💾 Mémoire utilisée : 11.40 MB

====================================================================================================
4️⃣ DOUBLONS
====================================================================================================
🔁 Nombre de lignes dupliquées : 25,510
📊 Pourcentage : 37.53 %

====================================================================================================
5️⃣ VALEURS MANQUANTES
====================================================================================================
colonne	manquants	%_manquant	non_manquants
✅ Aucune valeur manquante.

====================================================================================================
6️⃣ STATISTIQUES DES VARIABLES NUMÉRIQUES
====================================================================================================
🔢 Nombre de variables numériques : 5
count	mean	std	min	25%	50%	75%	max
salaire_mensuel	67,969.000	607,034.570	122,242.354	162,000.000	500,000.000	650,000.000	650,000.000	5,400,000.000
idHH_clean	67,969.000	70,570.278	40,572.650	101.000	35,508.000	70,611.000	105,806.000	140,612.000
score_individuel_epm	67,969.000	35.318	17.399	9.923	13.868	36.249	43.868	98.180
hhreg	67,969.000	33.346	17.337	11.000	14.000	32.000	51.000	62.000
hhmilieu2	67,969.000	1.533	0.499	1.000	1.000	2.000	2.000	2.000

====================================================================================================
7️⃣ VARIABLES CATÉGORIELLES
====================================================================================================
🔤 Nombre de variables catégorielles : 2

--------------------------------------------------------------------------------
📌 q4a_02
--------------------------------------------------------------------------------
Nombre de catégories : 2
C:\Users\Dell\AppData\Local\Temp\ipykernel_17996\1738953729.py:154: Pandas4Warning: For backward compatibility, 'str' dtypes are included by select_dtypes when 'object' dtype is specified. This behavior is deprecated and will be removed in a future version. Explicitly pass 'str' to `include` to select them, or to `exclude` to remove them and silence this warning.
See https://pandas.pydata.org/docs/user_guide/migration-3-strings.html#string-migration-select-dtypes for details on how to write code that works with pandas 2 and 3.
  categorical_cols = df.select_dtypes(
effectif
q4a_02	
Non	55057
Oui	12912

--------------------------------------------------------------------------------
📌 metier_trouve
--------------------------------------------------------------------------------
Nombre de catégories : 62
effectif
metier_trouve	
Ouvrier agricole	55667
Vendeur	3546
Ingénieur production	2718
Chauffeur	1173
Enseignant privé	905
Mécanicien	884
Serveur	883
Secrétaire	514
Maçon	371
Infirmier	205
Journaliste	102
Comptable	74
Responsable sécurité	74
Gestionnaire de crédit	68
Électricien bâtiment	59
Agent de sécurité confirmé	58
Maine d'oeuvre	57
Aide-cuisinier	50
Responsable logistique	49
Agent administratif	43

====================================================================================================
8️⃣ VARIABLES CONSTANTES OU QUASI CONSTANTES
====================================================================================================

🔴 Variables constantes :
   Aucune.

🟠 Variables quasi constantes (>95 % même valeur) :
   Aucune.

====================================================================================================
9️⃣ ANALYSE DE LA VARIABLE CIBLE
====================================================================================================
🎯 Cible : score_individuel_epm

Nombre total : 67,969
Nombre manquant : 0
Nombre non manquant : 67,969
Nombre de valeurs uniques : 176

📊 Statistiques :
count	mean	std	min	25%	50%	75%	max
score_individuel_epm	67,969.000	35.318	17.399	9.923	13.868	36.249	43.868	98.180

📌 Quantiles :
score
0.000	9.923
0.010	11.249
0.050	13.868
0.100	13.868
0.250	13.868
0.500	36.249
0.750	43.868
0.900	58.200
0.950	65.627
0.990	71.545
1.000	98.180

📌 Valeurs les plus fréquentes :
effectif
score_individuel_epm	
13.868	16122
43.868	15918
23.868	6015
53.868	4746
31.249	4092
21.249	2212
33.868	1705
68.200	1558
11.249	1473
61.249	1280
51.249	916
46.249	841
38.200	814
58.200	625
63.868	603
56.737	600
36.249	586
41.249	486
76.249	486
66.249	476

⚠️ Scores hors [0,100] : 0

C:\Users\Dell\AppData\Local\Temp\ipykernel_17996\1738953729.py:279: MatplotlibDeprecationWarning: vert: bool was deprecated in Matplotlib 3.11 and will be removed in 3.13. Use orientation: {'vertical', 'horizontal'} instead.
  plt.boxplot(y.dropna(), vert=False)


====================================================================================================
🔟 DÉTECTION DES VALEURS ABERRANTES
====================================================================================================
colonne	Q1	Q3	IQR	outliers	%_outliers
1	salaire_mensuel	500,000.000	650,000.000	150,000.000	532	0.783
0	idHH_clean	35,508.000	105,806.000	70,298.000	0	0.000
2	hhmilieu2	1.000	2.000	1.000	0	0.000
3	hhreg	14.000	51.000	37.000	0	0.000

====================================================================================================
1️⃣1️⃣ CORRÉLATIONS AVEC LE SCORE
====================================================================================================
corrélation_avec_score
hhmilieu2	-0.856
hhreg	0.115
salaire_mensuel	-0.047
idHH_clean	-0.005


====================================================================================================
1️⃣2️⃣ RELATION ENTRE VARIABLES NUMÉRIQUES ET SCORE
====================================================================================================





====================================================================================================
1️⃣3️⃣ SCORE MOYEN PAR CATÉGORIE
====================================================================================================

--------------------------------------------------------------------------------
📌 q4a_02
--------------------------------------------------------------------------------
effectif	moyenne	mediane	ecart_type
q4a_02				
Oui	12912	46.879	38.200	16.322
Non	55057	32.606	31.623	16.508

⏭️ metier_trouve ignorée : 62 catégories.

====================================================================================================
1️⃣4️⃣ ANALYSE SPÉCIFIQUE : SALAIRE → SCORE
====================================================================================================
💰 Colonnes potentiellement liées au salaire :
   - salaire_mensuel

📊 Analyse : salaire_mensuel
Corrélation salaire/score : -0.0469


====================================================================================================
1️⃣5️⃣ MATRICE DE CORRÉLATION
====================================================================================================
idHH_clean	salaire_mensuel	hhmilieu2	hhreg	score_individuel_epm
idHH_clean	1.000	0.004	0.005	0.013	-0.005
salaire_mensuel	0.004	1.000	-0.041	0.015	-0.047
hhmilieu2	0.005	-0.041	1.000	-0.145	-0.856
hhreg	0.013	0.015	-0.145	1.000	0.115
score_individuel_epm	-0.005	-0.047	-0.856	0.115	1.000


====================================================================================================
1️⃣6️⃣ FEATURES TRÈS CORRÉLÉES ENTRE ELLES
====================================================================================================
feature_1	feature_2	corrélation_abs
0	hhmilieu2	score_individuel_epm	0.856

====================================================================================================
1️⃣7️⃣ RECHERCHE DE FEATURES SUSPECTES / DATA LEAKAGE
====================================================================================================

⚠️ Colonnes potentiellement suspectes :
   Aucune détectée automatiquement.

⚠️ ATTENTION : cette liste n'est PAS une preuve de leakage.
Elle sert seulement à identifier les colonnes à examiner manuellement.

====================================================================================================
1️⃣8️⃣ CATÉGORIES RARES
====================================================================================================

📌 q4a_02
   Catégories avec ≤ 1 observation  : 0
   Catégories avec ≤ 5 observations : 0
   Catégories avec ≤ 10 observations: 0

📌 metier_trouve
   Catégories avec ≤ 1 observation  : 7
   Catégories avec ≤ 5 observations : 19
   Catégories avec ≤ 10 observations: 28

====================================================================================================
1️⃣9️⃣ RÉPARTITION DU SCORE
====================================================================================================
effectif	%
score_individuel_epm		
<10	3	0.004
10-20	17845	26.255
20-30	9592	14.112
30-40	7706	11.338
40-50	17782	26.162
50-60	8674	12.762
60-70	5256	7.733
70-80	1064	1.565
80-90	46	0.068
90-100	1	0.001
>100	0	0.000

====================================================================================================
2️⃣0️⃣ RÉSUMÉ AUTOMATIQUE
====================================================================================================

📦 DATASET
   Lignes              : 67,969
   Colonnes            : 7
   Variables numériques: 5
   Variables catégorielles: 2

🧹 QUALITÉ
   Valeurs manquantes  : 0
   Lignes dupliquées   : 25,510
   Variables constantes: 0

🎯 CIBLE
   Cible               : score_individuel_epm

   Valeurs manquantes  : 0
   Valeurs uniques     : 176
   Moyenne             : 35.318
   Médiane             : 36.249
   Minimum             : 9.923
   Maximum             : 98.180

====================================================================================================
✅ AUDIT TERMINÉ
====================================================================================================
# ============================================================


# ============================================================
# 14. RÉCUPÉRATION DES FEATURES APRÈS ENCODAGE
# ============================================================

fitted_preprocessor = best_model.named_steps['preprocessing']

feature_names = list(
    fitted_preprocessor.get_feature_names_out()
)


# ============================================================
# 15. MÉTADONNÉES
# ============================================================

metadata = {
    'feature_names': feature_names,
    'original_features': FEATURES,
    'target': TARGET,
    'group_column': GROUP,
    'model_name': best_model_name,
    'n_observations': int(len(df)),
    'n_features_after_encoding': len(feature_names),
    'metrics': {
        'MAE': float(results_df.iloc[0]['MAE']),
        'RMSE': float(results_df.iloc[0]['RMSE']),
        'R2': float(results_df.iloc[0]['R²'])
    }
}


METADATA_PATH = os.path.join(
    MODELS_DIR,
    'model_metadata.json'
)

with open(
    METADATA_PATH,
    'w',
    encoding='utf-8'
) as f:

    json.dump(
        metadata,
        f,
        ensure_ascii=False,
        indent=2
    )


print(f"📄 Metadata sauvegardées : {METADATA_PATH}")
print(f"📊 Features encodées : {len(feature_names)}")


# ============================================================
# 16. TEST RAPIDE DU MODÈLE
# ============================================================

print("\n" + "=" * 80)
print("🧪 TEST RAPIDE")
print("=" * 80)

sample = X_test.iloc[[0]]

real_score = float(y_test.iloc[0])
predicted_score = float(best_model.predict(sample)[0])

print("\nDonnées :")
display(sample)

print(f"Score réel      : {real_score:.3f}")
print(f"Score prédit    : {predicted_score:.3f}")
print(
    f"Erreur absolue  : {abs(real_score - predicted_score):.3f}"
)

print("\n" + "=" * 80)
print("✅ ENTRAÎNEMENT TERMINÉ")
print("=" * 80)
================================================================================
🚀 ENTRAÎNEMENT DU MODÈLE DE SCORE INDIVIDUEL
================================================================================

📊 Dataset : 67,969 lignes × 7 colonnes

📌 Variables utilisées :
   - salaire_mensuel
   - hhmilieu2
   - hhreg
   - q4a_02
   - metier_trouve

🎯 Variable cible : score_individuel_epm
👥 Variable de groupe : idHH_clean

================================================================================
🔍 VÉRIFICATION
================================================================================

Valeurs manquantes dans X : 0
Valeurs manquantes dans y : 0
Nombre d'observations : 67,969
Nombre de ménages      : 16,871

================================================================================
✂️ SÉPARATION TRAIN / VALIDATION
================================================================================

Train      : 54,458 lignes
Validation : 13,511 lignes
Ménages train      : 13,496
Ménages validation : 3,375
Ménages présents dans les deux : 0
✅ Aucun ménage partagé entre train et validation.

--------------------------------------------------------------------------------
🤖 Linear Regression
--------------------------------------------------------------------------------
C:\Memoire2\Memoire2\ml\.venv\Lib\site-packages\sklearn\preprocessing\_encoders.py:262: UserWarning: Found unknown categories in columns [1] during transform. These unknown categories will be encoded as all zeros
  warnings.warn(msg, UserWarning)
MAE  : 3.5259
RMSE : 4.0883
R²   : 0.9451
Temps : 2.04 sec

--------------------------------------------------------------------------------
🤖 Random Forest
--------------------------------------------------------------------------------
C:\Memoire2\Memoire2\ml\.venv\Lib\site-packages\sklearn\preprocessing\_encoders.py:262: UserWarning: Found unknown categories in columns [1] during transform. These unknown categories will be encoded as all zeros
  warnings.warn(msg, UserWarning)
MAE  : 2.7946
RMSE : 3.7671
R²   : 0.9534
Temps : 74.50 sec

--------------------------------------------------------------------------------
🤖 XGBoost
--------------------------------------------------------------------------------
C:\Memoire2\Memoire2\ml\.venv\Lib\site-packages\sklearn\preprocessing\_encoders.py:262: UserWarning: Found unknown categories in columns [1] during transform. These unknown categories will be encoded as all zeros
  warnings.warn(msg, UserWarning)
MAE  : 2.8236
RMSE : 3.7641
R²   : 0.9535
Temps : 34.64 sec

================================================================================
🏆 COMPARAISON DES MODÈLES
================================================================================
modèle	MAE	RMSE	R²	temps_entraînement_sec
0	XGBoost	2.824	3.764	0.953	34.639
1	Random Forest	2.795	3.767	0.953	74.498
2	Linear Regression	3.526	4.088	0.945	2.041

================================================================================
🏆 MEILLEUR MODÈLE
================================================================================

🥇 XGBoost
MAE  : 2.8236
RMSE : 3.7641
R²   : 0.9535

💾 Modèle sauvegardé : ../models\score_individuel_model.pkl
📄 Metadata sauvegardées : ../models\model_metadata.json
📊 Features encodées : 64

================================================================================
🧪 TEST RAPIDE
================================================================================

Données :
salaire_mensuel	hhmilieu2	hhreg	q4a_02	metier_trouve
0	375,000.000	1	33	Non	Chauffeur
Score réel      : 54.378
Score prédit    : 54.435
Erreur absolue  : 0.057

================================================================================
✅ ENTRAÎNEMENT TERMINÉ
================================================================================
# ============================================================
    )

    print("\nImportance regroupée par variable originale :")

    display(
        importance_original_df.style.format({
            'importance': '{:.4f}'
        })
    )


# ============================================================
# 15. EXEMPLES CONCRETS DE PRÉDICTION
# ============================================================

examples = pd.DataFrame({
    'score_reel': y_test.iloc[:20].values,
    'score_predit': best_predictions[:20]
})

examples['erreur'] = (
    examples['score_reel']
    - examples['score_predit']
)

examples['erreur_absolue'] = (
    examples['erreur'].abs()
)

print("\n" + "=" * 90)
print("🧪 EXEMPLES DE PRÉDICTIONS")
print("=" * 90)

display(
    examples.style.format({
        'score_reel': '{:.2f}',
        'score_predit': '{:.2f}',
        'erreur': '{:.2f}',
        'erreur_absolue': '{:.2f}'
    })
)


# ============================================================
# 16. RÉSUMÉ AUTOMATIQUE
# ============================================================

best_mae = evaluation_df.iloc[0]['MAE']
best_rmse = evaluation_df.iloc[0]['RMSE']
best_r2 = evaluation_df.iloc[0]['R²']

print("\n" + "=" * 90)
print("📝 RÉSUMÉ AUTOMATIQUE")
print("=" * 90)

print(f"""
Modèle retenu provisoirement : {best_model_name}

Nombre d'observations de validation : {len(y_test):,}

MAE  : {best_mae:.4f}
RMSE : {best_rmse:.4f}
R²   : {best_r2:.4f}

Erreur moyenne absolue :
→ environ {best_mae:.2f} points de score.

Erreur ≤ 2 points :
→ {evaluation_df.iloc[0]['Erreur ≤ 2 points (%)']:.2f}% des observations.

Erreur ≤ 5 points :
→ {evaluation_df.iloc[0]['Erreur ≤ 5 points (%)']:.2f}% des observations.

Erreur ≤ 10 points :
→ {evaluation_df.iloc[0]['Erreur ≤ 10 points (%)']:.2f}% des observations.
""")

print("=" * 90)
print("✅ ANALYSE TERMINÉE")
print("=" * 90)
==========================================================================================
📊 ANALYSE COMPLÈTE DES MODÈLES
==========================================================================================
✅ Prédictions calculées : Linear Regression
C:\Memoire2\Memoire2\ml\.venv\Lib\site-packages\sklearn\preprocessing\_encoders.py:262: UserWarning: Found unknown categories in columns [1] during transform. These unknown categories will be encoded as all zeros
  warnings.warn(msg, UserWarning)
C:\Memoire2\Memoire2\ml\.venv\Lib\site-packages\sklearn\preprocessing\_encoders.py:262: UserWarning: Found unknown categories in columns [1] during transform. These unknown categories will be encoded as all zeros
  warnings.warn(msg, UserWarning)
✅ Prédictions calculées : Random Forest
C:\Memoire2\Memoire2\ml\.venv\Lib\site-packages\sklearn\preprocessing\_encoders.py:262: UserWarning: Found unknown categories in columns [1] during transform. These unknown categories will be encoded as all zeros
  warnings.warn(msg, UserWarning)
✅ Prédictions calculées : XGBoost

==========================================================================================
🏆 TABLEAU COMPARATIF COMPLET
==========================================================================================
 	Modèle	MAE	RMSE	R²	Erreur médiane	Erreur max	Erreur ≤ 1 point (%)	Erreur ≤ 2 points (%)	Erreur ≤ 5 points (%)	Erreur ≤ 10 points (%)
0	XGBoost	2.824	3.764	0.9535	2.384	10.055	26.72	31.46	80.43	99.99
1	Random Forest	2.795	3.767	0.9534	2.375	10.013	27.10	31.34	80.50	99.97
2	Linear Regression	3.526	4.088	0.9451	3.039	15.365	11.07	18.84	77.40	99.44

==========================================================================================
🥇 MEILLEUR MODÈLE
==========================================================================================

Modèle : XGBoost
MAE    : 2.8236
RMSE   : 3.7641
R²     : 0.9535






==========================================================================================
📊 ERREUR PAR TRANCHE DE SCORE
==========================================================================================
 	tranche_score	observations	MAE	erreur_mediane	erreur_max
0	0–10	0	nan	nan	nan
1	10–20	3469	2.884	2.691	10.055
2	20–30	1843	5.539	7.121	9.795
3	30–40	1514	0.302	0.066	9.695
4	40–50	3581	2.311	2.291	10.049
5	50–60	1800	4.888	7.509	9.869
6	60–70	1070	0.330	0.058	6.061
7	70–80	223	0.155	0.081	1.834
8	80–90	11	1.715	0.349	7.052
9	90–100	0	nan	nan	nan



==========================================================================================
📌 PERFORMANCE PAR CLASSE DE SCORE
==========================================================================================
 	classe_score	observations	MAE	biais_moyen
0	Faible (0–25)	5131	3.876	-0.047
1	Moyen (25–50)	5276	1.716	-1.507
2	Élevé (50–75)	2975	3.082	2.789
3	Très élevé (75–100)	129	0.277	0.130

==========================================================================================
⚖️ ANALYSE DU BIAIS
==========================================================================================

Résidu moyen : 0.0089
✅ Très faible biais global.

==========================================================================================
🧠 IMPORTANCE DES VARIABLES
==========================================================================================
 	feature	importance
62	num__hhmilieu2	0.6793
44	cat__metier_trouve_Ouvrier agricole	0.1485
0	cat__q4a_02_Oui	0.1009
35	cat__metier_trouve_Ingénieur production	0.0172
61	num__salaire_mensuel	0.0063
25	cat__metier_trouve_Directeur administratif	0.0050
20	cat__metier_trouve_Comptable	0.0049
55	cat__metier_trouve_Secrétaire	0.0042
28	cat__metier_trouve_Enseignant privé	0.0036
59	cat__metier_trouve_Vendeur	0.0036
37	cat__metier_trouve_Journaliste	0.0029
52	cat__metier_trouve_Responsable sécurité	0.0028
63	num__hhreg	0.0026
51	cat__metier_trouve_Responsable logistique	0.0022
10	cat__metier_trouve_Chauffeur	0.0022
41	cat__metier_trouve_Menuisier	0.0020
40	cat__metier_trouve_Maçon	0.0017
22	cat__metier_trouve_Couturier	0.0012
42	cat__metier_trouve_Mécanicien	0.0011
56	cat__metier_trouve_Serveur	0.0009


Importance regroupée par variable originale :
 	variable	importance
0	hhmilieu2	0.6793
1	metier_trouve	0.2109
2	q4a_02	0.1009
3	salaire_mensuel	0.0063
4	hhreg	0.0026

==========================================================================================
🧪 EXEMPLES DE PRÉDICTIONS
==========================================================================================
 	score_reel	score_predit	erreur	erreur_absolue
0	54.38	54.43	-0.06	0.06
1	68.20	68.18	0.02	0.02
2	54.24	53.95	0.29	0.29
3	51.25	49.95	1.30	1.30
4	43.87	46.35	-2.48	2.48
5	43.87	46.35	-2.48	2.48
6	58.20	56.05	2.15	2.15
7	53.87	46.35	7.52	7.52
8	41.25	49.95	-8.70	8.70
9	43.87	46.35	-2.48	2.48
10	43.87	46.35	-2.48	2.48
11	43.87	46.35	-2.48	2.48
12	54.38	54.25	0.13	0.13
13	43.87	46.17	-2.30	2.30
14	43.87	46.17	-2.30	2.30
15	43.87	46.17	-2.30	2.30
16	53.87	46.17	7.70	7.70
17	53.87	46.17	7.70	7.70
18	58.20	55.64	2.56	2.56
19	68.20	68.24	-0.04	0.04

==========================================================================================
📝 RÉSUMÉ AUTOMATIQUE
==========================================================================================

Modèle retenu provisoirement : XGBoost

Nombre d'observations de validation : 13,511

MAE  : 2.8236
RMSE : 3.7641
R²   : 0.9535

Erreur moyenne absolue :
→ environ 2.82 points de score.

Erreur ≤ 2 points :
→ 31.46% des observations.

Erreur ≤ 5 points :
→ 80.43% des observations.

Erreur ≤ 10 points :
→ 99.99% des observations.

==========================================================================================
✅ ANALYSE TERMINÉE
==========================================================================================

