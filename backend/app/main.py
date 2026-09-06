from fastapi import FastAPI

app = FastAPI(
    title = "ATSight",
    description = "ATS checker and job description parser",
    version = "0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "ATS Resume checker APi is running",
        "status":  "healthy",
    }