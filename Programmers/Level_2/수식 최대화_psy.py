#[2020 카카오 인턴십] 수식 최대화
# 획득 포인트 4
# O(N**3)

from itertools import permutations

def solution(expression):
    operators = ['+', '*', '-']
    answer = []
    
    for op in permutations(operators, 3):
        tmp_exp = [''] # 계산 식 -> 결과값 리스트
        
        # 숫자 연산자 분리해서 리스트에 자장
        for exp in expression:
            if exp.isdigit() and tmp_exp[-1] not in operators: # 숫자이고 현재 식의 마지막이 연산자가 아니라면
                tmp_exp[-1] += exp # 숫자 잇기
            else: 
                tmp_exp.append(exp)
        
        # 연산자의 인덱스 위치를 기준으로 우선적으로 계산
        for i in op:
            while i in tmp_exp:
                idx = tmp_exp.index(i)
                tmp_exp = tmp_exp[:idx-1]+[str(eval("".join(tmp_exp[idx-1:idx+2])))]+tmp_exp[idx+2:]
        answer.append(abs(int(tmp_exp[0])))
        
    return max(answer)