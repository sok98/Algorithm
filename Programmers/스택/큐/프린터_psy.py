import collections

def solution(priorities, location):
    first = max(priorities)
    # print("max", first)
    priorities = collections.deque(priorities)
    
    while(first != priorities[0]):
        # print(priorities)
        priorities.rotate(-1)
        
        if location>0:
            location-=1
        else:
            location=len(priorities)-1
        
    # print("location: ", location)
    return location+1