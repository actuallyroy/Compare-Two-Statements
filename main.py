import requests
import json
import csv

negative_words = []
positive_words = []

with open('neg-pos-words.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row[0] == 'negative':
            negative_words = [i for i in row[1:] if i != ""]
        elif row[0] == 'positive':
            positive_words = [i for i in row[1:] if i != ""]


    
api_key = 'NcOmJTYYsDhBgkV3E-KVBC8Fcs1IgoAIpKdbM9mN3UM'
query = "class 10th CBSE schedule announced"
# r = requests.get('https://api.newscatcherapi.com/v2/search?q=${query}'.format(query = query), headers={'Accept': 'application/json', 'X-Api-Key': api_key})

# articles = r.json()['articles']


from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob("I love pizza", analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)
