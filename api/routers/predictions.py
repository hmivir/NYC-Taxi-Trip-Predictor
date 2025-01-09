from fastapi import APIRouter, HTTPException
from api.schemas.prediction import TripRequest, TripPrediction
from src.models.predictor import TaxiPredictor

router = APIRouter()
predictor = TaxiPredictor()
 