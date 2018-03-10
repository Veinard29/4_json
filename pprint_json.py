import json
import requests


def load_data(filepath):
    get_file = requests.get(filepath)
    return get_file.json()


def pretty_print_json(json_file):
    return print(json.dumps(json_file, skipkeys=True, ensure_ascii=False, sort_keys=True, indent=2, separators=(',', ': ')))



if __name__ == '__main__':
    file_input = input()
    load_file = load_data(file_input)
    print_file = pretty_print_json(load_file)


