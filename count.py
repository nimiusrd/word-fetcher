import json
from collections import Counter
from processer import processer

with open('./data/words.json') as fp:
    data = json.load(fp)

with open('./data/count.json', 'w') as fp:
    d = []
    for word in data:
        if processer.is_stopwords(word):
            pass
        elif processer.is_twitter_username(word):
            pass
        elif processer.is_number(word):
            pass
        else:
            d.append(word)
    d = Counter(d)
    d = d.most_common()
    json.dump(d, fp)
