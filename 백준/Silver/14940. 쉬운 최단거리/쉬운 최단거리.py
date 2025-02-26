import sys
from collections import deque


n,m = map(int,input().split())

grid = [ list(map(int,input().split())) for _ in range(n)]


# 먼저 목표지점 2찾기. 그리고 그자리는 1로 두기.
find_x = 0
find_y = 0 
found = False
for i in range(n):
    
    for j in range(m):
        if grid[i][j]==2:
            find_x =i
            find_y =j
            found= True
            break
    if found:
        break





# 출발점에서 모든 지점 최단 거리.
# bfs 이용시 처음 도착이 항상 최단거리가 된다. 모두 같은 깊이로 탐색되서.

dx= [0,1,0,-1]
dy= [1,0,-1,0]


def range_check(x,y):
    return x>=0 and x< n and y>=0 and y< m



def bfs(x,y):
    # x,y 목표지점.
    que = deque()
    que.append((x,y))
    
    while que:
        x,y = que.popleft()   
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]

            if range_check(nx,ny) and grid[nx][ny]==1:
                grid[nx][ny] = grid[x][y] +1 # 이전 방문지에서 +1 만큼 더하면 거리가 됨.
                # 처음 방문시 최소값이라 grid을 올려서 방문 못하게함.
                # 방문을 했다면 이제 queue에 추가.
                que.append((nx,ny))


    
bfs(find_x,find_y)


###
#이건 풀이방법에 따른 차이로. 시작점 x,y 부분은 다시 0으로 넣어준다.
 

###


for i in range(n):
    for j in range(m):
        if grid[i][j] !=0:
            grid[i][j] =grid[i][j]-2
        print(grid[i][j],end=' ')
    print()







