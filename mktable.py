import json
import random

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

