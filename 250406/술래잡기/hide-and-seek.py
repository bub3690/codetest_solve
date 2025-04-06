
# n,m,h,k
# n홀수
# 5<=n<=99
# m개줄 도망자 위치(x,y) d 1 좌우, d 2 상하
# k<= 100
# x,y반대 조심. 

# 요구사항
# 도망자-> 술래 순으로 움직임
# 거리가 3이하인 도망자만 움직임.
# 술래가있으면 방문 x
# 격자 끝에 와서 반대방향으로 돌기. 그 다음 이동.

# 술래는 달팽이처럼 돈다.
# 술래는 이동후에, 도망자를 잡음. 현재칸을 포함 3칸방향으로.
# 나무칸은 탐지 못함.
# 방향을 틀어야하는 위치면, 바로 방향을 틀어줌.

# k번동안 얻게되는 총 점수.

#시간 5초

# 알고리즘
# 시뮬레이션

# 풀이 방법
# (위치, 방법) 저장
# 술래: (위치,방향,크기)
# 격자가 아니라. 수치를 비교하는 방식으로 완전탐색하기.
# 10^6 으로 시간으로 충분해 보인다. 굳이 격자가 아니어도 될것 같다.
# 다만 트리에 포함된 위치는 넘어가야한다. 매번 in 연산해야하나?


# 각자 이동 구현
# 술래 이동 구현

# 이동함수는 동일. 자기 방향받고 +1 해준다.
# 술래는 미리 path를 만들고 거기를 따라 움직인다. direction도 미리 정해둔다. k마다 길이 정해짐.
# forward path, reverse path. 횟수가 n^2-1 이 되면, forwar, reverse 번갈아가면서 수행.


from collections import deque

n,m,h,K = tuple(map(int,input().split()))
runner_list = [ list(map(int,input().split())) for _ in range(m)]
tree_list = [ list(map(int,input().split())) for _ in range(h)]

# tree는 set로, runner는 que로 두기.
# tree는 xy를 붙여서 나타낼까?
tree_set = set()
for i in range(h):
    tree_x,tree_y = tree_list[i]
    tree_xy = str(tree_x*100)+str(tree_y)
    tree_set.add(tree_xy)

runner_que = deque()

for i in range(m):
    direction=runner_list[i][2]
    #상하좌우 1234
    if direction == 1:
        direction =4

    runner_list[i][2]=direction
    runner_que.append(runner_list[i])
   
#print(runner_list)

