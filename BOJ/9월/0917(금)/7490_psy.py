# [gold-5] 7490 0 만들기
# algorithm 부루트포스, DFS
# 메모리:    29200 KB
# 시간:      160 ms
import sys
input = sys.stdin.readline

T = int(input())
result = []

def operator(now,ans):
    if now == n+1:
        calc(ans)
        return

    operator(now+1,ans+' '+str(now))
    operator(now+1,ans+'+'+str(now))
    operator(now+1,ans+'-'+str(now))

def calc(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        result.append(ans)

for _ in range(T):
  n = int(input())
  operator(2,'1') # N은 3부터
  result.append(' ')

print(*result, sep='\n')