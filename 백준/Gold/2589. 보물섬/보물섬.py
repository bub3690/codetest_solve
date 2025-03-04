import sys
from collections import deque

input = sys.stdin.readline



dx = [0,1,0,-1]
dy = [1,0,-1,0]

L, W= tuple(map(int,input().split()))

grid = [ list(input()) for _ in range(L)]


#각 조합마다 bfs 계산.
#bfs에서 도달 못할시 계산 반영 x


def check_range(x,y):
    return x>=0 and x<L and y>=0 and y<W
    
# 특정 종점이 확실하지 않기에. visit 배열이 필요하다.

visit = [[0]*50 for _ in range(50)]

def clear():
    global visit
    for i in range(L):
        for j in range(W):
            visit[i][j] = 0


def bfs(start):
    x,y= start

    que = deque()
    que.append( (x,y) )
    visit[x][y] = 1
    temp_max = 0

    while que:
        x,y=que.popleft()
        
        for i in range(4):
            n_x = x+ dx[i]
            n_y = y+ dy[i]
            if check_range(n_x,n_y) and grid[n_x][n_y]=='L' and visit[n_x][n_y]==0: 
                que.append((n_x,n_y))
                visit[n_x][n_y] = visit[x][y] + 1
                temp_max = max(temp_max,visit[n_x][n_y])
    
    return temp_max

max_answer=1
# 2중 for문 자체가 느린가?
land = [(i,j) for j in range(W) for i in range(L) if grid[i][j]=='L' ]


if len(land)==W*L:
    #전처리.
    print(W+L-2)
else:
    for i,j in land:
            if grid[i][j]=='L':
                temp_max=bfs((i,j))
                max_answer = max(max_answer, temp_max)
                visit = [[0]*W for _ in range(L)]
                #clear()

    print(max_answer-1)



# https://letzgorats.tistory.com/entry/%EB%B0%B1%EC%A4%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98pythonjava-2589%EB%B2%88-%EB%B3%B4%EB%AC%BC%EC%84%AC
