# C:\Memoire2\Memoire2\ml\src\predict.py
import json
import os
import sys
import traceback
import joblib
import pandas as pd
import numpy as np


def get_valid_model_path(candidate_paths):
    """Retourne le premier chemin de modèle existant qui n'est PAS vide (> 0 octets)."""
    for path in candidate_paths:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            return path
    return None


def get_expected_features(metadata_paths):
    """
    Récupère les noms des features attendus depuis le fichier metadata.
    Retourne également les features originales pour la validation.
    """
    for meta_path in metadata_paths:
        if os.path.exists(meta_path) and os.path.getsize(meta_path) > 0:
            try:
                with open(meta_path, 'r', encoding='utf-8') as f:
                    meta = json.load(f)
                    return {
                        'feature_names': meta.get('feature_names', []),
                        'original_features': meta.get('original_features', []),
                        'target': meta.get('target', 'score_individuel_epm'),
                        'model_name': meta.get('model_name', 'Unknown')
                    }
            except Exception:
                continue
    return {
        'feature_names': [],
        'original_features': [],
        'target': 'score_individuel_epm',
        'model_name': 'Unknown'
    }


def restore_column_transformer_compatibility(pipeline):
    """Restaure un attribut absent lors du chargement avec scikit-learn 1.3."""
    for step in getattr(pipeline, 'named_steps', {}).values():
        if hasattr(step, 'transformers_') and not hasattr(
            step,
            '_name_to_fitted_passthrough'
        ):
            step._name_to_fitted_passthrough = {}


REGION_CODES = {
    'analamanga': 11,
    'vakinankaratra': 12,
    'vakinakaratra': 12,
    'itasy': 13,
    'bongolava': 14,
    'matsiatra ambony': 21,
    'haute matsiatra': 21,
    'amoron i mania': 22,
    'vatovavy': 23,
    'ihorombe': 24,
    'atsimo ats inanana': 25,
    'atsimo atsinanana': 25,
    'fitovinany': 26,
    'atsinanana': 31,
    'analanjirofo': 32,
    'alaotra mangoro': 33,
    'boeny': 41,
    'sofia': 42,
    'betsiboka': 43,
    'melaky': 44,
    'atsimo andrefana': 51,
    'androy': 52,
    'anosy': 53,
    'menabe': 54,
    'diana': 61,
    'sava': 62,
}


def normalize_location_features(data):
    """Convertit les libellés de localisation de l'interface en codes EPM."""
    normalized = dict(data)

    milieu = str(normalized.get('hhmilieu2', '')).strip().lower()
    if milieu in ('urbain', 'urbaine', 'urban'):
        normalized['hhmilieu2'] = 1
    elif milieu in ('rural', 'rurale'):
        normalized['hhmilieu2'] = 2
    else:
        normalized['hhmilieu2'] = pd.to_numeric(
            normalized.get('hhmilieu2'),
            errors='coerce'
        )

    region = str(normalized.get('hhreg', '')).strip().lower()
    if region in REGION_CODES:
        normalized['hhreg'] = REGION_CODES[region]
    else:
        normalized['hhreg'] = pd.to_numeric(
            normalized.get('hhreg'),
            errors='coerce'
        )

    return normalized


def prepare_features_for_prediction(data, original_features):
    """
    Prépare les données d'entrée au format attendu par le modèle.
    """
    # Créer un DataFrame avec une seule ligne
    df_input = pd.DataFrame([data])
    
    # Vérifier que toutes les features originales sont présentes
    missing_features = [f for f in original_features if f not in df_input.columns]
    if missing_features:
        raise ValueError(
            f"Variables manquantes dans les données d'entrée : {missing_features}"
        )
    
    # Ne garder que les colonnes nécessaires dans le bon ordre
    df_prepared = df_input[original_features].copy()
    
    # Gérer les valeurs manquantes (remplacer par 0 pour les numériques, 'Unknown' pour les catégorielles)
    for col in df_prepared.columns:
        if df_prepared[col].dtype in ['float64', 'int64']:
            df_prepared[col] = df_prepared[col].fillna(0)
        else:
            df_prepared[col] = df_prepared[col].fillna('Unknown')
    
    return df_prepared


