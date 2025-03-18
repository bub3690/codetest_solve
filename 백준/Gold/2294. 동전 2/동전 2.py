import sys

N,K = tuple(map(int,input().split() ))

coin_list=[]
dp = [sys.maxsize]*(K+1)
for i in range(N):
    coin_list.append(int(input()))

# 중요한 반례. 동전은 꼭 정렬된 채로 와야한다!!!!
coin_list.sort()

dp[0] = 0
for i in range(K+1):
    for j in coin_list:
        if j<=i:
            dp[i] = min(dp[i-j]+1,dp[i])

# 또 틀린 반례.
# 불가능하면 -1 이 되야함.
if dp[K] == sys.maxsize:
    print(-1)
else:
    print( dp[K] )


