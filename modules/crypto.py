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


def format(number):
    formatted = ''
    count = 0
    while count < len(number):
        if number[count] == '.':
            formatted = formatted + '.'
            if (len(number) - count) > 2:
                count = (len(number) - 2)
            elif (count + 1) == (len(number) - 1):
                formatted = formatted + number[count+1]
                formatted = formatted + '0'
                count += 2
            else:
                count += 1
        else:
            formatted = formatted + number[count]
            count += 1
    return formatted


def crypto_price(coin, currency):
    common = ['BTC', 'ETH', 'BCH', 'LTC']
    if coin in common and currency == 'USD':
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
        j = r.json()
        for item in j:
            if item['symbol'] == coin:
                price = str(item['price_usd'])
                fixed_price = format(price)
                print('\n' + coin + ' is currently worth ' + fixed_price +
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
                price = str(item[cur])
                fixed_price  = format(price)
                print('\n' + coin + ' is currently worth ' + fixed_price +
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
                price = str(item[cur])
                fixed_price = format(price)
                print('\n' + coin + ' is currently worth ' + fixed_price +
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
    crypto_price('BTC', 'USD')
    crypto_price('ETH', 'NZD')
#    crypto_price('BAY', 'USD')
#    crypto_price('ZZZ', 'JPY')
