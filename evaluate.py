import json
import numpy as np
import processer
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize

with open('data/feature.json') as fp:
    feature = np.array(json.load(fp))
    feature_word = feature.T[0]
    feature_count = feature.T[1]

with open('data/train.json') as fp:
    train = json.load(fp)

word_lists = []
preferences = []
for item in train:
    desc = processer.remove_url(item['description'])
    desc = processer.extract_word(desc)
    word_lists.append(desc)
    preferences.append(item['preference'])

X = [
        Counter([word for word in word_list if word in feature_word])
        for word_list in word_lists
    ]
v = DictVectorizer()
X = v.fit_transform(X)
X = normalize(X)
X_train, X_test, y_train, y_test = train_test_split(X, preferences, test_size=0.3, random_state=42)

lr = LogisticRegression(
    multi_class='ovr',
    random_state=42
)

lr.fit(X_train, y_train)
preds = lr.predict(X_test)

print(X_train)
print(y_train)
print(X_test)
print(y_test)
print(preds)
print(f'accuracy: {accuracy_score(y_test, preds):2.5f}')
