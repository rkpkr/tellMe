import argparse
import sys

# This is a general purpose function to grab the parameters for the subparsers either
# from the command line arguments, or, if no command line arguments are given, from
# the config file. For usage, look further down in the code at one of the functions
# that uses this.
def get_params(cfg_sect, *params):
    final_params = []
    for p in params:
        try:
            if cli_params[p] is not None:
                final_params.append(cli_params[p])
            elif p in cfg_vals[cfg_sect]:
                final_params.append(cfg_vals[cfg_sect][p])
        except KeyError:
            continue
    if len(final_params) < len(params):
        print('\nInsufficient parameters.')
        sys.exit(1)
    else:
        return final_params

def config(args):
    from modules.config import default_config, add_config
    if args.section is None:
        print('\nInvalid parameters.')
        return False
    elif args.section.lower() == 'new':
        default_config()
        print('\nNew configuration file created.')
        return True;
    else:
        try:
            add_config(args.section, args.name, args.value)
            print('\n' + args.value + ' assigned to ' + args.name + ' in ' + args.section)
        except:
            print('\nInvalid parameters.')
            return False
        

def coin(args):
    from modules.crypto import currency_check, format, crypto_price 
    prm = get_params('crypto', 'coin', 'fiat')
    if not currency_check(prm[1].upper()):
        print('\nInvalid currency.')
        return False
    cprice = crypto_price(prm[0].upper(), prm[1].upper())
    if prm[0] in cfg_vals['crypto']:
        print('Your ' + prm[0].upper() + ' is currently worth ' + 
            str(float(cfg_vals['crypto'][prm[0]]) * float(cprice)) +
            ' ' + prm[1].upper() + '.')

def wth(args):
    from modules.weather import get_weather, get_coords
    prm = get_params('weather', 'town', 'area')
    latlon = get_coords(prm[0], prm[1])
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
    prm = get_params('hnews', 'stories')
    print('\n', end='')
    hacker_news(int(prm[0]))

def fx(args):
    from modules.forex import frx
    prm = get_params('forex', 'base', 'target')
    try:
        value = frx(prm[0].upper(), prm[1].upper())
        print('\nOne ' + prm[0].upper() + ' is worth ' + str(value) + ' ' + prm[1].upper() + '.')
    except:
        print('\nInvalid parameters.')
        return False

def reddit(args):
    from modules.reddit import sub_headlines
    prm = get_params('reddit', 'subreddit', 'headlines')
    try:
        response = sub_headlines(prm[0], int(prm[1]))
        j = response.json()
        print('\n', end='')
        for x in range(len(j['data']['children'])):
            print(j['data']['children'][x]['data']['title'])
            print('https://www.reddit.com' + j['data']['children'][x]['data']['permalink'] + '\n')
    except:
        print('\nInvalid parameters')
        return False

def stock(args):
    from modules.stocks import get_stock
    prm = get_params('stocks', 'stock')
    data = get_stock(prm[0])
    print('\nStock:          ' + data['companyName'])
    print('52 Week High:   ' + str(data['week52high']))
    print('52 Week Low:    ' + str(data['week52low']))
    print('52 Week Change: ' + str(data['week52change']))



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
config_parser.add_argument('section', nargs='?', help='section in config to add value to')
config_parser.add_argument('name', nargs='?', help='item you want to add a value to in config')
config_parser.add_argument('value', nargs='?', help='value you want to add to specified item') 
config_parser.set_defaults(func=config)

coin_parser = subparsers.add_parser('coin', help='Find the value of a cryptocurrency in specified fiat currency.')
coin_parser.add_argument('coin', nargs='?', help='cryptocurrency you want to see the value of, e.g. BTC for Bitcoin, ETH for Ethereum, etc.')
coin_parser.add_argument('fiat', nargs='?', help='desired currency to convert to, e.g. USD)')
coin_parser.set_defaults(func=coin)

wth_parser = subparsers.add_parser('wth', help='Find the current weather for specified location.')
wth_parser.add_argument('town', nargs='?', help='town to get weather for')
wth_parser.add_argument('area', nargs='?', help='state or country town is in')
wth_parser.set_defaults(func=wth)

xmas_parser = subparsers.add_parser('xmas', help='Find how many days until Christmas.')
xmas_parser.set_defaults(func=xmas)

hnews_parser = subparsers.add_parser('hnews', help='Retrieve a number of top headlines from Hacker News.')
hnews_parser.add_argument('stories', nargs='?', help='how many headlines you want to see')
hnews_parser.set_defaults(func=hnews)

fx_parser = subparsers.add_parser('fx', help='Find the exchange rate of one currency into another.')
fx_parser.add_argument('base', nargs='?', help='base currency to compare to target currency')
fx_parser.add_argument('target', nargs='?', help='target currency to be compared to')
fx_parser.set_defaults(func=fx)

reddit_parser = subparsers.add_parser('reddit', help='Grab a specified number of headlines from a particular subreddit.')
reddit_parser.add_argument('subreddit', nargs='?', help='subreddit to grab headlines from')
reddit_parser.add_argument('headlines', nargs='?', help='number of headlines to grab')
reddit_parser.set_defaults(func=reddit)

stock_parser = subparsers.add_parser('stock', help='Grab recent high/low for specified stock.')
stock_parser.add_argument('stock', nargs='?', help='stock ticker to get information about')
stock_parser.set_defaults(func=stock)

zones_parser = subparsers.add_parser('zones', help='Display time in various time zones.')
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
    cli_params = vars(args)
    args.func(args)
