import csv
import json


rules_dict = {}


def csv_to_dict():
    with open('static/magic-book.csv', 'r', encoding='utf-8-sig') as file:
        i = 0
        output = csv.DictReader(file)
        for row in output:
            rules_dict[i] = row
            i += 1


def dict_to_json():
    with open('static/json/magic_rules.json', 'w') as file:
        json.dump(rules_dict, file)


csv_to_dict()
dict_to_json()
