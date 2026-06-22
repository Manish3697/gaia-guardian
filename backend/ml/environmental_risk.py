def environmental_risk(
    temperature,
    humidity,
    ndvi,
    reservoir_level
):

    score = 0

    if temperature > 35:
        score += 25

    elif temperature > 30:
        score += 15

    if humidity < 40:
        score += 20

    elif humidity < 60:
        score += 10

    score += (1 - ndvi) * 30

    score += (1 - reservoir_level) * 30

    return round(min(score, 100), 2)