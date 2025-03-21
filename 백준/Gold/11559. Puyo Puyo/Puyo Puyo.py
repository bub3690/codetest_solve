from collections import deque


# 6개문자. .,R,G,B,P,Y  : .은 빈공간
# 입력으로는 떨어져 내린 뿌요들
# 12*6 배열열

# 4개 이상이 상하좌우로 연결된다면. 없어지고 1연쇄.
# 그리고 내려온다.
# 현재 상황에서 몇 연쇄가 일어나는지 출력.


#BFS 처럼 주변 탐색.
#연결요소 탐색.
# 배열을 새로 만들어서 

# 1초



grid = [ list(input().rstrip()) for _ in range(12)]


# print(grid)

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def check_range(x,y):
    return 0<=x<12 and 0<=y<6

def bfs(x,y,visit):
    ground_color = grid[x][y]
    que=deque()
    que.append((x,y))
    visit[x][y] = 1
    color_count = 1
    visited_xy = []
    visited_xy.append((x,y))
    while que:
        now_x,now_y = que.popleft()
        now_color = grid[x][y]
        for i in range(4):
            next_x = now_x+dxs[i]
            next_y = now_y+dys[i]
            if check_range(next_x,next_y) and visit[next_x][next_y]!= 1:
                next_color= grid[next_x][next_y]
                if next_color==ground_color:
                    color_count += 1
                    visit[next_x][next_y] = 1
                    visited_xy.append((next_x,next_y))
                    que.append((next_x,next_y))

    return visited_xy


def change(checked_bomb,grid):
    new_bomb_list= []
    for bomb_list in checked_bomb:
        for pos in bomb_list:
            new_bomb_list.append(pos)
    
    # 한 컬럼별로 x표시된 것들을 제거해간다.
    # print('new bomb ',new_bomb_list)
    for j in range(6):
        que = deque()
        for i in range(11,-1,-1):
            if (i,j) in new_bomb_list:
                continue
            que.append(grid[i][j])
        
        while len(que) !=12:
            que.append('.')
        # print(que)
        for i in range(12):
            grid[i][j] = que.pop()
        



answer = 0
play = True
while play:
    visit = [ [0]*6 for _ in range(12) ]
    checked_bomb = []
    for i in range(12):
        for j in range(6):
            if visit[i][j] ==0 and grid[i][j] != '.':
                checked_temp = bfs(i,j,visit)
                # print(checked_temp)
                if len(checked_temp)>=4:
                    checked_bomb.append(checked_temp)
    
    if len(checked_bomb) ==0:
        play= False
    else:
        #print(checked_bomb)
        change(checked_bomb,grid)
        answer += 1

# for i in range(12):
#     for j in range(6):
#         print(grid[i][j],end=' ')
#     print()

print(answer) 

        


