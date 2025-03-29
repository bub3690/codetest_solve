import sys

input = sys.stdin.readline

N  = int(input())

lst = [ list(map(int,input().split())) for _ in range(N)]


lst.sort()

all_time = 0
for i in range(N):
    now_time, now_stop = lst[i]
    if all_time > now_time:
        all_time = all_time + now_stop
    else:
        all_time = now_time+ now_stop

print(all_time)

