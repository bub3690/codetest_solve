
# 입력
# 격자크기 n, 사람수 m
# 0은 공간. 1 베이스캠프.
# 2<=n<=15, 1<=m<=n^2 or 최대30 . m<=베이스캠프<=n^2-m

#요구사항

# 1번순서. 최단거리로 편의점 향하기. 상좌우하.(모든사람들이!!!!!)
# 2번순서. 해당 편의점 도착시, 지날수 없는칸.(다 움직이고 마지막에 체크)
# 3번순서. t번 사람은 베이스켐프에 들어감. 베이스캠프는 원하는 편의점에 행열 순으로 최단거리로.
# 베이스캠프가 할당되면 거기를 지날수 없음.
# 출력 모든 사람이 도착하는 시간.

#알고리즘
#bfs simulation

#풀이 방법
# 매번 bfs를 통해 한 편의점으로 부터 모든 경로를 측정. 그리고 본인 자리에서 가장 작고 우선순위대로 선택.
# set base시에 bfs를 통해 자리 정한다.
# moveall -> 편의점=-1 지정 -> setbase 순으로 진행

#시간
#1초. O(m*n^2*t). t는 최대 n^2. n^6안에 끝난다. 불안한데.

# 해당 문제가 틀린이유. base를 정할때도. bfs를 통해서 정해야한다. 최단거리란 매번 바뀐다.
# 또한 우선순위란건 단순히 bfs를 range 돌린다고 되는게 아니라. 모든 최단거리를 구한후에 그 시작점에서 정하는 것이다.



from collections import deque

n,m = tuple(map(int,input().split()))

grid = [ list(map(int,input().split())) for _ in range(n)]

cx_list = [ list(map(int,input().split())) for _ in range(m)]

base_list = []

man_list = [ [] for _ in range(m) ]


dxs = [-1,0,0,1]
dys = [0,-1,1,0]


visit = [[0]*n for _ in range(n)]
step  = [[0]*n for _ in range(n)]


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
    bfs(x_cx,y_cx)
    # 최단거리인 base 찾기.
    
    # i,j 순으로 탐색하면 최솟값이 먼저 담기게 된다. 그래서 조건에 맞음.
    # 따로 baselist를 관리하지는 않는다.

    next_x = -1
    next_y = -1
    dist = 1e9
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1 and visit[i][j]==1 and step[i][j]<dist:
                dist = step[i][j]
                next_x = i
                next_y = j

    return next_x,next_y

def set_base(t):
    time_ind = t -1
    if time_ind<m:
        cx = cx_list[time_ind]
        # 가장 가까운 베이스 찾기.
        x_cx, y_cx = cx[0],cx[1]
        base_x,base_y = search_base(x_cx,y_cx)
        #print("베이스 ",time_ind,base_x,base_y)
        
        # 현재 위치 할당
        man_list[time_ind]= [ base_x, base_y ]
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
    bfs(cx_x,cx_y)

    # 4방향을 보면서 갈 곳 정하기.  
    dist = 1e9
    next_x = -1
    next_y = -1
    for i in range(4):
        nx = x +dxs[i]
        ny = y +dys[i]
        if range_check(nx,ny) and visit[nx][ny]==1 and step[nx][ny]<dist:
            dist = step[nx][ny]
            #print("dist ",dist)
            next_x=nx
            next_y=ny
    #print("next : ",next_x,next_y)
    man_list[chr_idx][0] = next_x
    man_list[chr_idx][1] = next_y

    # 다른사람도 go를 다맞추면 체크해야한다!!
    #편의점 탐색 완료시 체크해줘야함!!!!

    return


# 틀린 부분. cx에서 x,y로 가는길을 탐색하는 방식으로 해야한다. 그리고 step 배열을 바탕으로 불러오기.
# 아니면 최단거리가 아닌 길이 나온다.
def bfs(x,y):
    que = deque()
    #초기화
    for i in range(n):
        for j in range(n):
            visit[i][j] = 0
            step[i][j] = 0
    
    que.append((x,y))
    visit[x][y] = 1

    while que:
        now_x,now_y=que.popleft()
        for i in range(4):
            next_x = now_x+dxs[i]
            next_y = now_y+dys[i]
            if range_check(next_x,next_y) and visit[next_x][next_y]==0 and grid[next_x][next_y]!=-1:
                step[next_x][next_y] = step[now_x][now_y] + 1
                visit[next_x][next_y] = 1
                que.append(( next_x,next_y ))


#print(base_list)
t=0
while True:
     
    t+=1    
    move_all()

    # 2단계 + 모두 도착했는지 체크.    
    #print('man ',man_list)
    #print('cx ',cx_list)
    for i in range(m):
        if man_list[i]==cx_list[i]:
            #print(i,' 도착')
            grid[man_list[i][0]][man_list[i][1]]= -1

    set_base(t)
    #print(man_list)    
    cnt = 0    
    for i in range(m):
        if man_list[i]==cx_list[i]:
            cnt+=1
    if cnt == m:
        break


print(t)



