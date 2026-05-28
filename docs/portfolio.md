# Portfolio Brief

## Problem

Genealogy workflows often require transforming scanned civil records into structured family-history data. This project explores an API and UI flow for extracting record fields and converting birth records to GEDCOM.

## What This Shows

- FastAPI endpoint design.
- Streamlit-based manual testing UI.
- Testable extraction wrapper around an OCR/LLM dependency.
- GEDCOM formatting logic.
- Safe local demo structure with mocked extraction in tests.

## Demo Flow

1. Start the API.
2. Start the Streamlit app.
3. Upload a sample record image.
4. Review extracted JSON and generated GEDCOM.
5. Run `pytest -q` to show deterministic tests.

## Recruiter Notes

This project demonstrates Python API design, testing around external model calls, and a practical data-conversion workflow.

