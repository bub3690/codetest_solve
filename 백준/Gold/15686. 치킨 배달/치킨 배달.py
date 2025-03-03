import sys
sys.setrecursionlimit(10000000)



N, M = tuple( map(int,input().split()) )
grid = [ list(map(int,input().split())) for _ in range(N) ]


chicken = []
home = []

# 1. 집 찾기.
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            home.append((i,j))
        elif grid[i][j] == 2:
            chicken.append((i,j))

len_chicken = len(chicken)
len_home = len(home)
# 2. 어떤 치킨집을 뺄건지. 조합 생성해내기.
# 조합만드는 건 속도가? o(2^m) 

combination_chickens = [] # 조합들을 담아둠.
temp_chickens = []
def combination(here):

    if here==len_chicken:
        return
    
    # 원하는 사이즈 m이 되면 종료.
    if len(temp_chickens) == M:
        combination_chickens.append(temp_chickens[:])
        return

    temp_chickens.append(here+1)
    combination(here+1)
    temp_chickens.pop()
    combination(here+1)

combination(-1)


#3. 구해진 조합들을 가지고 최소 거리 구하기.
# 속도: 집 개수 최대 100개. 100* 13 C m. 최대 100 * 13C6

len_combination = len(combination_chickens)
min_answer = 99999999
for i in range(len_combination):
    temp_res = 0
    for j in range(len_home):
            # 각 집마다 최소가 되는 치킨집 찾고 합해주기.
            min_chicken_temp = 9999999
            for chicken_home in combination_chickens[i]:
                dist_x = abs(home[j][0] - chicken[chicken_home][0] )
                dist_y = abs(home[j][1] - chicken[chicken_home][1] )
                sum_dist = dist_x+dist_y
                min_chicken_temp = min(min_chicken_temp,sum_dist)
            temp_res += min_chicken_temp
    
    min_answer = min(min_answer,temp_res)

print(min_answer)



