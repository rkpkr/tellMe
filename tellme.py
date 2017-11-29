import argparse
from modules.crypto import get_price, currency_check 
from modules.weather import galv_weather, caribou_weather

def btc(args):
    if not currency_check(args.fiat):
        print('\nInvalid currency.')
        return False
    price = get_price(args.fiat)
    print('\nBitcoin is currently worth ' + price + ' in ' + args.fiat)

def wth(args):
    if args.place == 'gal':
        weather = galv_weather()
        print('\n' + weather['detailedForecast'])
    elif args.place == 'car':
        weather = caribou_weather()
        print('\n' + weather['detailedForecast'])
    else:
        print('\nInvalid city.')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

btc_parser = subparsers.add_parser('btc')
btc_parser.add_argument('fiat', nargs='?', default='USD', const='USD')
btc_parser.set_defaults(func=btc)

wth_parser = subparsers.add_parser('wth')
wth_parser.add_argument('place', nargs='?', default='car', const='car')
wth_parser.set_defaults(func=wth)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
