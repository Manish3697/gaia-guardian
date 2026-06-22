from fastapi import FastAPI
from backend.ml.risk_calculator import calculate_risk
from backend.data.weather_api import get_weather
app = FastAPI()

@app.get("/")
def home():
    return {"message": "GAIA Guardian Running"}
@app.get("/risk")
def risk():

    score = calculate_risk(
        ndvi=0.42,
        rainfall_deficit=0.38,
        reservoir_level=0.45
    )

    return {
        "district":"Salem",
        "risk_score":score,
        "status":"WARNING"
    }
@app.get("/weather")
def weather():

    data = get_weather()

    return data