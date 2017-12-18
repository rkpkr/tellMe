import requests

# Powered by Coin Market Cap
# https://coinmarketcap.com


def currency_check(currency):
    supported_cur = ["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR",
        "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK",
        "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "USD",
        "ZAR"]
    if currency in supported_cur:
        return True
    else:
        return False

def crypto_price(coin, currency):
    common = ['BTC', 'ETH', 'BCH', 'LTC', 'XRP', 'DASH', 'XMR']
    if coin in common and currency == 'USD':
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
        j = r.json()
        for item in j:
            if item['symbol'] == coin:
                print('\n' + coin + ' is currently worth ' + str(item['price_usd']) +
                        ' in USD, with a change of ' + str(item['percent_change_24h']) +
                        '% in the past 24 hours.')
                return True
    elif coin in common and currency != 'USD':
        u = 'https://api.coinmarketcap.com/v1/ticker/?convert=' + currency + '&limit=10' 
        r = requests.get(u)
        j = r.json()
        for item in j:
            if item['symbol'] == coin:
                cur = 'price_' + currency.lower()
                print('\n' + coin + ' is currently worth ' + str(item[cur]) +
                        ' in ' + currency + ', with a change of ' +
                        str(item['percent_change_24h']) +
                        '% in the past 24 hours.')
                return True
    elif coin not in common:
        u = 'https://api.coinmarketcap.com/v1/ticker/?convert=' + currency
        r = requests.get(u)
        j = r.json()
        for item in j:
            if item['symbol'] == coin:
                cur = 'price_' + currency.lower()
                print('\n' + coin + ' is currently worth ' + str(item[cur]) +
                        ' in ' + currency + ', with a change of ' +
                        str(item['percent_change_24h']) +
                        '% in the past 24 hours.')
                return True
        print('\nCryptocurrency not found.')
        return False


if __name__ == '__main__':
    currency_check('USD')
    currency_check('NZD')
    currency_check('ZZZ')
    currency_check('asdfsdkf')
#    crypto_price('BTC', 'USD')
#    crypto_price('ETH', 'NZD')
    crypto_price('BAY', 'USD')
    crypto_price('ZZZ', 'JPY')
