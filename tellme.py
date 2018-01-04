import argparse

def config(args):
    from modules.config import default_config
    if args.create:
        default_config()
        print('\nNew configuration file created.')

def coin(args):
    from modules.crypto import currency_check, format, crypto_price 
    if not currency_check(args.fiat.upper()):
        print('\nInvalid currency.')
        return False
    cprice = crypto_price(args.coin.upper(), args.fiat.upper())
    if args.coin in cfg_vals['Cryptocurrency']:
        print('Your ' + args.coin.upper() + ' is currently worth ' + 
            str(float(cfg_vals['Cryptocurrency'][args.coin]) * float(cprice)) +
            ' ' + args.fiat.upper() + '.')

def wth(args):
    from modules.weather import get_weather, get_coords
    latlon = get_coords(args.town, args.area)
    try:
        weather = get_weather(latlon)
        print('\n' + weather['detailedForecast'])
    except KeyError:
        from modules.weather import get_weather2
        weather = get_weather2(latlon)
        print('\n' + weather)

def xmas(args):
    from modules.xmas import days_till_xmas
    days_till_xmas()

def hnews(args):
    from modules.hnews import hacker_news
    print('\n', end='')
    hacker_news(int(args.stories))

def zones(args):
    from modules.timezones import time_zones
    print('\n', end='')
    time_zones()

def timeleft(args):
    from modules.timeleft import time_left
    print('\n', end='')
    time_left(args.gender.upper(), int(args.year), int(args.month), int(args.day))

parser = argparse.ArgumentParser(prog='tellme',description='Retrieve information without leaving the command line.')
subparsers = parser.add_subparsers()

config_parser = subparsers.add_parser('config', help='Create a new config file or add/change config values.')
config_parser.add_argument('create', nargs='?', default=True, const=True, help='creates new config file')
config_parser.set_defaults(func=config)


coin_parser = subparsers.add_parser('coin', help='Find the value of a cryptocurrency in specified fiat currency.')
coin_parser.add_argument('coin', nargs='?', default='BTC', const='BTC', help='cryptocurrency you want to see the value of, e.g. BTC for Bitcoin, ETH for Ethereum, etc.')
coin_parser.add_argument('fiat', nargs='?', default='USD', const='USD',help='desired currency to convert to, e.g. USD)')
coin_parser.set_defaults(func=coin)

wth_parser = subparsers.add_parser('wth', help='Find the current weather for specified location.')
wth_parser.add_argument('town', nargs='?', default='Caribou', const='Caribou',help='town to get weather for')
wth_parser.add_argument('area', nargs='?', default='ME', const='ME', help='state or country town is in')
wth_parser.set_defaults(func=wth)

xmas_parser = subparsers.add_parser('xmas', help='Find how many days until Christmas.')
xmas_parser.set_defaults(func=xmas)

hnews_parser = subparsers.add_parser('hnews', help='Retrieve a number of top headlines from Hacker News.')
hnews_parser.add_argument('stories', nargs='?', default=5, const=5, help='how many headlines you want to see')
hnews_parser.set_defaults(func=hnews)

zones_parser = subparsers.add_parser('zones', help='Display time in various time zones')
zones_parser.set_defaults(func=zones)

timeleft_parser = subparsers.add_parser('timeleft', help='Find how many years or days you have left to live.')
timeleft_parser.add_argument('gender')
timeleft_parser.add_argument('year', help='year of birth')
timeleft_parser.add_argument('month', help='month of birth')
timeleft_parser.add_argument('day', help='day of birth')
timeleft_parser.set_defaults(func=timeleft)


if __name__ == '__main__':
    from modules.config import import_config
    cfg_vals = import_config()
    args = parser.parse_args()
    args.func(args)
