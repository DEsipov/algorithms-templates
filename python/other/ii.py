#!-*-coding:utf-8-*-


import json

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

filename = "intents_dataset.json"
with open(filename, 'r', encoding='UTF-8') as file:
    data = json.load(file)

x = []
y = []
for name in data:
    for phrase in data[name]['examples']:
        x.append(phrase)
        y.append(name)
    for phrase in data[name]['responses']:
        x.append(phrase)
        y.append(name)

vectorizer = CountVectorizer()
vectorizer.fit(x)
x_vec = vectorizer.transform(x)

model_mlp = MLPClassifier()
# model_mlp.fit(x_vec, y)  - комп вырубается