from fastapi import FastAPI
from backend.ml.risk_calculator import calculate_risk
from backend.data.weather_api import get_weather
from backend.ml.environmental_risk import environmental_risk
from backend.data.ndvi_service import get_ndvi
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
@app.get("/weather-risk")
def weather_risk():

    weather = get_weather()

    temp = weather["current"]["temperature_2m"]
    humidity = weather["current"]["relative_humidity_2m"]

    ndvi_data = get_ndvi()
    ndvi = ndvi_data["ndvi"]
    reservoir = 0.45

    risk = environmental_risk(
        temp,
        humidity,
        ndvi,
        reservoir
    )

    return {
        "district": "Salem",
        "risk_score": risk,
        "temperature": temp,
        "humidity": humidity,
        "ndvi": ndvi,
        "reservoir_level": reservoir
    }