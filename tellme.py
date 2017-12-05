import argparse


def btc(args):
    from modules.crypto import get_price, currency_check 
    if not currency_check(args.fiat.upper()):
        print('\nInvalid currency.')
        return False
    price = get_price(args.fiat.upper())
    print('\nBitcoin is currently worth ' + price[:-2] + ' in ' + args.fiat.upper())

def wth(args):
    from modules.weather import galv_weather, caribou_weather
    if args.place == 'gal':
        weather = galv_weather()
        print('\n' + weather['detailedForecast'])
    elif args.place == 'car':
        weather = caribou_weather()
        print('\n' + weather['detailedForecast'])
    else:
        print('\nInvalid city.')

def xmas(args):
    from modules.xmas import days_till_xmas
    days_till_xmas()

def hnews(args):
    from modules.hnews import hacker_news
    print('\n', end='')
    hacker_news(int(args.stories))

def timeleft(args):
    from modules.timeleft import time_left
    print('\n', end='')
    time_left(args.gender.upper(), int(args.year), int(args.month), int(args.day))

parser = argparse.ArgumentParser(prog='tellme',description='Retrieve information without leaving the command line.')
subparsers = parser.add_subparsers()

btc_parser = subparsers.add_parser('btc', help='Find the value of bitcoin in specified currency.')
btc_parser.add_argument('fiat', nargs='?', default='USD', const='USD',help='desired currency to convert to (format: 3 character currency code, e.g. USD)')
btc_parser.set_defaults(func=btc)

wth_parser = subparsers.add_parser('wth', help='Find the current weather for specified location.')
wth_parser.add_argument('place', nargs='?', default='car', const='car',help='location to get weather for')
wth_parser.set_defaults(func=wth)

xmas_parser = subparsers.add_parser('xmas', help='Find how many days until Christmas.')
xmas_parser.set_defaults(func=xmas)

hnews_parser = subparsers.add_parser('hnews', help='Retrieve a number of top headlines from Hacker News.')
hnews_parser.add_argument('stories', nargs='?', default=5, const=5, help='how many headlines you want to see')
hnews_parser.set_defaults(func=hnews)

timeleft_parser = subparsers.add_parser('timeleft', help='Find how many years or days you have left to live.')
timeleft_parser.add_argument('gender')
timeleft_parser.add_argument('year', help='year of birth')
timeleft_parser.add_argument('month', help='month of birth')
timeleft_parser.add_argument('day', help='day of birth')
timeleft_parser.set_defaults(func=timeleft)


if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
