def solution(a, b):
    answer = 0
    tmp = 0
    
    if a>b:
        tmp =a
        a= b
        b=tmp
    
    for i in range(a, b+1):
        answer += i
        
    return answer

nList = ["3000", "300","30"]

# if set(list(permute[0])) - set(list(permute[1])) == '0'


if '500'.rstrip('0') == '50'.rstrip('0'):
    print("와 이게 되네")

print("set", set(nList))