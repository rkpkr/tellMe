import argparse

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
    if args.coin is not None and args.fiat is not None:
        cn = args.coin
        ft = args.fiat
    elif 'crypto' in cfg_vals:
        cn = cfg_vals['crypto']['def_coin']
        ft = cfg_vals['crypto']['def_fiat']
    else:
        print('\nInvalid Parameters.')
        return False
    if not currency_check(ft.upper()):
        print('\nInvalid currency.')
        return False
    cprice = crypto_price(cn.upper(), ft.upper())
    if cn in cfg_vals['crypto']:
        print('Your ' + cn.upper() + ' is currently worth ' + 
            str(float(cfg_vals['crypto'][cn]) * float(cprice)) +
            ' ' + ft.upper() + '.')

def wth(args):
    from modules.weather import get_weather, get_coords
    if args.town is not None and args.area is not None:    
        t = args.town
        a = args.area
    else:
        try:
            t = cfg_vals['weather']['town']
            a = cfg_vals['weather']['area']
        except:
            print('\nNo town provided.')
            return False
    latlon = get_coords(t, a)
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
    if 'articles' in cfg_vals['hnews']:
        ars = cfg_vals['hnews']['articles']
    else:
        ars = args.stories
    print('\n', end='')
    hacker_news(int(ars))

def fx(args):
    from modules.forex import frx
    if args.base is not None and args.target is not None:
        bs = args.base
        tg = args.target
    elif 'forex' in cfg_vals: 
        bs = cfg_vals['forex']['base']
        tg = cfg_vals['forex']['target']
    else:
        print('\nInvalid parameters.')
        return False
    try:
        value = frx(bs.upper(), tg.upper())
        print('\nOne ' + bs.upper() + ' is worth ' + str(value) + ' ' + tg.upper() + '.')
    except:
        print('\nInvalid parameters.')
        return False

def reddit(args):
    from modules.reddit import sub_headlines
    if args.sub is not None and args.titles is not None:
        subred = args.sub
        headlines = args.titles
    elif 'reddit' in cfg_vals: 
        subred = cfg_vals['reddit']['subreddit']
        headlines = cfg_vals['reddit']['headlines']
    else:
        print('\nInvalid parameters.')
        return False
    try:
        response = sub_headlines(subred, int(headlines))
        j = response.json()
        print('\n', end='')
        for x in range(len(j['data']['children'])):
            print(j['data']['children'][x]['data']['title'])
            print('https://www.reddit.com' + j['data']['children'][x]['data']['permalink'] + '\n')
    except:
        print('\nInvalid parameters')
        return False


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
hnews_parser.add_argument('stories', nargs='?', default=5, const=5, help='how many headlines you want to see')
hnews_parser.set_defaults(func=hnews)

fx_parser = subparsers.add_parser('fx', help='Find the exchange rate of one currency into another.')
fx_parser.add_argument('base', nargs='?', help='base currency to compare to target currency')
fx_parser.add_argument('target', nargs='?', help='target currency to be compared to')
fx_parser.set_defaults(func=fx)

reddit_parser = subparsers.add_parser('reddit', help='Grab a specified number of headlines from a particular subreddit.')
reddit_parser.add_argument('sub', nargs='?', help='subreddit to grab headlines from')
reddit_parser.add_argument('titles', nargs='?', help='number of headlines to grab')
reddit_parser.set_defaults(func=reddit)

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
    args.func(args)
