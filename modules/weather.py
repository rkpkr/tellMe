import requests
import os


def get_weather(town, area):
    key = os.environ['MQKey']
    url = ('http://www.mapquestapi.com/geocoding/v1/address?key=' + str(key) +
            '&location=' + town + ',' + area)
    r = requests.get(url)
    j = r.json()
    lat = j['results'][0]['locations'][0]['latLng']['lat']
    lng = j['results'][0]['locations'][0]['latLng']['lng']
    url2 = ('https://api.weather.gov/points/' + str(lat) + ',' + 
             str(lng) + '/forecast')
    r2 = requests.get(url2)
    j2 = r2.json()
    return j2['properties']['periods'][0]


if __name__ == '__main__':
    city = input('city: ')
    state = input('state: ')
    print(get_weather(city, state))
