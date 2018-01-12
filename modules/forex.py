import requests

def frx(start_cur, target_cur):
    headers = {
            'User-Agent': 'https://github.com/rkpkr/tellMe'
    }
    url = 'https://api.fixer.io/latest?base=' + str(start_cur) + '&symbols=' + str(target_cur)
    r = requests.get(url, headers=headers)
    j = r.json()
    return j['rates'][target_cur]


if __name__ == '__main__':
    print(frx('USD','JPY'))
