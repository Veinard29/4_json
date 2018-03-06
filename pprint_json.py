import json
import requests


def load_data(filepath):
     f = requests.get(filepath)
     return f.json()


def pretty_print_json(data):
    return print(json.dumps(data, skipkeys=True, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': ')))



if __name__ == '__main__':
    f = input()
    c = load_data(f)
    b = pretty_print_json(c)
