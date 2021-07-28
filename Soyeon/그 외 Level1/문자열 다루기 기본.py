def solution(s):
    if len(s)!=4 and len(s)!=4:
        return False
    
    try:
        number = int(s)
    except ValueError:
        return False
    
    return True

print(solution("a234")) # false
print(solution("1234")) # true
