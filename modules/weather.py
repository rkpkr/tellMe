import requests
import os
import logging


def get_weather(town, area):
    key = os.environ['MQKey']
    headers = {
            'User-Agent': 'https://github.com/rkpkr/tellMe'
    }
    url = ('http://www.mapquestapi.com/geocoding/v1/address?key=' + str(key) +
            '&location=' + town + ',' + area)
    logging.debug(url)
    r = requests.get(url)
    j = r.json()
    lat = str(j['results'][0]['locations'][0]['latLng']['lat'])
    lng = str(j['results'][0]['locations'][0]['latLng']['lng'])
    logging.debug(lat)
    logging.debug(lng)
    url2 = ('https://api.weather.gov/points/' + lat[0:-4] + ',' + 
             lng[0:-4] + '/forecast')
    logging.debug(url2)
    r2 = requests.get(url2, headers=headers)
    j2 = r2.json()
    #logging.debug(j2)
    return j2['properties']['periods'][0]


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
    print(get_weather(city, state))
