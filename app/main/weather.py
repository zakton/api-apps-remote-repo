# Weather App functions

import requests

def get_temperature(city):

    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=facf53d897b2d8fc5f48d2f744b2e3fb'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        return 0, False
    else:
        return data['main']['temp'], True
