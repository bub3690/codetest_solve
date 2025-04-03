import sys


input = sys.stdin.readline
N = int(input())
lst = list( map(int,input().split()) )



left = 0 
right = 0


ret = 0
cnt = {}

while right<N:
    # 만약 lst[right]가 [s,right)에서 처음 등장하는 원소면
    if cnt.get(lst[right],0) ==0:
        cnt[lst[right]] =1
        right +=1
    else:
        # 중복이 발생시.
        # 지금까지 구간에서 만들 수 있는 경우의 수 더하기.
        ret += (right-left)
        cnt[lst[left]] -= 1
        left += 1

#마지막 남은 구간계산
ret += (right-left)*(right-left+1)//2

print(ret)





