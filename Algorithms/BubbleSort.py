# Murat KILCI
# 190403023
# 03.01.2022
def bubbleSort(_list):
    for i in range(1, len(_list)):
        for j in range(len(_list) - i):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    return _list
