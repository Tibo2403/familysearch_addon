"""Tests verifying LLaVA extraction integrates with GEDCOM conversion."""

import json
from pathlib import Path

import fastapi.dependencies.utils as fdu


def _noop():
    """Bypass FastAPI's python-multipart dependency check."""

    return None


fdu.ensure_multipart_is_installed = _noop

from backend import main
from src.familysearch_addon import birth_record_json_to_gedcom


def test_llava_extract_to_gedcom(monkeypatch, tmp_path: Path):
    """Pipeline output should feed correctly into GEDCOM generator."""

    expected = {
        "name": "Jane Smith",
        "gender": "F",
        "birth_date": "2 Feb 1900",
        "birth_place": "London",
    }

    class DummyResponse:
        def json(self):
            return {"response": json.dumps(expected)}

        def raise_for_status(self):  # pragma: no cover - no-op
            pass

    def fake_post(url, json=None, timeout=0):  # pragma: no cover - deterministic
        return DummyResponse()

    monkeypatch.setattr("backend.main.requests.post", fake_post)

    img = tmp_path / "test.png"
    img.write_bytes(b"data")

    record = main.llava_extract(str(img))
    assert record == expected

    gedcom = birth_record_json_to_gedcom(record)
    assert gedcom == (
        "0 @I1@ INDI\n"
        "1 NAME Jane Smith\n"
        "1 SEX F\n"
        "1 BIRT\n"
        "2 DATE 2 Feb 1900\n"
        "2 PLAC London"
    )

