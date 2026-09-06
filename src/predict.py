# C:\Memoire2\Memoire2\ml\src\predict.py
import json
import os
import sys
import traceback
import joblib
import pandas as pd


def get_valid_model_path(candidate_paths):
    """Retourne le premier chemin de modèle existant qui n'est PAS vide (> 0 octets)."""
    for path in candidate_paths:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            return path
    return None


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

        data = json.loads(raw_input)

        # 2. Localisation des répertoires
        src_dir = os.path.dirname(os.path.abspath(__file__))
        ml_dir = os.path.abspath(os.path.join(src_dir, '..'))
        root_dir = os.path.abspath(os.path.join(ml_dir, '..'))

        # Liste ordonnée des modèles (en priorité ton modèle valide de 256 Ko)
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

        # Filtre sur les fichiers non vides
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

        # 3. Chargement du modèle XGBoost (256 Ko)
        model = joblib.load(model_path)

        # 4. Chargement des colonnes d'entraînement depuis model_metadata.json
        expected_features = []
        for meta_path in candidate_metadata:
            if os.path.exists(meta_path) and os.path.getsize(meta_path) > 0:
                with open(meta_path, 'r', encoding='utf-8') as f:
                    meta = json.load(f)
                    expected_features = meta.get('feature_names', [])
                break

        if not expected_features and hasattr(model, 'feature_names_in_'):
            expected_features = list(model.feature_names_in_)

        # 5. Transformation et réalignement des données reçues
        df_single = pd.DataFrame([data])
        df_encoded = pd.get_dummies(df_single)

        if expected_features:
            df_aligned = pd.DataFrame(0, index=[0], columns=expected_features)
            for col in df_encoded.columns:
                if col in df_aligned.columns:
                    df_aligned[col] = df_encoded[col].values
        else:
            df_aligned = df_encoded

        # 6. Prédiction
        predicted_score = float(model.predict(df_aligned)[0])
        score_clamped = round(max(0.0, min(100.0, predicted_score)), 2)

        print(json.dumps({'score_individuel_epm': score_clamped}))

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