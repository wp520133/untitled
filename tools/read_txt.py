def read_txt(fileName):
    filepath = "C:/Users/17327/PycharmProjects/untitled/data/" + fileName
    arr = []
    with open(filepath, "r", encoding="utf-8") as file:
        datas = file.readlines()
        for data in datas:
            arr.append(tuple(data.strip().split(",")))
    return arr