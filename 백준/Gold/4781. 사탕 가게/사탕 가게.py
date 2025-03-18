import sys

input = sys.stdin.readline


dp = [0]*10002

while 1:
    n,m = input().split()
    n = int(n)
    m = float(m)
    m = int(m*100+0.5)
    if n==0 and m==0:
        break
    
    for i in range(m+2):
        dp[i]=0

    cal_list = []
    money_list = [] 
    for i in range(n):
        cal, money = input().split()
        cal = int(cal)
        money = float(money)
        money = int(money*100+0.5)

        cal_list.append(cal)
        money_list.append(money)


    for candy_idx in range(n):
        cal = cal_list[candy_idx]
        money = money_list[candy_idx]

        for i in range(m+1):
            if i>=money:
                dp[i] = max(dp[i],dp[i-money]+cal)
    
    print(dp[m])




