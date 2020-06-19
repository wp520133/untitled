import json


def read_json(fileName):
    filepath = "../data/" + fileName
    arr = []
    with open(filepath, "r", encoding="utf-8") as file:
        datas = json.load(file)
        for data in datas.values():
            arr.append((data['username'], data['password'], data['captcha_code'],data['success']))
    return arr
