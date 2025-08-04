# FamilySearch Addon

**FamilySearch Addon** est un projet expérimental pour extraire des informations généalogiques à partir de documents d'état civil.

## 🎯 Objectifs et fonctionnalités prévues

- **📤 Téléversement d’images** : Permettre aux utilisateurs d'envoyer des scans d’actes de naissance, mariage et décès.
- **🧠 Extraction IA/OCR** : Extraire les données textuelles via OCR et modèles linguistiques.
- **📄 Export GEDCOM** : Convertir les données extraites vers le format [GEDCOM](https://en.wikipedia.org/wiki/GEDCOM).
- **🔗 Intégration FamilySearch** : Transmettre les individus et relations extraits vers FamilySearch.

## ⚙️ Prérequis

- Python 3.10 ou plus récent
- Dépendances listées dans `requirements.txt` :
  - `FastAPI`
  - `Uvicorn`
  - `Streamlit`
  - `Ollama`
  - `python-gedcom`

Installation rapide :
```bash
pip install -r requirements.txt
```

## 🚀 Lancer l'application

1. Démarrer l'API FastAPI :
   ```bash
   python backend/main.py
   ```
2. Ouvrir l'interface Streamlit dans un autre terminal :
   ```bash
   streamlit run streamlit_app/main.py
   ```

Ensuite, chargez une image depuis l'interface pour tester l'extraction.

## 🏗️ Architecture

Le projet se compose de trois parties principales :

- **Backend FastAPI** (`backend/main.py`) : reçoit les fichiers téléversés et renvoie les données extraites en JSON et GEDCOM.
- **Interface Streamlit** (`streamlit_app/main.py`) : permet d'envoyer des documents et de visualiser les résultats.
- **Pipeline d'extraction** : actuellement un `dummy_extract` fixe, futur branchement d'OCR et de modèles LLM.

## 🚧 Limitations actuelles

- Extraction factice et limitée à un exemple statique.
- Aucune authentification ou gestion des utilisateurs.
- Seule la conversion d'actes de naissance est prise en charge.
- Peu de validation et de gestion d'erreurs.

## 📋 Exemples de sorties

JSON retourné par l'API :

```json
{
  "name": "John Doe",
  "gender": "M",
  "birth_date": "1 Jan 1900",
  "birth_place": "Paris"
}
```

GEDCOM généré :

```
0 @I1@ INDI
1 NAME John Doe
1 SEX M
1 BIRT
2 DATE 1 Jan 1900
2 PLAC Paris
```

## 🤝 Contribuer

1. Forker le dépôt et créer une branche pour votre fonctionnalité ou correction.
2. Installer les dépendances et exécuter les tests (`pytest`).
3. Ouvrir une Pull Request décrivant clairement les changements.

Merci de respecter les conventions PEP 8 et d'ajouter des tests si possible.

## 🗺️ Feuille de route

- Remplacer `dummy_extract` par une véritable pipeline OCR + LLM.
- Supporter d'autres types d'actes (mariage, décès).
- Ajouter authentification et gestion multi-utilisateurs.
- Intégration complète avec l'API FamilySearch.
- Mettre en place CI/CD et améliorer la couverture de tests.
