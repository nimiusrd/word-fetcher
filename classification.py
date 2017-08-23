import json
import numpy as np

MIN_PERCENT = 1
MAX_PERCENT = 100
MIN_COUNTS = 2
MAX_COUNTS = 100

with open('data/count.json') as fp:
    data = np.array(json.load(fp))

words, counts = data.T
counts = counts.astype(int)
percent = counts / counts.sum() * 100

cond = np.logical_or(
    np.logical_and(MAX_COUNTS >= counts, counts >= MIN_COUNTS),
    np.logical_and(MAX_PERCENT >= percent, percent >= MIN_PERCENT)
)

result = np.where(cond, [words, counts], 0)
result = np.array(result).T.tolist()

with open('data/feature.json', 'w') as fp:
    json.dump([x for x in result if x[0] != '0'], fp)
