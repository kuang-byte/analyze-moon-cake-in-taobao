import os.path

import pandas

fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/mooncake.txt')

f = open(fn, encoding='utf-8')

data = pandas.read_csv(f, sep=",", names=["title", "price", "sales", "location"])
print(data.describe())
