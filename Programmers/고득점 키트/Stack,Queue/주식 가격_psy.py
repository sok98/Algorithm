# 최악: N^2
# 최선: 2N

def solution(prices):
    # 가격이 떨어지는 시점
    dropPrice = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    sPrice = [0]
    
    for i in range(1, len(prices)):
        while sPrice:
            index = sPrice[-1]
            
            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                dropPrice[index] = i - index
                sPrice.pop()
            
            # 떨어지지 않음 => 주식 가격이 계속 증가 중 말)
            else:
                break
        
        # 스택에 추가
        sPrice.append(i)
    print(dropPrice)
    return dropPrice

solution([1, 2, 3, 2, 3])