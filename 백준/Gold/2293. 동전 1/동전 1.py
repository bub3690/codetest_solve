import sys
N,K = tuple(map(int,input().split() ))

coin_list=[]
dp = [0]*(K+1)
for i in range(N):
    coin_list.append(int(input()))

coin_list.sort()

dp[0]=1
for coin in coin_list:
    for i in range(K+1):
             if i>= coin:
                dp[i] += dp[i-coin]

print(dp[K])







