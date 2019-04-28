# Airport App functions

import requests

def get_airports(city):

    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query="+city
    response = requests.get(url,
    headers={
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "d1f1096a58mshf4c74db98fa26c8p1a8b67jsn0f46f81a2d16"
        }
    )

    data = response.json()

    if data['Places'] == []:
        return 0, False
    else:
        return data, True
