import argparse
from modules.crypto import get_price, currency_check 
from modules.weather import galv_weather, caribou_weather
from modules.xmas import days_till_xmas
from modules.hnews import hacker_news

def btc(args):
    if not currency_check(args.fiat.upper()):
        print('\nInvalid currency.')
        return False
    price = get_price(args.fiat.upper())
    print('\nBitcoin is currently worth ' + price[:-2] + ' in ' + args.fiat.upper())

def wth(args):
    if args.place == 'gal':
        weather = galv_weather()
        print('\n' + weather['detailedForecast'])
    elif args.place == 'car':
        weather = caribou_weather()
        print('\n' + weather['detailedForecast'])
    else:
        print('\nInvalid city.')

def xmas(args):
    days_till_xmas()

def hnews(args):
    print('\n')
    hacker_news(int(args.stories))

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

btc_parser = subparsers.add_parser('btc')
btc_parser.add_argument('fiat', nargs='?', default='USD', const='USD')
btc_parser.set_defaults(func=btc)

wth_parser = subparsers.add_parser('wth')
wth_parser.add_argument('place', nargs='?', default='car', const='car')
wth_parser.set_defaults(func=wth)

xmas_parser = subparsers.add_parser('xmas')
xmas_parser.set_defaults(func=xmas)

hnews_parser = subparsers.add_parser('hnews')
hnews_parser.add_argument('stories', nargs='?', default=5, const=5)
hnews_parser.set_defaults(func=hnews)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
