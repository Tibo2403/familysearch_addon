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
