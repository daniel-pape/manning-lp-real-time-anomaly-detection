import joblib
import os
from service.main import app
from service.schemas import Prediction, PredictionRequest
from sklearn.ensemble import IsolationForest
from fastapi import HTTPException
from pathlib import Path

CWD = Path(__file__).parent
clf: IsolationForest = joblib.load(CWD / "model" / "model.joblib")


@app.post("/prediction", response_model=Prediction)
def predict(request: PredictionRequest):
    response = {}

    feature_vector: List[float] = request.feature_vector
    is_score: bool = request.is_score

    if len(feature_vector) != 2:
        raise HTTPException(status_code=400,
                            detail=f"Feature vector must have length 2. "
                                   f"Instead got feature_vector={feature_vector}")

    prediction = clf.predict([feature_vector])
    response["is_inlier"] = int(prediction[0])

    response["anomaly_score"] = None

    if is_score:
        anomaly_scores = clf.score_samples([feature_vector])
        response["anomaly_score"] = anomaly_scores[0]

    return response

@app.get("/model_information")
def model_information():
    return clf.get_params()
