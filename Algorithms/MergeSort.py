# Murat KILCI
# 190403023
# 03.01.2022

from Algorithms.InsertionSort import insertionSort

def mergeSort(_list):
    middle = int(len(_list) / 2)
    firstList = _list[:middle]
    secondList = _list[middle:]
    resultList = []

    sortedFirstList = insertionSort(firstList)
    sortedSecondList = insertionSort(secondList)

    i = 0
    j = 0
    k = 0

    while i < len(sortedFirstList) and j < len(sortedSecondList):
        if sortedFirstList[i] < sortedSecondList[j]:
            resultList.append(sortedFirstList[i])
            i += 1
        else:
            resultList.append(sortedSecondList[j])
            j += 1
        k += 1

    while i < len(sortedFirstList):
        resultList.append(sortedFirstList[i])
        i += 1
        k += 1

    while j < len(sortedSecondList):
        resultList.append(sortedSecondList[j])
        j += 1
        k += 1

    return resultList
