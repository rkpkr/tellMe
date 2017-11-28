import argparse
from modules.crypto import get_price, currency_check 

def btc(args):
    if not currency_check(args.fiat):
        print('Invalid currency.')
        return False
    price = get_price(args.fiat)
    print('Bitcoin is currently worth ' + price + ' in ' + args.fiat)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

btc_parser = subparsers.add_parser('btc')
btc_parser.add_argument('fiat', nargs='?', default='USD', const='USD')
btc_parser.set_defaults(func=btc)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
