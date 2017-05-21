import re
import json


def remove_url(text):
    return re.sub('https?://[a-zA-Z0-9./]+', '', text)


def extract_word(text):
    return re.findall('[a-zA-Z0-9.@]+', text)


with open('stopwords.json') as fp:
    stopwords = json.load(fp)


def is_stopwords(word):
    return word in stopwords


def is_twitter_username(word):
    return re.match('^@[a-zA-Z0-9_]+', word)


def is_number(word):
    return re.match('^[0-9.]+$', word)
