rock = ""
for _ in range(5):
    rock+="o"

# print(rock)

# print(str(True or False))
# print(True or False)

#dic ={"A": {1:[0, 1, 3]}, "B": {1: [2, 4]}}

dic = {}
# innerDic = {}
# innerDic[1]=[0, 1, 3]
# innerDic[2]=[2, 4]
# for value in dic.items():
#     dic.value = {}
dic["A"] = {}
dic["B"] = {}
dic['A'][1] = [0, 1, 3] #innerDic[0]
dic['B'][1] = [2, 4] #innerDic[1]
print("dic=", dic)
