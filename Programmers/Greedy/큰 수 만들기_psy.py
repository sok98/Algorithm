def solution(number, k):
    stack = [number[0]]
    for n in number[1:] :
        while stack and k > 0 and stack[-1] < n : 
            stack.pop()
            k -= 1
        stack.append(n)
    return ''.join(stack[:len(number)-k])

# 8, 10 시간초과
# def solution(number, k):
#     i, count = 0, 0

#     for _ in range(k):
#         for i in range(len(number)):
#             if i == len(number)-1:
#                 return number[:-(k-count)]
#             else:
#                 if int(number[i])<int(number[i+1]):
#                     number = number.replace(number[i], '', 1)
#                     count += 1
#                     break
            
#     if count <k:
#         number = number[:-(k-count)]
#     print("number", number)

#     return number

solution("1924", 2) # "94"
solution("1231234", 3) # "3234"
solution("4177252841", 4) # "775841"


