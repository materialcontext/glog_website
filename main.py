import json
from flask import Flask, render_template
# from flask_wtf import FlaskForm

app = Flask(__name__)


def load_rules():
    with open('static/json/core_rules.json', 'r') as file:
        return json.load(file)


def load_magic():
    with open('static/json/magic_rules.json', 'r') as file:
        return json.load(file)


rules = load_rules()
magic = load_magic()


def get_headings():
    output = {}
    for row in rules:
        section = rules[row]['Section']
        title = rules[row]['Title']
        subtitle = rules[row]['Subtitle']
        rule = rules[row]['Body'].replace('\n', '<br>')
        if section not in output:
            output[section] = {title: {subtitle: [rule]}}
        elif title not in output[section]:
            output[section][title] = {subtitle: [rule]}
        elif subtitle not in output[section][title]:
            output[section][title][subtitle] = [rule]
        else:
            output[section][title][subtitle].append(rule)

    for row in magic:
        section = magic[row]['Section']
        title = magic[row]['Title']
        subtitle = magic[row]['Subtitle']
        rule = magic[row]['Body'].replace('\n', '<br>')
        if section not in output:
            output[section] = {title: {subtitle: [rule]}}
        elif title not in output[section]:
            output[section][title] = {subtitle: [rule]}
        elif subtitle not in output[section][title]:
            output[section][title][subtitle] = [rule]
        else:
            output[section][title][subtitle].append(rule)

    return output


headings = get_headings()


@app.route('/')
def index():
    return render_template('index.html', headings=headings)


if __name__ == '__main__':
    app.run(debug=True)