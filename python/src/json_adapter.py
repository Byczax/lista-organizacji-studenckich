import json


def save_to_file(name, data):
    with open(name, 'w') as f:
        json.dump(data, f)


def read_file(name):
    with open(name, 'r') as f:
        return json.load(f)


def file_exists(name):
    try:
        f = open(name, "r")
        f.close()
        return True
    except FileNotFoundError:
        return False
