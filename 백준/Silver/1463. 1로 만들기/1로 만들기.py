import sys

#sys.setrecursionlimit(2000000)



N= int(input())


dp = [sys.maxsize]*(10**6+2) # 128mb보다 큰가?
#dp = {}


dp[0] =0
dp[1] = 0

#초기화.

for i in range(2,N+1):

        if(i%3==0):dp[i] = min(dp[i//3] +1, dp[i])
        if(i%2==0):dp[i] = min(dp[i//2] +1, dp[i])
        dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[N])


