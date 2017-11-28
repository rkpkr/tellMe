import argparse

def btc(args):
    print('{0} is currently worth X {1}.'.format(args.coin, args.fiat))

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

btc_parser = subparsers.add_parser('btc')
btc_parser.add_argument('coin', nargs='?', default='btc', const='btc')
btc_parser.add_argument('fiat', nargs='?', default='usd', const='usd')
btc_parser.set_defaults(func=btc)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
