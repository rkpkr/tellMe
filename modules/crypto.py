import requests

# Powered by CoinDesk
# https://www.coindesk.com/price/

def get_price(currency):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(
        currency))
    price = r.json()
    return price['bpi'][currency]['rate']

def currency_check(currency):
    common = ['USD','JPY','EUR','GBP']
    if currency in common:
        return True
    else:
        r = requests.get('https://api.coindesk.com/v1/bpi/supported-currencies.json')
        j = r.json()
        currency_list = []
        for item in j:
            currency_list.append(item['currency'])
        if currency in currency_list:
            return True
        else:
            return False


if __name__ == '__main__':
    print(get_price('USD'))
