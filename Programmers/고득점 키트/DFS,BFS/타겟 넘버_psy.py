def solution(numbers, target):
    answer = 0

    def dfs(idx, total):
        if len(numbers) == idx:
            if total == target:
                nonlocal answer
                answer += 1
        else:
            SUM = total + numbers[idx]
            SUB = total - numbers[idx]

            dfs(idx+1, SUM)
            dfs(idx+1, SUB)

    dfs(0,0)


    return answer