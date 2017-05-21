from requests_oauthlib import OAuth1Session
import json

with open('./secret.json') as fp:
    data = json.load(fp)

twitter = OAuth1Session(
    data['consumerKey'],
    data['consumerSecret'],
    data['accessToken'],
    data['accessTokenSecret']
)

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {
    'tweet_mode': 'extended',
    'count': 3000
}

req = twitter.get(url, params=params)


def get_text(tweet):
    if 'retweeted_status' in tweet:
        return tweet['retweeted_status']['full_text']
    else:
        return tweet['full_text']


if req.status_code == 200:
    timeline = json.loads(req.text)
    with open('./data/data.json', 'w') as fp:
        json.dump([get_text(tweet) for tweet in timeline], fp)

else:
    print(f'Error: {req.status_code}')
