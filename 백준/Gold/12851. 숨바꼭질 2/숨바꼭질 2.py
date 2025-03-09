
from collections import deque



N,K = tuple(map(int,input().split()))

# bfs : O(N) 알고리즘이다. 그런데 간선이 생겨서. O(V+E)

# 최단거리 + 경우의수 문제.
dist = [-1]*100001 # visit과 같다. 
count = [0]*100001 #최단거리일때 count를 담음.


def bfs(here):
    global dist
    global count

    que = deque()
    que.append( here )
    while que:
        now = que.popleft()

        for next in [now*2,now-1,now+1]:
            if next>=0 and next<=100000:
                #방문 하지 않았다면.
                if dist[next] ==-1:
                    dist[next] = dist[now]+1
                    count[next] += count[now] # now까지 온 모든 경우의수를 합 한것과 같다.
                    que.append(next)
                elif dist[next] == dist[now]+1:
                    #이미 방문되었지만. 최소값과 같다면.
                    count[next] += count[now]
                
dist[N] = 0
count[N] = 1

bfs(N)

print(dist[K])
print(count[K])


