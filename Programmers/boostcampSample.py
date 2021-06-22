def doubleNumCheck(numList):
    countArray = []
    countDic = {}

    for i in numList:
        if i in countDic:
            countDic[i] +=1
        else:
            countDic[i] = 1
    
    for value in countDic.values():
        if value > 1:
            countArray.append(value)


    if len(countArray)<1:
        countArray.append(-1)

    print(countArray)

arr = [1, 2, 3, 3, 3, 3, 4, 4]
print("arr = ", arr)
print("answer = ")
doubleNumCheck(arr)

arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
print("arr = ", arr)
print("answer = ")
doubleNumCheck(arr)

arr = [3, 5, 7, 9, 1]
print("arr = ", arr)
print("answer = ")
doubleNumCheck(arr)