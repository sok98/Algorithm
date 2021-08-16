import collections

def solution(bridge_length, weight, truck_weights):
    # 트럭 여러 대가 모두 다리를 건너는데 걸리는 최소 시간
    # 모든 트럭은 길이 1
    # 다리에 길이: bridge_length
    # 다리가 견디는 최대 무게: weight

    time = 0
    bridge = [0] * bridge_length
    # print(bridge)

    while(bridge):
        time += 1
        bridge.pop(0)
        # 다리에 새 트럭이 올라올 수 있다면
        # 대기 -> 다리
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    print(time)
    return time
        

solution(2, 10, [7, 4, 5, 6]) # 8
# solution(100, 100, [10]) # 101
# solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) # 110
