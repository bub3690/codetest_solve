
# 입력
# n:격자크기,m: 참가자 수,k:게임시간.
# 4<=N<=10
# 1<=M<=10
# 1<=K<=100
# m줄의 참가자 위치 -> 1부터 시작
# 마지막 줄 출구 위치

#요구사항
# 최단거리 - 멘허튼
# 참가자
# 1초마다 움직임. 상하좌우. 벽으로 못감
# 움직인 칸은 현재칸보다 최단 거리가 가까움**
# 상하 우선
# 안 움직일수도 있음.
# 겹칠 수 있음.

# 미로 회전
# 한명이상 참가자, 출구를 포함 가장 작은 정사각형 잡기.
# -> 같은 사이즈가 있다면. r좌표가 작은것이 우선. (가장 작은게 하나 잡히면 바로 보기.)
# 90도로 회전하고, 내부 벽이 1씩 깎임.
# K초 동안 진행. 모든참가자가 탈출시 끝. 게임 끝날시, 이동거리합과 출구좌표 출력.

#시간 1초

#알고리즘
#BFS, 회전, 완탐
# O(k*n^2*m*n) ->k*n^4 -> 10^6

#풀이방법
# 모두 이동 -> BFS 배열와 맨허튼 거리 비교를 통해 결정
# 부분 회전 -> 완탐을 통해 정사각형을 하나씩 만든다. N^4

# 격자에는 참가자를 안두고, 벽만.
# 출구도 따로 기록

from collections import deque

N,M,K = tuple(map(int,input().split()))

grid = [ list(map(int,input().split())) for _ in range(N)]

man_list= [ list(map(int,input().split())) for _ in range(M)]
out_pos = list(map(int,input().split()))

# 1씩줄이기
for i in range(M):
    man_list[i][0] -= 1
    man_list[i][1] -= 1
out_pos[0] -= 1
out_pos[1] -= 1


visit = [ [0]*N for i in range(N) ]
step = [ [0]*N for i in range(N) ]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def range_check(x,y):
    return 0<=x<N and 0<=y<N

def move_all():
    bfs(out_pos[0],out_pos[1]) # 경로 기록
    mv_player_all = 0
    for chr_idx in range(M):
        mv_player_all += move(chr_idx)
    
    return mv_player_all


def get_distance(sx,sy,tx,ty):
    
    dist_x = abs(sx-tx)
    dist_y = abs(sy-ty)

    return dist_x+dist_y 
    

def move(idx):
    global man_list
    # step 배열을 통해 갈 수 있는 위치 선정
    nx,ny = man_list[idx][0],man_list[idx][1]
    dist = get_distance(nx,ny,out_pos[0],out_pos[1])
    
    confirmed_x= nx
    confirmed_y= ny

    for i in range(4):
        next_x = nx+dxs[i]
        next_y = ny+dys[i]
        next_dist = get_distance(next_x,next_y,out_pos[0],out_pos[1])
        if range_check(next_x,next_y) and visit[next_x][next_y] and next_dist<dist:
            dist = next_dist
            confirmed_x = next_x
            confirmed_y = next_y

    move_size = 0
    if confirmed_x !=nx or confirmed_y!=ny:
        move_size =1

    #수정
    man_list[idx][0] = confirmed_x
    man_list[idx][1] = confirmed_y


    return move_size



def bfs(t_x,t_y):
    
    for i in range(N):
        for j in range(N):
            visit[i][j] = 0
            step[i][j] = 0
    
    que = deque()
    que.append((t_x,t_y))
    visit[t_x][t_y] = True
    
    while que:
        nx,ny=que.popleft()
        for i in range(4):
            next_x = nx+dxs[i]
            next_y = ny+dys[i]
            if range_check(next_x,next_y) and not visit[next_x][next_y] and grid[next_x][next_y]==0:
                visit[next_x][next_y]= True
                step[next_x][next_y]= step[nx][ny] +1
                que.append((next_x,next_y))

    return



def rotate():
    size,s_x,s_y = find_square()
    #print(size,s_x,s_y)

    # 90도 회전
    # 만약 포함된다면
    for idx in range(M):
        px,py = man_list[idx][0],man_list[idx][1]
        if s_x<=px<=size+s_x-1 and s_y<=py<=size+s_y-1:
            temp_px = px -s_x
            temp_py = py -s_y
            px = s_x+temp_py # 
            py = s_y+size-temp_px-1 # 3-0-1
            man_list[idx][0] = px
            man_list[idx][1] = py
    #출구
    temp_tx = out_pos[0]-s_x#2
    temp_ty = out_pos[1]-s_y#0
    tx = s_x+ temp_ty # 
    ty = s_y+ size-temp_tx-1 # 2-2-1
    out_pos[0]=tx
    out_pos[1]=ty

    temp_arr = [[0]*N for i in range(N)]
    
    for i in range(size):
        for j in range(size):
            temp_arr[s_x+j][s_y+size-i-1] = grid[s_x+i][s_y+j]

    for i in range(size):
        for j in range(size):
            grid[s_x+i][s_y+j]=temp_arr[s_x+i][s_y+j]
            if grid[s_x+i][s_y+j]>0:
                grid[s_x+i][s_y+j] -= 1

    return

def find_square():
    tx, ty = out_pos[0], out_pos[1]

    find = False
    for s in range(2,N+1):
        for i in range(N):
            for j in range(N):
                last_x = i + s -1 
                last_y = j + s -1
                if not range_check(last_x,last_y):
                    continue
                # 출구가 포함되는지.
                if not (i<=tx<=last_x and j<=ty<=last_y):
                    continue

                # m이 하나라도 포함되는지.
                for idx in range(M):
                    px, py = man_list[idx][0],man_list[idx][1]
                    if px==out_pos[0] and py==out_pos[1]:
                        continue
                    if i<=px<=last_x and j<=py<=last_y:
                        find=True
                        break

                if find:
                    break

            if find:
                break
        
        if find:
            break
    
    return s,i,j
            



answer_cnt = 0
for i in range(K):
    #print("Before move",man_list)
    answer_cnt += move_all()
    # 검사
    all_cnt = 0
    for chr_idx in range(M):
        px,py = man_list[chr_idx][0],man_list[chr_idx][1]
        if px==out_pos[0] and py==out_pos[1]:
            all_cnt += 1
    
    if all_cnt==M:
        break


    #print("Move",man_list)
    rotate()
    #print(man_list)
    #print('out pos ',out_pos)
    # for i in range(N):
    #     for j in range(N):
    #         print(grid[i][j],end=' ')
    #     print()

print(answer_cnt)
print( out_pos[0]+1,out_pos[1]+1)



