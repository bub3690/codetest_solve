import sys

sys.setrecursionlimit(100000)

N= int(input())


dp = [sys.maxsize]*(10**6+2) # 128mb보다 큰가? # 128mb보다 큰가?
#dp = {}


def trace(here):
    print(here,end=' ')
    if (here%3==0) and (dp[here] == dp[here//3]+1):
        trace(here//3)
    elif (here%2==0) and (dp[here] == dp[here//2]+1):
        trace(here//2)
    elif (here-1 > 0):
        trace(here-1)
    return


# 백만 하면 리컬전이 너무 크다.
def go(here):
    #print(here)

    if here == 1:
        dp[here] = 0
        return 0
    
    if dp[here] != sys.maxsize:
        return dp[here]
    
    
    answer = sys.maxsize
    if (here%3==0) and (here%2==0):
        answer = min( go(here//3)+1, go(here//2)+1) 
    elif here%3 == 0:
        answer = min( go(here//3)+1, go(here-1)+1) 
    elif here%2 == 0:
        answer = min( go(here//2)+1, go(here-1)+1)
    else:
        answer = go(here-1)+1 # 여기가 문젠가?

    dp[here] = answer
    return answer


go(N)

print(dp[N])
trace(N)