start_position = [n//2+1, n//2+1]
end_position = [1,1]

def move_player(direct,pos):
    pos_x = pos[0]
    pos_y = pos[1]

    if direct == 0: # 상
        next_pos_x = pos_x-1
        next_pos_y = pos_y
    elif direct == 1: # 우
        next_pos_x = pos_x
        next_pos_y = pos_y +1         
    elif direct == 2: # 하
        next_pos_x = pos_x+1
        next_pos_y = pos_y
    else: #좌
        next_pos_x = pos_x
        next_pos_y = pos_y-1

    if 1<=next_pos_x<=n and 1<=next_pos_y<=n:
        return [next_pos_x,next_pos_y]
    else:
        return pos
    



def move_forward(start_position,end_position):
    path_list = []
    now_path = start_position
    count = 0
    direct = 0 # 0: 상, 1: 우, 2:하, 3:좌
    while now_path != end_position:
        move_much = count//2 +1

        for i in range(move_much):
            now_path = move_player(direct,now_path)
            next_direction = (direct+1)%4 # 바로 고개틀기.
            path_list.append([now_path[0],now_path[1],next_direction])
            if now_path == end_position:
                break
        
        count +=1
        direct = (direct+1)%4
        

    return path_list


#path_forward = [start_position,]
path_forward = move_forward(start_position,end_position)

path_backward = path_forward[::-1]


def get_dist(pos1,pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def move_runner(pos,direction,player_pos):
    
    x,y = pos
    player_x = player_pos[0]
    player_y = player_pos[1]

    # 상하좌우 1234
    if direction == 1:
        next_x = x -1
        next_y = y
    elif direction == 2:
        next_x = x+1
        next_y = y
    elif direction == 3:
        next_x = x
        next_y = y-1
    else:
        next_x = x
        next_y = y+1
    
    # 다음 방향이 벽이면, direction 바꾸고 다시. 시도
    if not( 1<=next_x<=n and 1<=next_y<=n):
        next_x = x
        next_y = y
        if direction == 1:
            direction = 2
        elif direction ==2:
            direction =1
        elif direction ==3:
            direction= 4
        else:
            direction=3
        
        if direction == 1:
            next_x = x -1
            next_y = y
        elif direction == 2:
            next_x = x+1
            next_y = y
        elif direction == 3:
            next_x = x
            next_y = y-1
        else:
            next_x = x
            next_y = y+1
        
        # player가 서있으면 진행하지 않음,
        if next_x==player_x and next_y==player_y:
            next_x = x
            next_y = y
        #print('next ',next_x,next_y)

    next_direction = direction
    return next_x,next_y,next_direction

before_x = start_position[0]
before_y = start_position[1]
answer = 0

for k in range(K):

    now_m = len(runner_que)

    #플레이어 현재 위치.
    now_k = k%(n**2-1) # 23 % 25
    turn = k//(n**2-1)
    if turn%2==0:
        # foward
        now_state_player = path_forward[now_k]
    else:
        #backward
        now_state_player = path_backward[now_k]
    
    player_x = now_state_player[0]
    player_y = now_state_player[1]
    player_dir = now_state_player[2]
    #print('player ',now_state_player)

    #러너 무브.(3이내 만)
    for i in range(now_m):
        #deque에서 하나씩 뽑고 다시 푸시.
        runner_now_lst=runner_que.popleft()
        
        runner_x, runner_y, dir_runner = runner_now_lst[0], runner_now_lst[1], runner_now_lst[2]
        
        runner_dist = get_dist((before_x,before_y),(runner_x,runner_y))
        if runner_dist>3:
            runner_que.append([runner_x, runner_y, dir_runner])
            continue
        runner_x,runner_y,dir_runner=move_runner( (runner_x,runner_y),dir_runner,[before_x,before_y])# 바뀐 방향과 x,y
        runner_que.append([runner_x, runner_y, dir_runner])

    #player move
    before_x= player_x
    before_y= player_y


    # tree에 없다면 제거.
    # 제거 로직.
    ## 3개 좌표만큼 해당되는지 보고 제거.
    for i in range(now_m):
        #deque에서 하나씩 뽑고 다시 푸시.
        runner_now_lst=runner_que.popleft()
        #print(runner_now_lst)        
        runner_x, runner_y, dir_runner = runner_now_lst[0], runner_now_lst[1], runner_now_lst[2]
        xy= str(runner_x*100)+str(runner_y)
        kill_runner = False
        if player_dir == 0: #상
            if player_x-runner_x >= 0 and ( (player_x-runner_x)<=2 and player_y==runner_y) and xy not in tree_set:
                kill_runner = True
        elif player_dir == 1: #우
            if runner_y-player_y >= 0 and ( (runner_y-player_y)<=2 and player_x==runner_x) and xy not in tree_set:
                kill_runner = True      
        elif player_dir == 2:#하
            if runner_x-player_x >=0 and ( (runner_x-player_x)<=2 and player_y==runner_y) and xy not in tree_set:
                kill_runner = True
        else: #좌
            if player_y-runner_y >=0 and ( (player_y-runner_y)<=2 and player_x==runner_x) and xy not in tree_set:
                kill_runner = True                             
      
        if not kill_runner:
            runner_que.append([runner_x, runner_y, dir_runner])
        else:
            #print('kill',[runner_x, runner_y, dir_runner])
            answer += (k+1)
    
    ###

print(answer)
    

