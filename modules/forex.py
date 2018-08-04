import requests
import xml.etree.ElementTree as ET

def frx():
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }
    url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml?'
    r = requests.get(url, headers=headers)
    tree = ET.fromstring(r.text)
    usd_rate = tree[2][0][0].attrib['rate']
    for child in tree[2][0]:
        print(child.attrib['currency'] + ' : ' + str(round((float(child.attrib['rate']) / float(usd_rate)),2)))


if __name__ == '__main__':
    frx()
