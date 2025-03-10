from collections import deque


# dist
# pre  -> 오기전에 어떤 배열에서 왔는지.

N,K = tuple(map(int,input().split() ))

dist = [-1]*100005
pre = [0]*100005


def bfs(here):
    que = deque()
    que.append(here)

    while que:
        now = que.popleft()
        
        for next in [now+1,now-1,now*2]:
            if 0<=next<=100000:
                if dist[next] == -1:
                    dist[next] = dist[now]+1
                    #경로 적어두기.
                    pre[next] = now
                    que.append(next)


dist[N] = 0
bfs(N)

print(dist[K])
# 경로를 따라서 출력.
arrive_list = deque()
now_pos = K
arrive_list.append(now_pos)
while now_pos!=N:
    temp=pre[now_pos]
    arrive_list.append(temp)
    now_pos = temp
while arrive_list:
    print(arrive_list.pop(),end=' ')