def main():
    try:
        # 1. Lecture de la saisie utilisateur
        if len(sys.argv) >= 2:
            raw_input = sys.argv[1]
        else:
            raw_input = sys.stdin.read()

        if not raw_input.strip():
            print(
                json.dumps({
                    'error': 'Aucune donnée JSON reçue.'
                })
            )
            sys.exit(1)

        data = normalize_location_features(json.loads(raw_input))

        # 2. Localisation des répertoires
        src_dir = os.path.dirname(os.path.abspath(__file__))
        ml_dir = os.path.abspath(os.path.join(src_dir, '..'))
        root_dir = os.path.abspath(os.path.join(ml_dir, '..'))

        # Liste ordonnée des modèles
        candidate_models = [
            os.path.join(ml_dir, 'models', 'score_individuel_model.pkl'),
            os.path.join(root_dir, 'models', 'score_individuel_model.pkl'),
            os.path.join(ml_dir, 'models', 'score_individuel_epm.pkl'),
            os.path.join(root_dir, 'models', 'score_individuel_epm.pkl'),
            os.path.join(ml_dir, 'models', 'final_model.pkl'),
            os.path.join(root_dir, 'models', 'final_model.pkl'),
        ]

        candidate_metadata = [
            os.path.join(ml_dir, 'models', 'model_metadata.json'),
            os.path.join(root_dir, 'models', 'model_metadata.json'),
        ]

        # 3. Chargement des métadonnées
        metadata = get_expected_features(candidate_metadata)
        original_features = metadata.get('original_features', [])
        target = metadata.get('target', 'score_individuel_epm')

        # 4. Trouver et charger le modèle
        model_path = get_valid_model_path(candidate_models)

        if not model_path:
            print(
                json.dumps({
                    'error': (
                        'Aucun fichier .pkl valide (> 0 octets) trouvé dans'
                        ' models/'
                    )
                })
            )
            sys.exit(1)

        # Chargement du pipeline complet (prétraitement + modèle)
        pipeline = joblib.load(model_path)
        restore_column_transformer_compatibility(pipeline)

        print(
            f"✅ Modèle chargé : {model_path}",
            file=sys.stderr
        )
        print(
            f"📊 Modèle nom : {metadata.get('model_name', 'Unknown')}",
            file=sys.stderr
        )

        # 5. Vérifier que le modèle est un pipeline
        if not hasattr(pipeline, 'named_steps'):
            print(
                json.dumps({
                    'error': (
                        'Le fichier chargé n\'est pas un pipeline sklearn.'
                        ' Vérifiez que vous utilisez le bon modèle.'
                    )
                }),
                file=sys.stderr
            )
            sys.exit(1)

        # 6. Préparation des données
        if original_features:
            # Utiliser les features originales pour préparer les données
            df_prepared = prepare_features_for_prediction(data, original_features)
            print(
                f"📋 Features originales : {original_features}",
                file=sys.stderr
            )
        else:
            # Fallback : utiliser toutes les colonnes disponibles
            df_prepared = pd.DataFrame([data])
            # Remplacer les valeurs manquantes par 0
            df_prepared = df_prepared.fillna(0)
            print(
                "⚠️ Aucune feature originale trouvée, utilisation de toutes les colonnes",
                file=sys.stderr
            )

        # 7. Vérification des données
        print(
            f"📊 Données d'entrée : {df_prepared.shape[1]} colonnes",
            file=sys.stderr
        )
        print(
            f"🔍 Colonnes : {list(df_prepared.columns)}",
            file=sys.stderr
        )

        # 8. Prédiction avec le pipeline
        try:
            predicted_score = float(pipeline.predict(df_prepared)[0])
        except Exception as e:
            print(
                json.dumps({
                    'error': (
                        f"Erreur lors de la prédiction : {str(e)}. "
                        f"Vérifiez que les données sont correctement formatées."
                    ),
                    'traceback': traceback.format_exc(),
                }),
                file=sys.stderr
            )
            sys.exit(1)

        # 9. Arrondir le score entre 0 et 100
        score_clamped = round(max(0.0, min(100.0, predicted_score)), 2)

        # 10. Retourner le résultat
        result = {target: score_clamped}
        print(json.dumps(result))

    except json.JSONDecodeError as e:
        print(
            json.dumps({
                'error': f'Erreur de parsing JSON : {str(e)}',
                'traceback': traceback.format_exc(),
            })
        )
        sys.exit(1)

    except ValueError as e:
        print(
            json.dumps({
                'error': str(e),
                'traceback': traceback.format_exc(),
            })
        )
        sys.exit(1)

    except Exception as e:
        print(
            json.dumps({
                'error': str(e) if str(e) else type(e).__name__,
                'traceback': traceback.format_exc(),
            })
        )
        sys.exit(1)


if __name__ == '__main__':
    main()