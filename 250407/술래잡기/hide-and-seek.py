
n, m, h, k = tuple(map(int, input().split()))

#도망자의 방향을 담을 배열
hiders=[
    [ [ ] for _ in range(n) ]
    for _ in range(n)
]
#temp
next_hiders = [
    [[] for _ in range(n) ]
    for _ in range(n)
]

tree =[
    [False]*n
    for _ in range(n)
]

# 정방향 기준으로 
# 술래가 달팽이모양으로 돌 방향
# 다음으로 어디에 갈 것인지, 얼굴 방향을 기록해 둔 것.
seeker_next_dir = [
    [0]*n 
    for _ in range(n)
]

seeker_rev_dir = [
    [0]*n
    for _ in range(n)
]

seeker_pos = (n//2,n//2)
#술래가 움직이는 방향이 정방이면 True / 아니면 False
forward_facing = True
ans = 0

# 술래 정보
for _ in range(m):
    x,y,d = tuple(map(int, input().split()))
    hiders[x-1][y-1].append(d)

#나무정보
for _ in range(h):
    x, y = tuple(map(int, input().split()))
    tree[x - 1][y - 1] = True

#정방향 seeker 경로
def initialize_seeker_path():
    #상우하좌
    dxs=[-1,0,1,0]
    dys=[0,1,0,-1]

    # 시작위치와 방향
    # 해당방향으로 이동할 횟수
    curr_x,curr_y = n//2,n//2
    move_dir, move_num = 0,1
    while curr_x or curr_y:
        for _ in range(move_num):
            seeker_next_dir[curr_x][curr_y] = move_dir
            curr_x, curr_y = curr_x+dxs[move_dir], curr_y+dys[move_dir]
            #이동하고 나서 역방향 기록. (3,3)은reverse에 없을 것. 다음에 어디로갈지 기록해둔것이니.
            seeker_rev_dir[curr_x][curr_y] = move_dir + 2 if move_dir <2 else move_dir -2
            
            # 이동하는 도중 원점으로 오면, 종료
            if not curr_x and not curr_y:
                break
                
        # 방향을 바꿈
        move_dir = (move_dir+1)%4
        # 위 혹은 아래 가된 경우.
        # 움직이는 횟수를 1 키움
        if move_dir ==0 or move_dir ==2:
            move_num += 1

# 격자 내에 있는지를 판단.
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def hider_move(x,y,move_dir):
    dxs = [0,0,1,-1]
    dys = [-1,1,0,0] 
    # 좌우하상 #두방향으로 움직이니까
    nx,ny = x+dxs[move_dir],y+dys[move_dir]

    # step1
    # 격자를 벗어나면. 우선 방향을 튼다.
    if not in_range(nx,ny):
        # 0 <1 , 2 <3
        move_dir = 1 -move_dir if move_dir<2 else 5-move_dir
        nx,ny = x+dxs[move_dir],y+dys[move_dir]
    
    # step2
    # 그다음 위치에 술래가 없다면 움직임
    if (nx,ny) != seeker_pos:
        #temp에 박아둔다.
        next_hiders[nx][ny].append(move_dir)
    else:
        next_hiders[x][y].append(move_dir)


def dist_from_seeker(x,y):
    #현재 술래
    seeker_x,seeker_y = seeker_pos
    return abs(seeker_x-x)+abs(seeker_y-y)

def hider_move_all():
    #next hider 초기화
    for i in range(n):
        for j in range(n):
            next_hiders[i][j] = []
    
    # hider 전부 움직여준다.
    for i in range(n):
        for j in range(n):
            # 술애와 거리가 3이내인 도망자들에 대해 적용
            if dist_from_seeker(i,j) <=3:
                for move_dir in hiders[i][j]:
                    hider_move(i,j,move_dir)
            
            # 그렇지 않다면 현재 위치에 그대로 넣어줌.
            else:
                for move_dir in hiders[i][j]:
                    next_hiders[i][j].append(move_dir)
    
    # next hider temp값들을 옮겨줌.
    for i in range(n):
        for j in range(n):
            hiders[i][j] = next_hiders[i][j]


# 현재 술래가 바라보는 방향을 가져옴.
def get_seeker_dir():
    x,y = seeker_pos

    #다음에 어느방향으로 움직여하는지. 정보. (또한 바라보는방향)
    move_dir = 0
    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir= seeker_rev_dir[x][y]
    
    return move_dir
                    
def check_facing():
    global forward_facing

    # case1 . 정방향으로 끝에 다다른 경우, 방향을 바꿔준다.
    # 역방향 0,0에는 뭐가 담겨있지?
    if seeker_pos == (0,0) and forward_facing:
        forward_facing = False
    
    # 역방향으로 끝에 다다른 경우, 방향을 바꿔줌.
    if seeker_pos ==(n//2,n//2) and not forward_facing:
        forward_facing = True


def seeker_move():
    global seeker_pos
    x,y = seeker_pos

    # 상우하좌 순서대로 넣어줌.
    dxs,dys = [-1,0,1,0],[0,1,0,-1]

    move_dir = get_seeker_dir()#다음에 어느 방향으로 갈지

    # 술래를 한칸움직인다.
    seeker_pos = (x+dxs[move_dir], y+dys[move_dir])

    # 끝에 도달했다면 방향을 바꿈. ****
    check_facing()

def get_score(t):
    #죽이는 코드 부분
    global ans

    # 상우하좌 순서대로 넣어줌.
    dxs,dys = [-1,0,1,0],[0,1,0,-1]
    x,y = seeker_pos
    # 술래의 방향을 불러옵니다.
    move_dir = get_seeker_dir()
    
    for dist in range(3):
        nx,ny = x+dist*dxs[move_dir], y+dist*dys[move_dir]

        #격자를 벗어나지 않으며, 나무가 없는 위치면.
        # 도망자 전부 잡음.
        if in_range(nx,ny) and not tree[nx][ny]:
            ans += t*len(hiders[nx][ny])

            #도망자들 사라진다.
            hiders[nx][ny] = []

def simulate(t):
    hider_move_all()

    #술래 움직임.
    seeker_move()# seeker_pos, dir 갱신

    #점수 얻기.
    get_score(t)


#정,역 방향 페스 계산
initialize_seeker_path()

#k번 술래잡기.
for t in range(1,k+1):
    simulate(t)

print(ans)
