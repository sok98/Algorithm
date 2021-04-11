from collections import deque


def solution(begin, target, words):
    level = []
    visited = []
    queue = deque([begin])

    if target in words:
        # BFS
        while queue:
            print(level)
            n = queue.popleft()

            # 방문한 적 없을 때만 탐색
            if n not in visited:
                print("n --- ", n)

                # 목표에 도달
                if n == target:
                    return len(level)

                visited.append(n)
                # 한글자만 다른 단어 queue에 넣기
                collect = []
                for word in words:
                    count = 0
                    for i in range(len(n)):
                        if n[i] == word[i]:
                            count += 1
                    if count == len(n) - 1 and word not in visited:
                        collect.append(word)
                level.append(collect)
                queue.extend(collect)
                print(len(level))
    # words에 target이 없거나 도달할 방법이 없는 경우
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
