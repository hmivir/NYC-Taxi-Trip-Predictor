from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import predictions

app = FastAPI()

# Include routers
app.include_router(predictions.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to NYC Taxi Predictor API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 