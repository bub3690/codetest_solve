import sys

sys.setrecursionlimit(100000)


T,W = tuple(map(int, input().split() ))
grid = [0]*(T+1)
for i in range(1,T+1):
    grid[i] = int(input())



dp = [ [  [-1]*(W+1) for _ in range(3)  ]  for _ in range(T+2)]


def go(time,here,w):
    # 1초 부터 선택.

    count = 0
    if grid[time]==here:
        count = 1
    else:
        count = 0
    

    if time == T:
        if grid[T-1]==here:
            # dp 해주기.
            dp[time][here][w] = count
            return count
        else:
            dp[time][here][w] = count
            return count

    # 메모라이제이션 불러오기
    if dp[time][here][w] != -1:
        return dp[time][here][w]
    

    #갈것인가 안갈것인가
    
    # 1과2 뒤집기.
    next_tree = here
    go1=go(time+1,next_tree,w)
    if here == 1:
        next_tree=2
    else:
        next_tree=1
    go2= 0
    if w>0:
        go2=go(time+1,next_tree,w-1)

    
    count += max(go1,go2)
    dp[time][here][w] = count
    return count


go(0,1,W)


print(dp[0][1][W])


