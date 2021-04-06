import math

test_size=int(input(""))
for i in range(test_size):
    x, y = map(int, input().split())
    sqrt_length = math.sqrt(y-x)
    count = int(sqrt_length)*2
    if int(sqrt_length) == sqrt_length: #제곱 수 일 때
        count-=1

    #제곱수, 제곱수의 중앙 (9, 5)에서 count
    elif y-x>(math.pow(int(sqrt_length),2) + math.pow(int(sqrt_length)+1,2))/2:
        count+=1
    print(count)

# Other solution

# import math

# for tc in range(int(input())):
#     x, y = map(int, input().split())
#     dist = y - x  # 두 점 사이의 거리
#     my_sqrt = int(math.sqrt(dist))  # 제곱근
#     nmg = dist - my_sqrt ** 2  # 제곱까지 빼고 나머지
#     cnt = my_sqrt * 2 - 1  # 제곱근 일때의 이동횟수
#     if nmg == 0:
#         print(cnt)
#     elif nmg <= my_sqrt:
#         print(cnt + 1)
#     else:
#         print(cnt + 2)