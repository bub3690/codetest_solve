



N,K = tuple(map(int,input().split()))
arr = list( map(int,input().split()))
#arr = [i for i in range(200000)]

head = 0
tail = 0


mp = {}
answer = 0

for tail in range(N):
    mp[arr[tail]] = mp.get(arr[tail],0) +1

    while( mp[arr[tail]] >K ):
        mp[arr[head]] -=1
        head+= 1
    
    answer = max(answer,abs(tail-head)+1)



print(answer)





