

N= int(input())

grid = [  list(map(int,input().split())) for _ in range(N)] 

dp = [  [ [0]*(3) for _ in range(N+1)] for _ in range(N+1) ]




def check(i,j,dir):
    if 0<=i<N and 0<= j<N:
        if dir==0 or dir==1: 
            if grid[i][j] == 0:
                return True
        elif dir==2:
            if grid[i][j]==0 and grid[i-1][j]==0 and grid[i][j-1]==0:
                return True
        
    return False

dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        # 체크하고 가로 일때 된 경우들
        if check(i,j+1,0): 
            dp[i][j+1][0] += dp[i][j][0]
        if check(i+1,j+1,2):
            dp[i+1][j+1][2] += dp[i][j][0]
        
        # 세로로 올 경우
        if check(i+1,j,1):
            dp[i+1][j][1] += dp[i][j][1]
        if check(i+1,j+1,2):       
            dp[i+1][j+1][2] += dp[i][j][1]

        #대각선 시작일경우.
        if check(i,j+1,0):       
            dp[i][j+1][0] += dp[i][j][2]
        if check(i+1,j,1):
            dp[i+1][j][1] += dp[i][j][2]
        if check(i+1,j+1,2):
            dp[i+1][j+1][2] += dp[i][j][2]

#print(dp)
result = dp[N-1][N-1][0]+dp[N-1][N-1][1]+dp[N-1][N-1][2]
print(result)










