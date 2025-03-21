
# 연결요소 내부 카운트?

# 2<=N<=100, 1<=M<5000
# M개 관계.양방향 관계.
# 번호는 1~N

# 캐빈 베이컨 수가 가장 작은 사람 출력.
# 모든 사람은 연결되어있다.
# 최소 케빈 베이컨 수 구하기

# BFS 방식으로 각 정점마다 카운트 구하기.
# 그냥 최단거리의 합 같은 문제같다.
# Visit N*N 배열로 선언하고 각 원소마다 최단거리 담기.

from collections import deque

N, M = tuple(map(int,input().split()))
friend_list=  [[] for _ in range(N+2)]

for i in range(M):
    f,t = tuple(map(int,input().split()))
    friend_list[f].append(t)
    friend_list[t].append(f)

visit = [ [-1]*(N+2) for _ in range(N+2)]

def bfs(i,visit):
    que = deque()
    que.append(i)
    visit[i][i] = 0

    while que:
        now_i = que.popleft()
        for next_i in friend_list[now_i]:
            if visit[i][next_i] == -1:
                visit[i][next_i] = visit[i][now_i] +1
                que.append(next_i)
    
    return

for i in range(1,N+1):
    bfs(i,visit)


result = []
for i in range(1,N+1):
    sum_temp = 0
    for j in range(1,N+1):
        sum_temp += visit[i][j]
    result.append((sum_temp,i))

result.sort()
print(result[0][1])




