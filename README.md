# FamilySearch Addon

FamilySearch Addon is an experimental project for extracting genealogical information from historical records.

## Project Goals and Planned Features

- **Image Uploads:** Users can upload scans of civil records such as birth, marriage and death certificates.
- **OCR/AI Extraction:** Extract data from uploaded images using optical character recognition and language models.
- **GEDCOM Export:** Convert extracted data into the [GEDCOM](https://en.wikipedia.org/wiki/GEDCOM) genealogy format.
- **FamilySearch Integration:** Send parsed individuals and relationships directly to FamilySearch.

## Prerequisites

- Python 3.10 or newer
- Packages listed in `requirements.txt`:
  - FastAPI
  - Uvicorn
  - Streamlit
  - Ollama
  - python-gedcom

Install the requirements with:

```bash
pip install -r requirements.txt
```

## Installation & Local Development

1. Clone this repository and install the dependencies as above.
2. Start the backend API:

   ```bash
   uvicorn backend.api:app --reload
   ```

3. In a separate terminal, run the Streamlit interface:

   ```bash
   streamlit run streamlit_app/app.py
   ```

These commands start a local development server where you can test the upcoming features.

## Example: Parse a French Birth Record JSON

Below is a minimal example using Python to parse a JSON representation of a French birth certificate (`naissance`). This illustrates the kind of structured data that could be produced by the OCR/AI step:

```python
import json

naissance_json = """
{
    "acte": "naissance",
    "nom": "Dupont",
    "prenom": "Jean",
    "date": "1890-03-12",
    "commune": "Paris"
}
"""

record = json.loads(naissance_json)
print(record["prenom"], record["nom"], "born on", record["date"], "in", record["commune"])
```

Running this example would output:

```
Jean Dupont born on 1890-03-12 in Paris
```

This serves as a simple demonstration of how the project plans to transform extracted record data into a format ready for GEDCOM export or integration with FamilySearch.

