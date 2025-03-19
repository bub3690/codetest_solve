import sys
import copy

input = sys.stdin.readline
N,M,K = tuple(map(int,input().split()))

A = [ list(map(int,input().split())) for _ in range(N) ] # 양분
dp = [ [ [] for _ in range(N+1) ] for _ in range(N+1) ]
dp2 = [ [ 5 for _ in range(N)] for _ in range(N) ]

tree_list = [ tuple(map(int,input().split())) for _ in range(M) ]

for tree in tree_list:
    x,y,age = tree
    x = x-1
    y = y-1
    dp[x][y].append(age)

def spring_summer():
    for i in range(N):
        for j in range(N):
            if len(dp[i][j]) ==0:
                continue

            dp[i][j].sort() #어린것 부터 먹이기.
            kill_tree_sum = 0
            temp = []
            for tree_id,tree in enumerate(dp[i][j][:]):
                if tree> dp2[i][j]:
                    kill_tree_sum += tree//2
                    continue
                dp[i][j][tree_id] += 1 # 나이 먹기
                dp2[i][j] -= tree
                temp.append(dp[i][j][tree_id])
            # 나무 제거 하고 양분 주기.
            dp2[i][j] += kill_tree_sum
            dp[i][j] = temp

    return
 
dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

def check_range(x,y):
    return 0<=x<N and 0<=y<N

def fall():
    for i in range(N):
        for j in range(N):
            if len(dp[i][j]) ==0:
                continue
                
            for tree in  dp[i][j]:
                if tree % 5 == 0:
                    for d_ind in range(8):
                        next_x = i + dxs[d_ind]
                        next_y = j + dys[d_ind]
                        if check_range(next_x,next_y):
                            dp[next_x][next_y].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            dp2[i][j] += A[i][j]


for i in range(K):

    spring_summer()
    fall()
    winter()

answer= 0
for i in range(N):
    for j in range(N):
        answer += len(dp[i][j])

print(answer)



