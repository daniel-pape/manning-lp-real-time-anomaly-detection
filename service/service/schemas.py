from pydantic import BaseModel, Extra
from typing import List, Optional

class PredictionRequest(BaseModel):
    feature_vector: List[float]
    is_score: bool

class Prediction(BaseModel):
    is_inlier: int
    anomaly_score: Optional[float]
