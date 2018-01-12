import requests

def hacker_news(desired_num):
    headers = {
            'User-Agent': 'https://github.com/rkpkr/tellMe'
    }
    r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json', headers=headers)
    j = r.json()
    for x in range(desired_num):
        url = 'https://hacker-news.firebaseio.com/v0/item/' + str(j[x]) + '.json'
        r2 = requests.get(url, headers=headers)
        j2 = r2.json()
        try:
            print(j2['title'])
            print('https://news.ycombinator.com/item?id=' + str(j[x]) + '\n')
        except UnicodeEncodeError:            
            print(j2['title'].encode('utf-8'))
            print('https://news.ycombinator.com/item?id=' + str(j[x]) + '\n')


if __name__ == '__main__':
    hacker_news(10)
