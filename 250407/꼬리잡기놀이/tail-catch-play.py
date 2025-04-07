

#입력
#n,m,k 격자크기, 팀 개수, 라운드k
#0:빈칸, 1: 머리사람, 2:나머지, 3: 꼬리사람, 4: 이동선

# 3<=n<=20, 1<=m<=5, 1<=k<=1000


#요구사항
#3명이상이 한팀.
# 맨앞 머리사람. 맨뒤 꼬리사람.
# 각팀은 이동선만 따라걸음. 팀끼리 선 안겹침.

# 머리사람을 따라서 한 칸 이동.
# 왼 행-> 아래열. ->오 행 > 위 열 ->.. 반복해서 공이 던져짐
# 공을 첫번째로 받는 사람한테 점수를줌. k^2 (머리부터 시작하여 번호) 점수.
# 공을 획득하면, 머리와 꼬리 사람이 바뀐다. 방향을 바꾼다.

#점수의 총합 구하라.

# 알고리즘.
# 시뮬레이션

# 풀이방법
# 회전알고리즘.

#시간 5초

# k*n^2. 10^3*10^2=10^5

from collections import deque

n,m,k = tuple(map(int,input().split()))

grid = [ list(map(int,input().split())) for _ in range(n)]


team_list = [] #현재 팀의 위치를 담은 배열
visit = [ [0 for _ in range(n)] for _ in range(n) ]

dxs = [0,1,0,-1]#우하좌상
dys = [1,0,-1,0]

def check_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x,y):
    
    que = deque()
    que.append((x,y))
    path_list = []
    visit[x][y] = True
    path_list.append([x,y])
    while que:
        now_x, now_y = que.popleft()
        selection_next =[]
        for i in range(4):
            next_x = now_x+dxs[i]
            next_y = now_y+dys[i]
            if not check_range(next_x,next_y):
                continue
            if grid[next_x][next_y] == 0 or grid[next_x][next_y] == 4:
                continue
            if visit[next_x][next_y]==True:
                continue
            # 2또는 1을 팀으로 추가시키는 코드가 됨.
            # 그런데, 찾는순서가 1보다 2을 먼저 추가하게 된다면 문제가 된다. 2먼저 찾도록할 방법이 있을까?
            # 다 모은다음 그다음 추가하기.
            selection_next.append((next_x,next_y))
        
        if len(selection_next)==1:
            #그냥 바로 head을 찾은 경우.
                next_x,next_y = selection_next[0]
                path_list.append([next_x,next_y])
                visit[next_x][next_y]= True
                que.append((next_x,next_y))
        else:
            for selection in selection_next:
                next_x,next_y = selection
                next_val = grid[next_x][next_y]
                if next_val ==1:
                    continue
                path_list.append([next_x,next_y])
                visit[next_x][next_y]= True
                que.append((next_x,next_y))
                break

    return path_list

def search_team():
    global team_list
    global visit
    visit = [ [0 for _ in range(n)] for _ in range(n) ]#visit도 초기화.
    
    team_list = [] # 초기화
    for i in range(n):
        for j in range(n):
            # 꼬리를 찾아서 추가하기.
            if visit[i][j]!=True and grid[i][j]==3:
                team_path=bfs(i,j)
                team_list.append(team_path)
    return

def search_next(x,y):
    found = False
    for i in range(4):
        next_x = x+dxs[i]
        next_y = y+dys[i]
        if check_range(next_x,next_y) and grid[next_x][next_y]==4 :
            found= True
            break

    if not found:
        for i in range(4):
                next_x = x+dxs[i]
                next_y = y+dys[i]
                if check_range(next_x,next_y) and grid[next_x][next_y]==3:
                    found= True
                    break    
        
    return next_x,next_y,found
            

def rotate():
    global team_list
    new_team_list = []
    # 머리부터 한칸씩 움직이기.
    for team in team_list:
        now_new_team = []
        next_x=None
        next_y=None
        
        for idx,member in enumerate(team[::-1]):
            # 머리부터시작해서 하나씩 밀기.
            now_x,now_y = member[0], member[1]
            if next_x==None or next_y==None:
                next_x, next_y,found = search_next(now_x,now_y)
            
            if grid[now_x][now_y]==1 and grid[next_x][next_y]==3 and idx !=0:
                #돌고돌아 3자리.
                now_new_team.append([next_x,next_y])
                break

            #4와 자리바꾸기.
            temp = grid[next_x][next_y]
            grid[next_x][next_y] = grid[now_x][now_y]
            grid[now_x][now_y] = temp
            
            now_new_team.append([next_x,next_y])#팀 바꿔서 기록용
            
            next_x = now_x
            next_y = now_y
        
        new_team_list.append(now_new_team[::-1])

            
    #팀 변경사항을 덮어쓰기.
    team_list = new_team_list
    return 

def ballshot(round):
    # 모든 팀 대상으로 공은 공유되니까. 맞은 위치 하나 리턴.
    # turn 별로.
    
    turn = round//n

    find_x = None
    find_y = None
    find_first = True
    if turn==0:
        row = round%n
        for i in range(n):
            if grid[row][i] == 1 or grid[row][i] == 3 or grid[row][i] == 2 :
                find_x = row
                find_y = i
                break
    elif turn==1:
        col = round%n
        for i in range(n-1,-1,-1):
            if grid[i][col]==1 or grid[i][col]==3 or grid[i][col]==2:
                find_x = i
                find_y = col
                break
    elif turn==2:
        row = n-round%n -1
        for i in range(n-1,-1,-1):
            if grid[row][i] ==1 or grid[row][i] ==3 or grid[row][i] ==2 :
                find_x = row
                find_y = i
                break
    else:
        col = n-round%n -1
        for i in range(n):
            if grid[i][col]==1 or grid[i][col]==3 or grid[i][col]==2:
                find_x = i
                find_y = col
                break

    return find_x,find_y

def get_score(member,team):
    # 몇번째 멤버인지 계산해서 점수로 추출.
    len_team =len(team)
    ind = team.index(member)
    score = (len_team-ind)**2
    return score

answer = 0

search_team()

for round in range(k):
    rotate()
    #print("----")
    # for i in range(n):
    #     for j in range(n):
    #         print(grid[i][j],end=' ')
    #     print()    
    #print(team_list)
    find_x,find_y=ballshot(round)
    #print('ballshot ',find_x,find_y)
    #어느 팀인지 찾고. 점수 내기.
    for team_idx,team in enumerate(team_list):
        if [find_x,find_y] in team:
            answer += get_score([find_x,find_y],team)
            # 맞은팀 거꾸로 만들어주기.
            tail_x,tail_y = team[0][0],team[0][1]
            head_x,head_y = team[-1][0],team[-1][1]
            grid[tail_x][tail_y] = 1
            grid[head_x][head_y] = 3
            team_list[team_idx] = team_list[team_idx][::-1]
            break





    #print(answer)


print(answer)

# print(team_list)

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j],end=' ')
#     print()


