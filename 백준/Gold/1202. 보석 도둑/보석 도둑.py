import heapq
import sys

input = sys.stdin.readline


N,K = tuple(map(int,input().split() ))

v_lst = [ list(map(int,input().split()))  for _ in range(N)]
k_lst =  [ int(input())  for _ in range(K)]

v_lst.sort()
k_lst.sort()


pq_list = []


j=0
ans =0 
for i in range(K):
    
    # 가능한 모든 돌들 검사.
    while j<N and v_lst[j][0]<=k_lst[i]:
        heapq.heappush(pq_list, -v_lst[j][1])
        j += 1
    
    # 최상단 하나 뽑기
    if pq_list:
        ans += -heapq.heappop(pq_list)

print(ans)



