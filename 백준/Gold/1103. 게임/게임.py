import sys
sys.setrecursionlimit(100000)


N, M = tuple(map(int,input().split() ))


grid = [ list(input().strip()) for _ in range(N) ]

dp = [ [0]*(M+1) for _ in range(N+1)]
visited = [ [False]*(M+1) for _ in range(N+1)]

def check_range(x,y):
    return 0<=x<N and 0<=y<M

dxs= [0,1,0,-1]
dys= [1,0,-1,0]

detect_cycle = False
def go(now_x,now_y):
    global detect_cycle

    
    if not check_range(now_x,now_y):
        # 문제는.. 여기서 메모라이제이션은 못한다. 범위가 밖이면 기록을 못하니까.
        # 또는 범위가 밖일때 나가지기.
        return 0
    
    if grid[now_x][now_y] == 'H':
        return 0
    
    if dp[now_x][now_y] != 0:
        return dp[now_x][now_y]
    
    max_val = 0

    for i in range(4):
        next_x = now_x + dxs[i] * int(grid[now_x][now_y])
        next_y = now_y + dys[i] * int(grid[now_x][now_y])
        # cycle 발견시.
        
        if check_range(next_x,next_y) and visited[next_x][next_y]:
            detect_cycle = True
            print(-1)
            exit(0)
            return -1
        
        if check_range(next_x,next_y):
            visited[next_x][next_y] = True

        now_val=go(next_x,next_y)+1

        if check_range(next_x,next_y):
            visited[next_x][next_y] = False

        max_val = max(max_val,now_val)

    dp[now_x][now_y] = max_val

    return dp[now_x][now_y]


visited[0][0] = True
go(0,0)
visited[0][0] = False

if detect_cycle:
    print(-1)
else:
    print(dp[0][0])










