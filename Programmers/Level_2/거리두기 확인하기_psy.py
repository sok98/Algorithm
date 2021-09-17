#[2021 카카오 채용 연계형 인턴십] 거리두기 확인하기
# 획득 포인트 7

def check(p):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(5):
        for y in range(5):
            if p[x][y] == "P": # P일 경우 -> 상하좌우 체크
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= 5 or ny >= 5: # 범위 체크
                        continue
                    if p[nx][ny] == "X": # 파티션이 있는경우 통과
                        continue
                    if p[nx][ny] == "P": # 주변에 또 응시자가 있는 경우 -> 맨해튼 거리 위반이므로 0 리턴
                        return 0
                    for i in range(4): # 상하좌우 노드의 상하좌우 체크
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                        if nnx == x and nny == y: # 시작 노드면 통과
                            continue
                        if nnx < 0 or nny < 0 or nnx >= 5 or nny >= 5:  # 범위 체크
                            continue
                        if p[nnx][nny] == "X":  # 파티션이 있는경우 통과
                            continue
                        if p[nnx][nny] == "P": # 주변에 또 응시자가 있는 경우 -> 맨해튼 거리 위반이므로 0 리턴
                            return 0

    # 모든 노드에 대체 대각선 노드의 체크를 마침 -> 맨해튼 거리 검증 -> 1 리턴                    
    return 1

def solution(places):
    answer = []
    for p in places:
        answer.append(check(p))
    return answer