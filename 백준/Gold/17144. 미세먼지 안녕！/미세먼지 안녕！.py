import sys

input = sys.stdin.readline

R,C,T = tuple(map( int,input().split() ))

grid = [ list(map(int,input().split())) for _ in range(R)]
grid_temp = [ [0]*C for _ in range(R)]

# find head, leg
head =-1
tail =-1
for i in range(R):
    for j in range(C):
        if head==-1 and grid[i][j] ==-1:
            head = (i,j)
        elif head!=-1 and tail==-1 and grid[i][j]==-1:
            tail = (i,j)


dxs =[0,1,0,-1]
dys =[1,0,-1,0]

def check_range(x,y):
    return 0<=x<R and 0<=y<C


def spread():
    for i in range(R):
        for j in range(C):
            temp =0
            if grid[i][j] == -1:
                continue
            
            for dir in range(4):
                now_x = i + dxs[dir]
                now_y = j + dys[dir]
                if check_range(now_x,now_y) and grid[now_x][now_y]!=-1:
                    grid_temp[now_x][now_y] += grid[i][j]//5
                    temp += grid[i][j]//5
            grid_temp[i][j] += grid[i][j]
            grid_temp[i][j] -= temp


def push():
    #HEAD 부분
    # 시작만 잘해도 temp는 없어도 됨.
    #아래줄
    start_point = [head[0],head[1]]
    #왼세로
    for row in range(start_point[0]-1,-1,-1):
        if grid[row+1][start_point[1]]==-1:
            continue
        grid[row+1][start_point[1]]= grid[row][start_point[1]]
    #위가로
    for col in range(1,C):
        grid[0][col-1] = grid[0][col]
    
    #우세로
    for row in range(1,start_point[0]+1):
        grid[row-1][C-1] = grid[row][C-1]

    #아래가로
    for col in range(C-2,start_point[1],-1):
        grid[start_point[0]][col+1] = grid[start_point[0]][col]
    grid[start_point[0]][start_point[1]+1]=0
    

    ##tail 부분
    start_point = [tail[0],tail[1]]

    #왼 세로
    for row in range(start_point[0],R):
        if grid[row-1][start_point[1]] ==-1:
            continue        
        grid[row-1][start_point[1]]= grid[row][start_point[1]]

    #아래가로
    for col in range(1,C):
        grid[R-1][col-1] = grid[R-1][col]    

    #우세로
    for row in range(R-2,start_point[0]-1,-1):
        grid[row+1][C-1] = grid[row][C-1] 

    #위가로
    for col in range(C-2,start_point[1],-1):
        grid[start_point[0]][col+1] = grid[start_point[0]][col]
    grid[start_point[0]][start_point[1]+1]=0





    
ans = 0
for t in range(T):
    spread()
    for i in range(R):
        for j in range(C):
            if grid[i][j] == -1:
                continue
            grid[i][j]=grid_temp[i][j]

    push()
    for i in range(R):
        for j in range(C):
            grid_temp[i][j]=0





for i in range(R):
    for j in range(C):
        ans += grid[i][j]

ans +=2
print(ans)

