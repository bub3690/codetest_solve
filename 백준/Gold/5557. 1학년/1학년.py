

# 숫자 개수 : 3<=N<=100 , 0이상 9이하의 숫자들 N개


# 모든 등식의수, 경우의수 찾기.
# N-2개 만큼 연산자 존재.
# 중간에 나오는 수가 모두 0~20 이어야한다. *** -> dp 가능.
# 마지막 두 숫자에는 무조건 = 이 들어간다. ***
# 결정해야할 요소는 N-3개.

# 시간제한 1초

# 완전탐색
# 연산자에 무조건 =이 있어야한다.
# 백트래킹 문제.
# 가능한 연산 +,- (1,2)  = : 0
# 2^100이므로 dp를 사용


N = int(input())

grid = list(map(int,input().rstrip().split() ))


dp = [ [-1]*21 for _ in range(N+1)  ]

def go(here,res):

    #기저
    if res<0 or res>20:
        return 0

    if here==N-1:
        if grid[here] == res:
            return 1
        else:
            return 0
    
    
    if dp[here][res] != -1:
        return dp[here][res]
    
    #+
    case1 = go(here+1, res+grid[here])
    #-
    case2 = go(here+1, res-grid[here])

    dp[here][res] = case1+case2
    return dp[here][res]


res=go(1,grid[0])
print(res)




