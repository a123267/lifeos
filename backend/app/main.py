from fastapi import FastAPI

app = FastAPI(
    title="LifeOS API",
    description="Personal Productivity and Analytics Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to LifeOS API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "LifeOS"
    }