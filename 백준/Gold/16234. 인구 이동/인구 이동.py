import sys

sys.setrecursionlimit(100000)



N,L,R = tuple(map(int, input().split()))

grid = [ list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N) ]


dx=[0,1,0,-1]
dy=[1,0,-1,0]

def range_check(x,y):
    return x >=0 and x<N and y>=0 and y<N

def check_movement(x,y, next_x,next_y):
    
    distance = abs(grid[x][y]-grid[next_x][next_y]) 
    return distance >= L and distance <= R



def dfs(x,y):
    
    # 이동할 이웃이 없다면. 알아서 종료.
    lazy_sum = grid[x][y]
    lazy_num = 1

    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if range_check(next_x,next_y) and check_movement(x,y,next_x,next_y) and visit[next_x][next_y]==0 :
            visit[next_x][next_y] = lazy_count
            temp_lazy_sum, temp_lazy_num = dfs(next_x,next_y)

            lazy_sum += temp_lazy_sum
            lazy_num += temp_lazy_num
    
    return lazy_sum, lazy_num




# 연결요소 찾기. lazy 배열 삽입.

#변경이 발생안할때까지.


answer = 0
while(1):
    lazy_count = 1
    lazy_arr = []
    # visit 초기화.
    for i in range(N):
        for j in range(N):
            visit[i][j] = 0 

    for i in range(N):
        for j in range(N):
            if visit[i][j] ==0:
                lazy_sum = 0
                visit[i][j]= lazy_count
                lazy_sum, lazy_num = dfs(i,j)
                #print(lazy_sum,lazy_num)
                lazy_count += 1
                lazy_arr.append(lazy_sum//lazy_num)

    # 만약 lazy_count 가 n^2같다면 더 변경안된 것이니. 현재 반복문의 -1이 정답.
    if lazy_count -1 == N**2:
        break

    # lazy에 맞게 평균값 할당.
    for i in range(N):
        for j in range(N):
            grid[i][j] = lazy_arr[visit[i][j]-1]
            #print(grid[i][j],end=' ')

    answer += 1    

print(answer)

