import requests
import os
import logging


def get_weather(town, area):
    key = os.environ['MQKey']
    wth_key = os.environ['WTH']
    url = ('http://www.mapquestapi.com/geocoding/v1/address?key=' + str(key) +
            '&location=' + town + ',' + area)
    logging.debug(url)
    r = requests.get(url)
    j = r.json()
    lat = str(j['results'][0]['locations'][0]['latLng']['lat'])
    lng = str(j['results'][0]['locations'][0]['latLng']['lng'])
    logging.debug(lat)
    logging.debug(lng)
    url2 = ('http://api.openweathermap.org/data/2.5/weather?lat=' + lat[0:-4] + '&lon=' + 
             lng[0:-4] + '&APPID=' + str(wth_key) + '&units=imperial')
    logging.debug(url2)
    r2 = requests.get(url2)
    j2 = r2.json()
    #logging.debug(j2)
    return j2['weather'][0]['description']




# This is the old weather module based on the weather.gov API.
# It would give errors at random and I could never get to the
# root of the problem. It was most likely either an issue with
# their API, or their server was rejecting my requests because
# it decided this program wasn't trusted. 
'''
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
'''

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
