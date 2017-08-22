import json
import numpy as np
import processer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

with open('data/feature.json') as fp:
    feature = json.load(fp)

with open('data/train.json') as fp:
    train = json.load(fp)

word_lists = []
preferences = []
for item in train:
    desc = processer.remove_url(item['description'])
    desc = processer.extract_word(desc)
    word_lists.append(desc)
    preferences.append(item['preference'])

X = []
for word_list in word_lists:
    count = 0
    for word in word_list:
        if word in feature:
            count += 1
    X.append([count])

X_train, X_test, y_train, y_test = train_test_split(X, preferences, test_size=0.3, random_state=42)

lr = LogisticRegression(
    multi_class='ovr',
    random_state=42
)

lr.fit(X_train, y_train)
preds = lr.predict(X_test)

print(y_test)
print(preds)
print(f'accuracy: {accuracy_score(y_test, preds):2.5f}')
