from collections import deque

N,K = tuple( map(int,input().split()) )

visited = [[-1]*500002 for _ in range(2)]


visited[0][N] = 1

def bfs(N,K):
    que=deque()
    que.append(N)
    turn = 0
    b = K
    ok = False

    while que:
        b += turn
        if b> 500000:
            break
        if visited[turn%2][b] != -1:
            ok = True
            break
            
        q_size = len(que)
        for i in range(q_size):
            now = que.popleft()

            for next in [now-1,now+1,now*2]:
                if 0<=next<=500000:
                    if visited[(turn+1)%2][next] == -1:
                        visited[(turn+1)%2][next] = visited[ turn %2][now] +1 
                        que.append(next)
            
        turn +=1
    
    if ok:
        print(turn)
    else:
        print(-1)


bfs(N,K)



        




