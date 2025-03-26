import sys
from collections import deque


dice_list = list(map(int,input().split()))

dat = [ [] for _ in range(32)  ]


#set map
def set_map(dat):
    #1번부터 21번까지는 서로 연결.
    for i in range(19):
        dat[i].append(i+1)
    dat[19].append(31)
    #나머지 맵
    dat[4].append(20) ##
    dat[20].append(21)
    dat[21].append(22)
    dat[22].append(23)
    dat[23].append(24)
    dat[24].append(25)
    dat[25].append(19)

    dat[9].append(26) ##
    dat[26].append(27)
    dat[27].append(23)

    dat[14].append(28) ##
    dat[28].append(29)
    dat[29].append(30)
    dat[30].append(23)

set_map(dat)


score_map = [2,4,6,8,10,
             12,14,16,18,20,
             22,24,26,28,30,
             32,34,36,38,40,
             13,16,19,25,
             30,35,
             22,24,
             28,27,26,0]

#완탐 방식
pos_list = [-1,-1,-1,-1]# -1 에서 시작해서 1씩 올리는거니까.

def move(now_pos,now_dice):
    #dice 만큼 이동해야함.
    if now_pos==-1:
        now_dice -= 1
        now_pos =0

    #bfs 방식으로 하나씩 넣고 움직이기
    here = now_pos
    for step in range(now_dice):
        if now_pos == 31:
            return now_pos
        # 첫 이동일 때 파란색 경로가 있다면 두 번째 경로 선택
        if len(dat[now_pos])==0:
            return now_pos
        elif step == 0 and len(dat[now_pos]) > 1:
            now_pos = dat[now_pos][1]
        else:
            now_pos = dat[now_pos][0]

    return now_pos


def check_mal(pos):
    check = False
    if pos ==31:
        return False

    for i in range(4):
        if pos_list[i]==pos:
            check=True
    
    return check


answer = -1
def go(here,score):
    global pos_list
    global answer

    #기저 . 10번 다이스.
    if here == 10:
        answer = max(answer,score)
        return
    
    get_score =0
    for i in range(4):
        now_pos = pos_list[i]
        now_dice = dice_list[here]

        next_pos=move(now_pos,now_dice)

        if next_pos>=32 or now_pos==31:
            # 끝점에 도달하면 빼버리기.
            continue
        # 겹치는 부분 처리.
        if check_mal(next_pos):
            #도착시 겹치면 그 말 안씀.
            continue
        
        pos_list[i] = next_pos
        # print(next_pos)
        # print("score ",score_map[next_pos])
        go( here+1, score+score_map[next_pos] ) 
        pos_list[i] = now_pos
        




go(0,0)# dice 번호. 점수 합.

print(answer)






