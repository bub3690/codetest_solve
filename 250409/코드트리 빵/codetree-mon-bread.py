
# 입력
# 격자크기 n, 사람수 m
# 0은 공간. 1 베이스캠프.
# 2<=n<=15, 1<=m<=n^2 or 최대30 . m<=베이스캠프<=n^2-m

#요구사항

# 1번순서. 최단거리로 편의점 향하기. 상좌우하.
# 2번순서. 해당 편의점 도착시, 지날수 없는칸.
# 3번순서. t번 사람은 베이스켐프에 들어감. 베이스캠프는 원하는 편의점에 행열 순으로 최단거리로.
# 베이스캠프가 할당되면 거기를 지날수 없음.
# 출력 모든 사람이 도착하는 시간.

#알고리즘
#bfs simulation

#풀이 방법
# 움직일때 매번 bfs로 경로를 탐색해서 할당한다.
# moveall -> setbase 순으로 진행

#시간
#5초. O(m*n^2*t). t는 최대 n^2. n^6안에 끝난다. 불안한데.

from collections import deque

n,m = tuple(map(int,input().split()))

grid = [ list(map(int,input().split())) for _ in range(n)]

cx_list = [ list(map(int,input().split())) for _ in range(m)]

base_list = []

man_list = [ [] for _ in range(m) ]


dxs = [-1,0,0,1]
dys = [0,-1,1,0]


#cx 낮추기.
for i in range(m):
    cx_list[i][0] -= 1
    cx_list[i][1] -= 1

# base 탐색
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            base_list.append((i,j))



def search_base(x_cx,y_cx):
    global base_list
    # base가 이미 쓰인곳은 못쓴다. 따라서 제거 해줘야함.
    candidates = []
    len_base = len(base_list)
    for i in range(len_base):
        row =  base_list[i][0]
        col =  base_list[i][1]
        diff_row = abs(x_cx-row)
        diff_col = abs(y_cx-col)
        distance = diff_row+diff_col
        candidates.append( (distance,diff_row,row,col) )
    #tie을 어떻게 처리하지?
    best_idx, best_val = min(enumerate(candidates),key=lambda x:x[1] )

    return best_idx

def set_base(t):
    if t<m:
        cx = cx_list[t]
        # 가장 가까운 베이스 찾기.
        x_cx, y_cx = cx[0],cx[1]
        base_idx=search_base(x_cx,y_cx)
        base_x, base_y = base_list[base_idx][0],base_list[base_idx][1]
        del base_list[base_idx]

        # 현재 위치 할당
        man_list[t]= [ base_x, base_y ]
        grid[base_x][base_y] = -1
        

    return

def move_all():
    for i in range(m):
        if len(man_list[i]) == 0:
            continue
        if man_list[i] == cx_list[i]:
            continue # 도착했는지 여부.
        move(i)

def range_check(x,y):
    return 0<=x<n and 0<=y<n

def move(chr_idx):
    # visit 초기화
    x,y = man_list[chr_idx][0], man_list[chr_idx][1]
    cx_x,cx_y = cx_list[chr_idx]
    next_x,next_y=bfs(x,y,cx_x,cx_y)
    #print("result :",next_x,next_y)
    man_list[chr_idx][0]=next_x
    man_list[chr_idx][1]=next_y
    return

def bfs(x,y, cx_x,cx_y):
    visited = [[False]*n for _ in range(n)]
    found = False

    que = deque()
    que.append((x,y))
    visited[x][y]= True
    while(que):
        now_x,now_y = que.popleft()
        for i in range(4):
            next_x = now_x + dxs[i]
            next_y = now_y + dys[i]
            if range_check(next_x,next_y) and grid[next_x][next_y]!=-1 and visited[next_x][next_y]==False:
                # 방문.
                visited[next_x][next_y] = (now_x,now_y)
                que.append((next_x,next_y))
                # 목표,cx 면 탐색을 멈춰야함.
                if next_x==cx_x and next_y==cx_y:
                    found= True
                    #print("found",next_x,next_y)
                    #print(visited[next_x][next_y])
                    break
                
        if found:
            break        
    
    #x,y 가 나올때 까지 따라 올라가기.
    next_prev = visited[next_x][next_y]
    if next_prev == (x,y):
        # 도착
        return next_x,next_y

    now_prev = visited[next_x][next_y]
    while next_prev != (x,y):
        now_prev = (next_prev[0],next_prev[1]) # 직후 에 가야할곳이 담김.
        next_prev = visited[next_prev[0]][next_prev[1]]
    # 바로 이전 경우면?

    return now_prev


t=0
while True:
    move_all()
    set_base(t)


    #print(man_list)

    # 모두 도착했는지 체크.    
    cnt = 0
    for i in range(m):
        if man_list[i]==cx_list[i]:
            cnt+=1
    if cnt == m:
        break
    
    t+=1

print(t+1)



