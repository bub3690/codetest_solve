
from collections import deque

N,M = tuple(map(int,input().split()))

# 3 4 , 1 2
# 주난 범인
x_j,y_j, x_t,y_t = tuple(map(int,input().split() ))
x_j -= 1
y_j -= 1
x_t -=1
y_t -=1



grid = [ list(input()) for _ in range(N) ]
visit = [ [-1]*M for _ in range(N) ]

grid[x_j][y_j] = '0'
grid[x_t][y_t] = '1'


dxs= [0,1,0,-1]
dys= [1,0,-1,0]


def range_check(x,y):
    return 0<=x<N and 0<=y<M


    
    

def bfs(pos_j):
    global grid
    global visit

    que = deque()
    x,y = pos_j
    que.append((x,y))

    while que:
        n_x,n_y = que.popleft()
        for i in range(4):
            next_x = n_x + dxs[i]
            next_y = n_y + dys[i]
            
            if range_check(next_x,next_y):
                if visit[next_x][next_y] == -1:
                    # 순서가 1이먼저 해줘야하는데.. 

                    if grid[next_x][next_y] =='0' and grid[n_x][n_y] =='0':
                        visit[next_x][next_y] = visit[n_x][n_y]
                        grid[next_x][next_y] = '0'
                        que.appendleft( (next_x,next_y) )
                    else:                
                        visit[next_x][next_y] = visit[n_x][n_y] +1
                        grid[next_x][next_y] = '0'
                        que.append((next_x,next_y))

                    



visit[x_j][y_j] = 0


bfs((x_j,y_j))


print(visit[x_t][y_t])







