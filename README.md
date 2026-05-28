# FamilySearch Addon

[![Python Tests](https://github.com/Tibo2403/familysearch_addon/actions/workflows/tests.yml/badge.svg)](https://github.com/Tibo2403/familysearch_addon/actions/workflows/tests.yml)

FamilySearch Addon is an experimental FastAPI and Streamlit project for extracting genealogical data from civil records and converting it to GEDCOM.

## Features

- Upload scanned birth, marriage, or death records.
- Extract structured fields from images through an OCR/LLM pipeline.
- Convert extracted birth-record data to GEDCOM.
- Provide a Streamlit interface for manual testing.
- Keep the extraction function isolated so it can be replaced by better OCR or FamilySearch integrations later.

## Current Architecture

```text
backend/main.py          FastAPI upload endpoint and LLaVA extraction wrapper
streamlit_app/main.py    Streamlit UI for upload and result preview
src/familysearch_addon/  GEDCOM conversion helpers
tests/                   API, extraction, and GEDCOM tests
```

The current extraction implementation calls an Ollama LLaVA model at `http://localhost:11434/api/generate`. Tests mock that call, so CI does not require Ollama.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On Linux or macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Locally

Start the API:

```bash
python backend/main.py
```

Start the Streamlit UI in another terminal:

```bash
streamlit run streamlit_app/main.py
```

The Streamlit app reads the API URL from `API_URL`, defaulting to `http://localhost:8000`.

## Tests

```bash
pytest -q
```

The test suite covers:

- GEDCOM formatting.
- Upload endpoint validation and error handling.
- LLaVA response parsing into GEDCOM-compatible data.

## Example API Output

```json
{
  "json": {
    "name": "Jane Smith",
    "gender": "F",
    "birth_date": "2 Feb 1900",
    "birth_place": "London"
  },
  "gedcom": "0 @I1@ INDI\n1 NAME Jane Smith\n1 SEX F\n1 BIRT\n2 DATE 2 Feb 1900\n2 PLAC London"
}
```

## Portfolio Assets

- `docs/portfolio.md` explains the project in recruiter/client terms.
- `docs/demo-media.md` lists screenshots and GIFs to capture.
- `docs/issue-backlog.md` contains ready-to-create GitHub issues.
- `examples/` contains safe demo placeholders.
- `CHANGELOG.md` tracks release notes.

## Roadmap

- Add a deterministic demo extractor for local portfolio demos.
- Support marriage and death record schemas.
- Add FamilySearch API integration behind explicit credentials.
- Add stronger upload size limits and content validation.
- Add screenshots of the Streamlit workflow.
