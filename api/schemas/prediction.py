from pydantic import BaseModel, Field
from datetime import datetime
from typing import Tuple

class Location(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
