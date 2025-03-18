import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


N,M,C = tuple(map(int,input().split()))
N = N
M = M
C = C

pc_list = []
for i in range(C):
    pc_x,pc_y = tuple(map(int,input().split()))
    pc_x = pc_x-1
    pc_y = pc_y-1
    pc_list.append((pc_x,pc_y))

#쉽게 그리드 형태로
grid = [[0]*51 for _ in range(51)] 
for i,pos in enumerate(pc_list):
    x,y = pos
    grid[x][y] = i+1


dp = [ [  [  [ -1 for _ in range(51) ] for _ in range(51)] for _ in range(51)]  for _ in range(51)]


mod = 1000007
#cnt는 앞으로 몇개 pc 더 방문해야하는지
def go(here,cnt,prev ):
    x,y =here
    # 방문 가능한 구역인지 체크.
    if x>= N or y>=M : return 0

    #기저
    if x==N-1 and y==M-1:
        # cnt를 다쓰고 방문지가 문제없는지.
        # prev에 대한 기저도.
        if cnt ==0 and grid[x][y]==0 : return 1
        
        #pc방과 겹칠때. prev보다 높은 위치여야함.
        if cnt ==1 and grid[x][y]>prev : return 1

        return 0

         
    #메모
    if dp[x][y][cnt][prev] != -1:
        return dp[x][y][cnt][prev]

    # 여기 구역에 들어가는 코드.
    ret = 0
    if grid[x][y]==0:# 오락실 아니면
        ret = (go( (x+1,y),cnt,prev) + go( (x,y+1),cnt,prev))%mod
    elif grid[x][y]>prev:
        ret = (go( (x+1,y),cnt-1, grid[x][y]) + go( (x,y+1),cnt-1, grid[x][y]))%mod

    
    dp[x][y][cnt][prev] = ret

    # 잘못 들어온 구역이면 0으로 나감.
    return ret


for i in range(C+1):
    print(go((0,0),i,0),end=' ') # xy c prev




