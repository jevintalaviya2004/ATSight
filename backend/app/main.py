from fastapi import FastAPI, File, HTTPException, UploadFile

from pathlib import Path
from uuid import uuid4
from app.resume.resume_parser import parse_resume

app = FastAPI(
    title = "ATSight",
    description = "ATS checker and job description parser",
    version = "0.1.0",
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".docx", ".pdf"}

@app.get("/")
def root():
    return {
        "message": "ATS Resume checker APi is running",
        "status":  "healthy",
    }

@app.post("/api/resume/upload")
async def upload_file(file: UploadFile = File(...)):
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX file are supported",
        )

    file_id = f"{uuid4()}{extension}"
    file_path = UPLOAD_DIR / file_id

    try:
        contents = await file.read()
        file_path.write_bytes(contents)

        resume = parse_resume(file_path)

        return {
            "filename": file.filename,
            "file_type": extension,
            "resume": resume,
            }

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code = 500,
            detail = f"Failed to process file: {str(exc)}",
        )

    finally:
        if file_path.exists():
            file_path.unlink()  # Clean up the uploaded file after processing
