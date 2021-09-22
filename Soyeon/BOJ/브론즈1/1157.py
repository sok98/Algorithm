# 단어 공부

from collections import defaultdict
cList = list(input())

freqWord = []
max = 0
cDic = defaultdict(int)

for c in cList:
    cDic[c.upper()] += 1


for key, value in cDic.items():
    if value > max:
        freqWord = []
        freqWord.append(key)
        max = value
    elif value == max:
        freqWord.append(key)


if len(freqWord)>1:
    print('?')
else:
    print(freqWord[0])
