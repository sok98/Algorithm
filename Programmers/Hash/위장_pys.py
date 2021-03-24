def solution(clothes):
    types = []
    nums = []
    for i in clothes:
        flag = True
        for j, v in enumerate(types):
            if i[1]==v:
                nums[j] += 1
                flag = False
        if flag:
            types.append(i[1])
            nums.append(1)
    ans = 1
    for i in nums:
        ans *= (i+1)
    return ans-1

# def solution(clothes):
#     answer = 1
#     kind = dict()

#     for cloth in clothes:
#         if(cloth[1] not in kind.keys()):
#             kind[cloth[1]] = 1
#         else:
#             kind[cloth[1]] += 1

#     kindCount = list(kind.values())

#     for kc in kindCount:
#         answer = answer * (kc+1)

#     return answer-1