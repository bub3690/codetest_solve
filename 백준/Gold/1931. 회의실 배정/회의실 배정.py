


N = int(input())
lst = [ list(map(int,input().split())) for _ in range(N)]

# 순서 바꾸기.
for i in range(N):
    i_from,i_to = lst[i]
    lst[i][0] = i_to
    lst[i][1] = i_from

lst.sort()


last_to  = lst[0][0]
ret = 1
for i in range(1,N):
    now_to, now_from = lst[i]

    if now_from < last_to:
        continue
    
    last_to = now_to
    ret+=1

print(ret)



