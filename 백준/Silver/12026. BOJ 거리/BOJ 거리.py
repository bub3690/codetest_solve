

# 입력 : 1<= N <= 1000
# 글자가 1번부터 순서대로

# 1번 -> N번까지 점프
# B,O,J 문자열
# K*K 에너지든다.
# B,O,J 순으로 밟을때. 최소 에너지값을 구하라

# DP[I]에서 앞을 돌아보며 dp[j]+거리 을 이용해서 구한다.
# N^2로 에너지가 제일 작게 DP를 만들어 나간다.

N = int(input())
blocks = list(input().rstrip())
visited = True
dp = list([1e9, not visited] for _ in range(N)) # 두칸만 만들기. *2와 같음.

dp[0][0],dp[0][1] = 0,True

for i in range(1, N):
    block=blocks[i]
    check_jump = '?'

    if block=='B':
        check_jump = 'J'
    elif block=='O':
        check_jump='B'
    else:
        check_jump='O'
    
    for j in range(i):
        if check_jump == blocks[j]:
            # j->i
            dp[i][0] = min(dp[i][0],dp[j][0]+pow(i-j,2))

            if dp[i][0] != 1e9:
                dp[i][1] = True

#print(dp)
if dp[N-1][1]:
    print(dp[N-1][0])
else:
    print(-1)





