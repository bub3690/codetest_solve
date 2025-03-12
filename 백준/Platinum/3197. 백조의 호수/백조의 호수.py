from collections import deque
import sys

input = sys.stdin.readline

R,C = tuple(map( int, input().split() ))
grid = [ list(input().strip()) for _ in range(R) ]


# def generate_example(grid):
#     R, C = 1500, 1500
#     # 기본 격자를 얼음('X')으로 초기화
#     grid = [['X'] * C for _ in range(R)]
    
#     # 가운데 세로줄을 물('.')로 변경
#     mid_col = C // 2
#     for i in range(R):
#         grid[i][mid_col] = '.'
    
#     # 가운데 가로줄을 물('.')로 변경
#     mid_row = R // 2
#     for j in range(C):
#         grid[mid_row][j] = '.'
    
#     # 백조 위치 지정: 왼쪽 상단과 오른쪽 하단에 배치
#     grid[0][0] = 'L'
#     grid[R-1][C-1] = 'L'
    
#     # 결과 출력 (첫 줄은 행과 열의 크기)
#     # print(f"{R} {C}")
#     # for row in grid:
#     #     print("".join(row))
#     return grid

# R,C =(1500,1500)
# grid = []
# grid=generate_example(grid)


dxs = [0,1,0,-1]
dys = [1,0,-1,0]


x=[0,0]
y=[0,0]
bird_cnt = 0


swan_que = deque()
swan_next_que = deque()

water_que = deque() # melt에서 사용

for i in range(R):
    for j in range(C):
        if grid[i][j]=='L':
            x[bird_cnt]=i
            y[bird_cnt]=j
            grid[i][j] = '.'
            bird_cnt += 1
        
        if grid[i][j]== '.':
            water_que.append( (i,j))


def range_check(x,y):
    return 0<=x<R and 0<=y<C


visit_swan = [[-1]*C for _ in range(R) ]

visit_swan[x[0]][y[0]] = 0

swan_que.append(( x[0],y[0] ))

melting_visited = [[-1]*C for _ in range(R)  ]


def swan_bfs():
    # target x를 찾는 과정
    while swan_que:
        now_x,now_y = swan_que.popleft()

        for i in range(4):
            next_x = now_x + dxs[i]
            next_y = now_y + dys[i]

            if range_check(next_x,next_y):
                
                if grid[next_x][next_y]=='.' and visit_swan[next_x][next_y] ==-1:
                   swan_que.append((next_x, next_y))
                   visit_swan[next_x][next_y] = visit_swan[now_x][now_y] + 1

                elif grid[next_x][next_y]=='X' and visit_swan[next_x][next_y] ==-1:
                   swan_next_que.append((next_x, next_y))
                   visit_swan[next_x][next_y] = visit_swan[now_x][now_y] + 1
    

    return visit_swan[x[1]][y[1]] != -1


def melting():
    
    water_next_que = deque()
    while water_que:
        now_x,now_y = water_que.popleft()
        melting_visited[now_x][now_y] = 1
        for i in range(4):
            next_x = now_x + dxs[i]
            next_y = now_y + dys[i]

            if range_check(next_x,next_y):
                if grid[next_x][next_y]=='X' and melting_visited[next_x][next_y] == -1:
                    grid[next_x][next_y] = '.'
                    water_next_que.append((next_x,next_y))
                    melting_visited[next_x][next_y] = 1
    
    return water_next_que



count = 0
while True:
    if swan_bfs() :
        break
    

    swan_que = swan_next_que
    swan_next_que = deque() # 새로운 변수를 덮어씌우면 추적이 안된다.

    water_que = melting()
    count += 1    



print(count)

