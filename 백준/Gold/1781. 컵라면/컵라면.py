import heapq
from collections import deque


N = int(input())
item_list = [ list(map(int,input().split())) for _ in range(N)]


item_list.sort()
pq_list = []


score = 0
for now_dat in item_list:
    day = now_dat[0]
    val = now_dat[1]
    heapq.heappush(pq_list,val)
    score += val
    if len(pq_list) > day:
        # 빼줘야한다는 뜻.
        top=heapq.heappop(pq_list)
        score -= top

print(score)
    
    





