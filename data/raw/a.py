# visualiser_epm_light.py
import pandas as pd
import os

print("1 - Démarrage du script")

dossier_actuel = os.getcwd()
print(f"2 - Dossier actuel: {dossier_actuel}")

# Liste des fichiers
fichiers = [
    '21_MDG_EPM2122_IMPO.dta',
]

for fichier in fichiers:
    print(f"\n3 - Traitement de: {fichier}")
    
    if not os.path.exists(fichier):
        print(f"   ❌ Fichier non trouvé")
        continue
    
    print(f"   ✅ Fichier trouvé")
    
    # Taille du fichier
    taille = os.path.getsize(fichier) / (1024 * 1024)
    print(f"   📦 Taille: {taille:.1f} Mo")
    
    try:
        print(f"   🔄 Chargement des 5 premières lignes...")
        
        if fichier.endswith('.dta'):
            df = pd.read_stata(fichier, iterator=True)
            lignes = []
            for i, chunk in enumerate(df):
                lignes.append(chunk)
                if i >= 0:  # juste le premier chunk
                    break
            df = pd.concat(lignes)
            
        elif fichier.endswith('.sav'):
            # Pour les fichiers .sav, on charge tout (pas d'itérateur)
            try:
                import pyreadstat
                df, _ = pyreadstat.read_sav(fichier)
            except ImportError:
                print(f"   ⚠️ Installer pyreadstat: pip install pyreadstat")
                continue
            df = df.head(5)  # on garde juste 5 lignes
        
        print(f"   ✅ Chargé: {len(df)} lignes (aperçu)")
        print(f"   📋 Colonnes: {list(df.columns)[:10]}")
        print(f"\n   📊 Aperçu:")
        print(df.head(3).to_string())
        
        # Libérer
        del df
        
    except Exception as e:
        print(f"   ⚠️ Erreur: {e}")

print("\n✅ Terminé")