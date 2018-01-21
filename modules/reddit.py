import requests
import requests.auth
import os

password = os.environ['RPASS']
username = os.environ['RNAME']
app_id = os.environ['RAPP']
app_secret = os.environ['RSCRT']

def get_token():
    client_auth = requests.auth.HTTPBasicAuth(app_id, app_secret)
    post_data = {'grant_type': 'password',
                'username': username,
                'password': password}
    headers = {'User-Agent': 'tellMe (https://github.com/rkpkr/tellMe)'}
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers)
    return response.json()

def sub_headlines(subreddit, count):
    token_info = get_token()
    token = token_info['access_token']
    type = token_info['token_type']
    auth_token = type + ' ' + token
    headers = {'Authorization': auth_token,
            'User-Agent': 'tellMe (https://github.com/rkpkr/tellMe)'}
    url = ('https://oauth.reddit.com/r/' + subreddit + '/top/?t=day&limit=' + str(count))
    response = requests.get(url, headers=headers)
    return response



if __name__ == '__main__':
    sub = input('Name a subreddit: ')
    r = sub_headlines(sub, 10)
    j = r.json()
#    print(j['data']['children'][0]['data']['title'])
    for x in range(len(j['data']['children'])):
        print(j['data']['children'][x]['data']['title'])
