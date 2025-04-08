

# 입력
# n,m,k 격자 플레이어수 라운드 수
# 2<=n<=20
# 1<=m<=최대 30명
# 1<=총<=10^5
# 초기능력치 1<=s<=100

#1<=x,y<=n -> 0으로 낮춰야한다.
# d: 0,1,2,3 / 상우하좌 / 오른 90도회전 방향으로


#요구사항

# 가던 방향이 막히면, 반대 방향으로 움직임.
# battle시, 패배하면 가던방향으로 계속간다.
# 가다가 막히거나 사람있을시 우측 90도 회전

# 능력치+총의 차만큼 포인트 획득
# 각 플레이어의 획득한 포인트 출력

# 시간 5초.

# 알고리즘
# 시뮬레이션
 

n,m,k = tuple(map(int,input().split()))

answer = [0]*m

board_gun = [[ [] for _ in range(n)  ] for _ in range(n)]
board_man = [ [-1]*n for _ in range(n)]
grid = [ list(map(int,input().split())) for _ in range(n)]


# print(board_gun)
# print(grid)
#x,y,d,s
man_data = [ list(map(int,input().split())) for _ in range(m)]
#x,y,d,s,(gun 추가)


for i in range(n):
    for j in range(n):
        if grid[i][j]!=0:
            board_gun[i][j].append(grid[i][j])
# print(board_gun)
for i in range(m):
    man_data[i][0] -= 1
    man_data[i][1] -= 1
    x,y,d,s = man_data[i]
    # board에 넣고.
    board_man[x][y] = i
    man_data[i].append(0) # 가진 총 크기 백터도 추가. 0이면 없는 것. 

# print(man_data)

dxs=[-1,0,1,0]# 상우하좌
dys=[0,1,0,-1]



def range_check(x,y):
    return 0<=x<n and 0<=y<n

def move_next_val(x,y,idx):
    # 다음에 갈 방향을 정의

    direction = man_data[idx][2]
    #print('direction',direction)    
    #범위밖이면 반대로 뒤집기. +2 %
    next_x=x+dxs[direction]
    next_y=y+dys[direction]
    if not range_check(next_x,next_y):
        #뒤집어서 다음 칸으로
        direction = (direction+2)%4
        # 방향도 다시 담아줌
        man_data[idx][2]=direction
        ##
        next_x = x+dxs[direction]
        next_y = y+dys[direction]
    return next_x,next_y 

def move_next_val_looser(x,y,idx):
    # 다음에 갈 방향 정의
    # 범위 밖이거나, 사람이 있을경우 
    direction = man_data[idx][2]
    for i in range(4):
        new_direction = (direction+i)%4        
        #뒤집어서 다음 칸으로        
        next_x=x+dxs[new_direction]
        next_y=y+dys[new_direction]
        # 자기 원래 자리로 돌아오기 포함.
        if range_check(next_x,next_y) and (board_man[next_x][next_y]==-1 or board_man[next_x][next_y]==idx ) :
            # 방향도 다시 담아줌
            man_data[idx][2]=new_direction
            ##
            next_x = x+dxs[new_direction]
            next_y = y+dys[new_direction]
            break
    return next_x,next_y 

    
def move_chr(next_x,next_y,now_x,now_y,idx):
    global board_man
    global man_data
    board_man[now_x][now_y]=-1
    board_man[next_x][next_y]=idx
    man_data[idx][0]=next_x
    man_data[idx][1]=next_y

def chagne_gun(x,y,idx):
    # 땅에서 chr가 좋은 총을 골라 바꿔준다.
    global board_gun
    global man_data
    tmp = man_data[idx][4]
    max_idx = 0
    max_gun = -1
    for gun_idx,gun in enumerate(board_gun[x][y]):
        if max_gun<gun:
            max_gun = gun
            max_idx = gun_idx
    if tmp < max_gun:
        man_data[idx][4]=max_gun
        board_gun[x][y][max_idx] = tmp


def fight(idx1,idx2):
    # 두 사람이 싸운다.
    winner = idx1
    looser = idx2
    
    stat1,gun1 = man_data[idx1][3],man_data[idx1][4]
    stat2,gun2 = man_data[idx2][3],man_data[idx2][4]
    allstat1 = stat1+gun1
    allstat2 = stat2+gun2

    point = abs(allstat1-allstat2)
    if allstat1> allstat2:
        winner =idx1
        looser =idx2
    elif allstat1< allstat2:
        winner =idx2
        looser =idx1
    else:
        # 둘이 같으면
        if stat1> stat2:
            winner =idx1
            looser =idx2
        elif stat1< stat2:
            winner =idx2
            looser =idx1
        #point = abs(stat1-stat2)
    answer[winner]+=point
    return winner,looser

def drop_gun(x,y,idx):
    global man_data
    tmp=man_data[idx][4]
    if tmp==0:
        # 원래 총이 없으면.
        return
    man_data[idx][4] = 0
    board_gun[x][y].append(tmp)



for t in range(k):
    # print("Round ",t)
    for chr_idx in range(m):
        now_x,now_y = man_data[chr_idx][0],man_data[chr_idx][1]
        next_x,next_y=move_next_val(now_x,now_y,chr_idx)
        #print('chr idx',chr_idx,next_x,next_y,board_man[next_x][next_y])

        # 다음 사람 있는지 검사해서
        if board_man[next_x][next_y] ==-1:
            # 사람 없을때.
            move_chr(next_x,next_y,now_x,now_y,chr_idx)
            # 총바꾸기
            chagne_gun(next_x,next_y,chr_idx)
            
        else:
            # 사람 있을때.
            #print("found : ",next_x,next_y)
            fight_person=board_man[next_x][next_y]
            winner_idx,looser_idx = fight(chr_idx,fight_person)
            # drop gun
            drop_gun(next_x,next_y,looser_idx)
            # change gun
            chagne_gun(next_x,next_y,winner_idx)
            # looser move
            # winner 가 누구냐에 따라 move 달리.
            if chr_idx==winner_idx:
                # 후발이 이길시
                move_chr(next_x,next_y,now_x,now_y,winner_idx)
                looser_next_x,looser_next_y=move_next_val_looser(next_x,next_y,looser_idx)
                move_chr(looser_next_x,looser_next_y,next_x,next_y,looser_idx)
                #이동해서 패자도 먹기.
                chagne_gun(looser_next_x,looser_next_y,looser_idx)
                # 어쩔수 없이 보드에 다시 기록
                board_man[next_x][next_y]=winner_idx
                #
            else:
                #후발이 질시. 후발만 움직인다.
                looser_next_x,looser_next_y=move_next_val_looser(next_x,next_y,looser_idx)
                move_chr(looser_next_x,looser_next_y,now_x,now_y,looser_idx)
                chagne_gun(looser_next_x,looser_next_y,looser_idx)
    # for chr_idx in range(m):    
    #     print('fin : ',man_data[chr_idx])
    
    # for i in range(n):
    #     for j in range(n):
    #         print(board_man[i][j],end=' ')
    #     print()

    # for i in range(n):
    #     for j in range(n):
    #         print(board_gun[i][j],end=' ')
    #     print()
        

    # for i in range(m):
    #     print(answer[i],end=' ')

for i in range(m):
    print(answer[i],end=' ')





