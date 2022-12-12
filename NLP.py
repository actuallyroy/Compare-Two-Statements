import csv
import json

f = open('./verbs.json', 'r', encoding='utf-8-sig')

verbs = json.load(f)['verbs']





auxiliary_verbs_positive = []
auxiliary_verbs_negative = []

adjectives = []
adjectives_antonyms = {}
adjectives_synonyms = {}

with open('adjectives.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        adjectives = row[1:]
        break

with open('auxiliary_verbs.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row[0] == 'positive':
            auxiliary_verbs_positive = row[1:]
        elif row[0] == 'negative':
            auxiliary_verbs_negative = row[1:]

with open('adjectives_antonyms.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        adjectives_antonyms[row[0]] = [i for i in row[1:] if i != ""]

with open('adjectives_synonyms.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        adjectives_synonyms[row[0]] = [i for i in row[1:] if i != ""]


def getTokens(string):
    tokens = {
        "subject": "",
        "object": "",
        "verb": "",
        "adjective": "",
        "auxiliary_verb_positive": "",
        "auxiliary_verb_negative": "",
        "negative": 0,
        "positive": 0,
        "queryIsPositive": False
    }


    negative = 0
    positive = 0

    for word in string.split():
        if word not in adjectives and word not in auxiliary_verbs_positive and word not in auxiliary_verbs_negative and "'" + word + "'" not in str(verbs):
            if(tokens["subject"] == ""):
                tokens["subject"] = word
            else:
                tokens["object"] = word
        if word in adjectives:
            tokens["adjective"] = word
        if "'" + word + "'" in str(verbs):
            tokens["verb"] = word
        if word in auxiliary_verbs_positive:
            tokens["auxiliary_verb_positive"] = word
            positive+=1
        if word in auxiliary_verbs_negative:
            tokens["auxiliary_verb_negative"] = word
            negative+=1
        tokens["negative"] = negative
        tokens["positive"] = positive
        p = bool(tokens.get("auxiliary_verb_positive")) and positive > negative
        tokens["queryIsPositive"] = p
    return tokens



string = "Earth is ugly"
tokens = getTokens(string)


string1 = "Earth isn't adorable"
tokens1 = getTokens(string1)


if(tokens1.get("queryIsPositive")):
    print(tokens.get("adjective") in adjectives_synonyms.get(tokens1.get("adjective")) or tokens.get("adjective") == tokens1.get("adjective"))
else:
    print(tokens.get("adjective") in adjectives_antonyms.get(tokens1.get("adjective")) or tokens.get("adjective") != tokens1.get("adjective"))

