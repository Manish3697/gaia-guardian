import requests

def get_weather():

    url = "https://api.open-meteo.com/v1/forecast?latitude=11.6643&longitude=78.1460&current=temperature_2m,relative_humidity_2m"

    response = requests.get(url)

    return response.json()