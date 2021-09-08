#not solved
def solution(begin, target, words):
    answer = 0 #depth
    stacks = [begin]
    visited = { i:0 for i in words} #이미 검사했던 단어를 다시 검사하지 않도록 하기 위한 딕셔너리
    if target not in words:
        return 0
    while stacks:
        stack = stacks.pop()
        if stack == target: #target이 리스트에 없으면 0 리턴
            return answer
        
        for word in words:
            for i in range(len(word)): 
                copy = list(word)
                copy_front = list(stack)
                copy[i] = 0
                copy_front[i]=0

                if copy == copy_front:
                    if visited[word] != 0:
                        continue
                    visited[word] = 1
                    stacks.append(word)
                    break
        answer += 1 #depth 1추가


    return answer
        