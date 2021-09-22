def solution(citations):
    # 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지는 h번 이하 인용되었다면 h의 최댓값
    # 논문의 인용 횟수를 담은 배열 = citations

    # citations를 정렬 후 중앙 인덱스 기준으로 
    citations.sort(reverse = True)
    print(citations)

    if min(citations) >= len(citations):
        print("h index=", len(citations))
        return len(citations)

    # H-index의 min, max는 각각 citations의 min, max
    for i in range(citations[0], citations[-1]-1, -1):
        count=0
        for j in range(len(citations)):
            if citations[j] >= i:
                count += 1
        
        if count>=i and (len(citations)-count)<=i:
            print("h index=", i)
            return i

# solution([3, 0, 6, 1, 5]) # 3
# solution([1, 3, 5, 7, 9, 11]) # 4
# solution([0, 0, 0, 0, 1]) # 0 <= 테케 16
# solution([5, 5, 5, 5, 5]) # 5
# solution([22, 42]) # 2 <= 테케 9

