from bow import bow
import json

with open('./data/data.json') as fp:
    data = json.load(fp)

words = []
for tweet in data:
    tweet = bow.remove_url(tweet)
    w = bow.extract_word(tweet)
    if w:
        words.extend(w)

with open('./data/words.json', 'w') as fp:
    json.dump(words, fp)
