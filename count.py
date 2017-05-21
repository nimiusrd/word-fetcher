import json
from collections import Counter
from processer import processer

with open('./data/words.json') as fp:
    data = json.load(fp)

with open('./data/count.json', 'w') as fp:
    d = data
    for word in d:
        if processer.is_stopwords(word):
            d.remove(word)
        elif processer.is_twitter_username(word):
            d.remove(word)
        elif processer.is_number(word):
            d.remove(word)
    d = Counter(d)
    d = d.most_common()
    json.dump(d, fp)
