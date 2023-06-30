import json
import random
info = {
    # 座席表
    "table": [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ],
    # その他情報
    "class": "1-1",
    "num": 30

}
coordinates = [(1.0, 1.0), (2.1, 0.9), (2.9, 1.1), (1.1, 2.1),
               (2.0, 1.9), (3.1, 2.0), (0.9, 2.9), (1.9, 3.0), (3.0, 3.1)]


def mktable(coordinates0, info):
    xlen = len(info["table"][0])
    ylen = len(info["table"])
    coordinates = random.sample(coordinates0,len(coordinates0))
    table = [[] for _ in range(ylen)]
    print(json.dumps(table))
    sorted_coordinates = sorted(coordinates, key=lambda coord: coord[0])
    for i in range(0, xlen):
        row = sorted_coordinates[i*ylen:(i+1)*ylen]
        sorted_row = sorted(row, key=lambda coord: coord[1])
        for j in range(0, ylen):
            table[j].append(
                {
                    "name": info["table"][j][i],
                    "coordinate": sorted_row[j]
                }
            )
    print(table)
    print(json.dumps(table))


mktable(coordinates, info)
