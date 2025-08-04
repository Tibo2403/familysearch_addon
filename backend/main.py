from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import base64
import json
import requests
import tempfile
from typing import Dict
from src.familysearch_addon import birth_record_json_to_gedcom

app = FastAPI(title="FamilySearch Addon API")


def llava_extract(path: str) -> Dict[str, str]:
    """Extract birth record fields using the LLaVA/Ollama pipeline.

    Parameters
    ----------
    path: str
        Path to an image file containing a birth record.

    Returns
    -------
    Dict[str, str]
        Dictionary with ``name``, ``gender``, ``birth_date`` and
        ``birth_place`` keys.  Missing values are returned as empty
        strings.
    """
    with open(path, "rb") as img:
        image_b64 = base64.b64encode(img.read()).decode("utf-8")

    prompt = (
        "Extract the person's name, gender, birth date and birth place "
        "from this birth record. Return a JSON object with keys 'name', "
        "'gender', 'birth_date', 'birth_place'."
    )
    payload = {
        "model": "llava",
        "prompt": prompt,
        "images": [image_b64],
        "stream": False,
    }

    resp = requests.post(
        "http://localhost:11434/api/generate", json=payload, timeout=60
    )
    resp.raise_for_status()
    raw_text = resp.json().get("response", "{}")
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        data = {}

    return {
        "name": data.get("name", ""),
        "gender": data.get("gender", ""),
        "birth_date": data.get("birth_date", ""),
        "birth_place": data.get("birth_place", ""),
    }


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """Receive a file and return extracted JSON and GEDCOM."""
    suffix = file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    record = llava_extract(temp_path)
    gedcom = birth_record_json_to_gedcom(record)

    return JSONResponse({"json": record, "gedcom": gedcom})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
