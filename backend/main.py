from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import tempfile
from typing import Dict
from src.familysearch_addon import birth_record_json_to_gedcom

app = FastAPI(title="FamilySearch Addon API")


def dummy_extract(path: str) -> Dict[str, str]:
    """Placeholder extraction using a static result.

    In a real implementation this would call the LLaVA/Ollama
    pipeline to extract text from the uploaded image.
    """
    return {
        "name": "John Doe",
        "gender": "M",
        "birth_date": "1 Jan 1900",
        "birth_place": "Paris",
    }


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """Receive a file and return extracted JSON and GEDCOM."""
    allowed_types = {"image/png", "image/jpeg", "application/pdf"}
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    suffix = file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    try:
        record = dummy_extract(temp_path)
        gedcom = birth_record_json_to_gedcom(record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse({"json": record, "gedcom": gedcom})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
