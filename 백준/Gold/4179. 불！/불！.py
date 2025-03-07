import sys
from collections import deque


R,C = map(int,input().split())
grid = []

INF=9999999
map_data = {
    '#': -1,
    'J': 1,
    'F': 1,
    '.': INF
}

grid = [ list(input()) for _ in range(R) ]

person_grid = []

fire_list = [] # (x,y) 
j_pos = (0,0) # 이 초기값 덕분에 j나 f가 없어도 작동함.

for i in range(R):
    for j in range(C):
        
        if grid[i][j] =='J':
            j_pos = (i,j)
        elif grid[i][j]=='F':
            fire_list.append((i,j))
        grid[i][j]=map_data[grid[i][j]]

person_grid  = [ row[:] for row in grid ]
#print(person_grid)

def range_check(x,y):
    return x>=0 and x<R and y>=0 and y<C

dx=[0,1,0,-1]
dy=[1,0,-1,0]


def bfs_fire():
    que=deque(fire_list)
    #que.append((x,y))
    while que:
        n_x,n_y = que.popleft()
        
        for i in range(4):
            next_x = n_x + dx[i]
            next_y = n_y + dy[i]

            if range_check(next_x,next_y) and grid[next_x][next_y]==INF:
                que.append((next_x,next_y))
                grid[next_x][next_y] = grid[n_x][n_y] + 1
    
    return


def bfs_j(x,y):
    que=deque()
    que.append((x,y))
    while que:
        n_x,n_y = que.popleft()
        
        #print(n_x,n_y, person_grid[n_x][n_y])
        ###
        # 가장 자리 체크
        if (n_x==0) or (n_y==0) or (n_x==R-1) or (n_y==C-1):
            return person_grid[n_x][n_y]

        ###


        for i in range(4):
            next_x = n_x + dx[i]
            next_y = n_y + dy[i]


            if range_check(next_x,next_y) and person_grid[next_x][next_y]==INF and (grid[next_x][next_y] > person_grid[n_x][n_y] + 1) :
                que.append((next_x,next_y))
                person_grid[next_x][next_y] = person_grid[n_x][n_y] + 1
    
    return -1


# 불 bfs. 이게 맞을까?. min하게 먼저 도착하면 덮어 씌워줘야할까?
# 혹시나 불이 여럿일수도 있으니 코딩 스타일.
# 틀렸다. 멀티소스 BFS 방식으로 되야한다고 한다.
for fire in fire_list:
    x, y = fire
    bfs_fire()


person_grid[j_pos[0]][j_pos[1]] = 1
answer = bfs_j(j_pos[0],j_pos[1])


if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer)










