def read_txt(fileName):
    filepath = "../data/" + fileName
    arr = []
    with open(filepath, "r", encoding="utf-8") as file:
        datas = file.readlines()
        for data in datas:
            arr.append(tuple(data.strip().split(",")))
    return arr
