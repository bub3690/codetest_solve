import sys

sys.setrecursionlimit(10000)




dp = [ [0]*31 for _ in range(31)  ]

def go(here):
    now_one, now_half = here

    if now_one == 0 and now_half ==1 :
        return 1

    if dp[now_one][now_half]:
        return dp[now_one][now_half]
    
    sum1 =0
    sum2 =0

    if now_half >0:
        sum1 = go((now_one, now_half-1) )
    if now_one >0:
        sum2 = go((now_one-1, now_half+1) )

    dp[now_one][now_half] = sum1+sum2
    return dp[now_one][now_half]



while 1:
    N = int(input())
    
    if N == 0:
        break
    
    for i in range(N+1):
        for j in range(N+1):
            dp[i][j]=0

    go((N,0))
    print(dp[N][0])




    








