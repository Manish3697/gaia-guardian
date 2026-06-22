import json

def get_ndvi():

    with open("datasets/ndvi_salem.json") as file:
        data = json.load(file)

    return data