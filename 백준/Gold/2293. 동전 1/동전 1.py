import sys
sys.setrecursionlimit(100000)

N,K = tuple(map(int,input().split() ))

coin_list=[]
dp = [[-1]*(K+1) for _ in range(N+1) ] # 코인, 남은돈
for i in range(N):
    coin_list.append(int(input()))

coin_list.sort()

def solve(coin_id,remain):
    
    # 기저가 두개.
    if remain==0:
        return 1
    
    if coin_id ==N or remain < 0:
        return 0
    
    #메모
    if dp[coin_id][remain] != -1:
        return dp[coin_id][remain] 

    dp[coin_id][remain] = solve(coin_id,remain-coin_list[coin_id])+solve(coin_id+1,remain)
    return dp[coin_id][remain]


solve(0,K) #coin idx, remain

print(dp[0][K])




