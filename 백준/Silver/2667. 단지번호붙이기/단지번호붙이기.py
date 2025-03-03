from collections import deque



N = int(input())

grid = [ list(map(int,input())) for _ in range(N) ]

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def range_check(x,y):
    return x>=0 and x<N and y>=0 and y<N


check_grid = [[0]*N for _ in range(N)]


def bfs(pos):
    x,y=pos
    check_grid[x][y] = 1    
    count = 0
    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        count+=1

        #주변 탐색.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if range_check(nx,ny) and grid[nx][ny]==1 and check_grid[nx][ny] != 1 :
                que.append((nx,ny))
                check_grid[nx][ny] = 1                # 바로 해줘야함.

    return count




danji_list = []
for i in range(N):
    for j in range(N):
        if check_grid[i][j] != 1 and grid[i][j]==1:
            house_count=bfs((i,j))
            danji_list.append(house_count)
        
print(len(danji_list))
danji_list.sort()
for v in danji_list:
    print(v)



