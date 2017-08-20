import processer
import json

with open('./data/data.json') as fp:
    data = json.load(fp)

words = []
for tweet in data:
    tweet = processer.remove_url(tweet)
    w = processer.extract_word(tweet)
    if w:
        words.extend(w)

with open('./data/words.json', 'w') as fp:
    json.dump(words, fp)
