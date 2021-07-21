import collections

def solution(priorities, location):
    priorities = collections.deque(priorities)
    count=0

    while(priorities):

        # 가장 큰 수
        pNum = max(priorities)

        # 현재 인덱스의 수가 가장 큰 수라면
        if pNum == priorities[0]:
            count+=1
            
            # 찾으려는 인덱스를 pop
            if location == 0:
                # print("answer", count) 
                return count
 
            priorities.popleft()

        # 가장 큰 수가 맨 앞에 올 때 까지 큐 회전
        else:
            priorities.rotate(-1)
        
        location -=1
        if (location<0):
            location += len(priorities)


# solution([2, 1, 3, 2], 2) # 1
# solution([1, 1, 9, 1, 1, 1], 0) # 5
# solution([2, 1, 9, 1, 9, 1], 1) # 4