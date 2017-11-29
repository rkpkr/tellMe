import requests

def caribou_weather():
    r = requests.get('https://api.weather.gov//points/46.866,-67.9906/forecast')
    j = r.json()
    return j['properties']['periods'][0]

def galv_weather():
    r = requests.get('https://api.weather.gov//points/29.2859,-94.8232/forecast')
    j = r.json()
    return j['properties']['periods'][0]


if __name__ == '__main__':
    w = caribou_weather()
    print(w['detailedForecast'])
