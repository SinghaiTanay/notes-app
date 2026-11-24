from fastapi import FastAPI

from app.api.health import router as health_router


app = FastAPI(
    title="Notes API",
    description="FastAPI application with PostgreSQL",
    version="1.0.0"
)


app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)


@app.get("/")
def home():
    return {
        "message": "Notes API is running"
    }