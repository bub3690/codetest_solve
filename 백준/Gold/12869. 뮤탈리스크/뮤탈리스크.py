# 공격이 9 3 1 로 전파될때. 누구먼저 치면 최소인지 찾는. 순열문제?..

import sys
from collections import deque

N=int(input())
arrs = list(map(int,input().split()))

len_arr = len(arrs)

result = 99999
#temp_arrs=[]
attack_dmg = [
    [9,3,1],
    [9,1,3],
    [3,9,1],
    [3,1,9],
    [1,9,3],
    [1,3,9]
]



def bfs(hp_arr):
    global result
    que=deque()
    que.append((hp_arr,0))
    visited= set()

    while que:
        now_hp_arr,depth = que.popleft()
        
        check= True

        for j in range(N):
            if now_hp_arr[j] >0:
                check=False
        if check:
            result = min(result, depth)
            break

        for i in range(6):
            # 조건으로 j가 0인부분에 9가 있는 i 빼버리기.

            temp_hp_arr = [0,0,0]
            for j in range(N):
                temp_hp_arr[j] = max(0,now_hp_arr[j]-attack_dmg[i][j])

            #print(temp_hp_arr,depth)
            hash_id = tuple(temp_hp_arr)
            if hash_id not in visited:
                que.append((temp_hp_arr,depth+1))
            visited.add(hash_id)

        



bfs(arrs)

print(result)





