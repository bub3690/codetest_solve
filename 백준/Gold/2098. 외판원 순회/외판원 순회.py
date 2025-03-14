import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline
N = int(input())
grid = [ list(map(int,input().split())) for _ in range(N)]


visit = []

dp = [[-1]*20 for _ in range(1<<N)]  # dp[몇번째][어떤 노드인지]
# dp는 답범위를 최대한 벗어나게 해야함.

full_count = (1<<N) -1


def go(here,visited):
    global answer

    # 리프 만들기 == 기저
    if visited==full_count:
        # 종료.
        # 마지막 복귀 비용 계산
        if grid[here][0] >0:
            dp[visited][here] =  grid[here][0]
        else:
            dp[visited][here] = sys.maxsize
        return dp[visited][here] ### 여기서 실수. grid 자체가 0일수도 있다.
    
    #메모라이제이션
    if dp[visited][here] != -1:
        return dp[visited][here]

    #로직
    ret = sys.maxsize
    for i in range(N): # 0,1,2,3
        if not( visited & (1<<i) ) and grid[here][i] > 0: #i가 될수도 있고 아니기도 하고.
            next_visited = visited | (1 << i)
            result=go(i,next_visited)
            now_cost = result + grid[here][i]
            ret = min(now_cost,ret)
    
    dp[visited][here] = ret

    return ret

    

print(go(0, 1))
#print(dp)





