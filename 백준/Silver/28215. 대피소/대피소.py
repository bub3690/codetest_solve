import sys
sys.setrecursionlimit(1000000)


N, K = tuple(map(int,input().split()))
homes = [ list( map(int,input().split()) ) for _ in range(N) ]
# N개 집. (x,y).


# 1. nCk 조합 샘플링. dfs 방식
# 2. 각 조합마다 max_dist 구해주기.

temp_combination = []
min_answer = float('INF')
def combination(here, depth):
    global min_answer

    if depth==K:

        # 모든 집과 거리를 계산.
        max_house_temp = 0
        for i in range(N):
            # i는 모든집. 
            # i가 K개안에 선정되었다면 넘어가야함.
            if i in temp_combination:
                continue

            min_answer_temp = float('INF')
            for j in range(K):
                dist_x = abs(homes[i][0] - homes[temp_combination[j]][0])
                dist_y = abs(homes[i][1] - homes[temp_combination[j]][1])
                dist_xy = dist_x + dist_y
                min_answer_temp = min(min_answer_temp, dist_xy) # 가장 가까운 대피소 거리.
            
            # 그리고 모든 집들중에 최대 거리 찾고.
            max_house_temp = max(max_house_temp, min_answer_temp)
            
        # 최대거리중 최소값 업데이트
        min_answer = min(min_answer, max_house_temp)
        return

    #home을 뽑고 그다음. 집을 선택하는 dfs
    for i in range(here,N):
        temp_combination.append(i)
        combination(i+1,depth+1)#그 다음 집들 선택하러가기.
        temp_combination.pop() #원상복구. i부분이 선택 안됬을 경우로.

    return

combination(0,0)

print(min_answer)




