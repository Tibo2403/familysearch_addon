"""Tests for the upload endpoint."""

import asyncio
import io

import pytest
from fastapi import HTTPException, UploadFile

import fastapi.dependencies.utils as fdu

# Skip the runtime check for python-multipart during tests.
fdu.ensure_multipart_is_installed = lambda: None

import backend.main as main


def test_upload_rejects_invalid_file_type():
    file = UploadFile(
        file=io.BytesIO(b"data"),
        filename="test.txt",
        headers={"content-type": "text/plain"},
    )
    with pytest.raises(HTTPException) as exc:
        asyncio.run(main.upload(file))
    assert exc.value.status_code == 400


def test_upload_handles_extraction_failure(monkeypatch):
    file = UploadFile(
        file=io.BytesIO(b"data"),
        filename="test.png",
        headers={"content-type": "image/png"},
    )

    def _fail(path: str):  # pragma: no cover - used only for testing
        raise Exception("boom")

    monkeypatch.setattr(main, "dummy_extract", _fail)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(main.upload(file))
    assert exc.value.status_code == 500
    assert "boom" in exc.value.detail

