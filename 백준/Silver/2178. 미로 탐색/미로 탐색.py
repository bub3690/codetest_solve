import sys
from collections import deque

sys.setrecursionlimit(1000000)


N,M= tuple(map(int,input().split()))

grid = [ list(map(int,input())) for _ in range(N) ]



# 0,0 to n-1, m-1 까지 가기.
# 최소 거리 기록하기.
# 최소 거리이기에 

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def range_check(x,y):
    return x>=0 and x<N and y>=0 and y<M

def bfs(x,y):
    que = deque()
    # visit 없이
    que.append((x,y))
    while que:
        x,y = que.popleft()
    
        #4방향 체크
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if range_check(nx,ny) and grid[nx][ny]==1:
                # visit 배열은 없으니까. 1인 경우만 처리한다는 의미로 ==1 추가됨.
                # 그리고 가장먼저 도착한 경우만 남게 된다.
                grid[nx][ny] = grid[x][y] + 1
                que.append((nx,ny))
                      
            
    
    return grid[N-1][M-1]


print(bfs(0,0))










