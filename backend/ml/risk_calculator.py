def calculate_risk(
    ndvi,
    rainfall_deficit,
    reservoir_level
):
    
    ndvi_risk = (1 - ndvi) * 40
    rainfall_risk = rainfall_deficit * 30
    reservoir_risk = (1 - reservoir_level) * 30

    total_risk = (
        ndvi_risk
        + rainfall_risk
        + reservoir_risk
    )

    return round(min(total_risk,100),2)