import requests
import os
import logging

def get_coords(town, area):
    key = os.environ['MQKey']
    url = ('http://www.mapquestapi.com/geocoding/v1/address?key=' + str(key) +
            '&location=' + town + ',' + area)
    logging.debug(url)
    r = requests.get(url)
    j = r.json()
    lat = str(j['results'][0]['locations'][0]['latLng']['lat'])
    lng = str(j['results'][0]['locations'][0]['latLng']['lng'])
    coords = (lat, lng)
    return coords


def get_weather(coordinates):
    headers = {
            'User-Agent': 'https://github.com/rkpkr/tellMe'
    }
    url2 = ('https://api.weather.gov/points/' + coordinates[0][0:-4] + ',' + 
             coordinates[1][0:-4] + '/forecast')
    logging.debug(url2)
    r2 = requests.get(url2, headers=headers)
    j2 = r2.json()
    #logging.debug(j2)
    return j2['properties']['periods'][0]


def get_weather2(coordinates):
    wth_key = os.environ['WTH']
    url2 = ('http://api.openweathermap.org/data/2.5/weather?lat=' + coordinates[0][0:-4] + '&lon=' + 
             coordinates[1][0:-4] + '&APPID=' + str(wth_key) + '&units=imperial')
    logging.debug(url2)
    r2 = requests.get(url2)
    j2 = r2.json()
    #logging.debug(j2)
    forecast = ('Current weather: '+ j2['weather'][0]['description'] +
                '. The temperature is ' + str(j2['main']['temp']) + 'F, with winds at ' + str(j2['wind']['speed']) +
                'MPH.')
    return forecast




if __name__ == '__main__':
    # These first two lines modify the logger to not show messages from
    # the requests or urllib3 modules.
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.basicConfig(filename='weather.log', level=logging.DEBUG,
                        format='%(asctime)s :: %(message)s',
                        datefmt="%Y-%m-%d %H:%M")
    city = input('city: ')
    state = input('state: ')
    ll = get_coords(city, state)
    print(get_weather(ll))
    print(get_weather2(ll))
