import json

def coor_check(coor,table):
    stu_coor = [[point["coordinate"] for point in sublist] for sublist in table]
    for i in stu_coor:
        for j in i:
            x2 = (coor[0] - j[0])^2
            y2 = (coor[1] - j[1])^2
            table[i][j]["dis"] = (x2+y2) #tableに判定座標からの距離の二乗を保存
    min_distance = float('inf')  # 初期値として無限大を設定
    min_name = ""

    for sublist in table:
        for point in sublist:
            if "dis" in point and point["dis"] < min_distance:
                min_distance = point["dis"]
                min_name = point["name"]

    return min_name


