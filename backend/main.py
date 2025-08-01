from fastapi import FastAPI, File, UploadFile
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
    suffix = file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    record = dummy_extract(temp_path)
    gedcom = birth_record_json_to_gedcom(record)

    return JSONResponse({"json": record, "gedcom": gedcom})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
