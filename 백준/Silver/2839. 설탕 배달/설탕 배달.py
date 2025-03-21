
# 정확히 n개 배달 하는 방법.

# 인풋
# 3<=N<=5000

# 최소 봉지 개수. N개 못하면 -1

#알고리즘
# DP? 개수가 무한인 DP -> 아닌것 같다. 정확히 맞아야해서.
# 그냥 그리디로 푼다.
# 5부터 최대값으로하나씩 내려가면서 맞춰보는 방식으로

# 시간 1초




N = int(input())

start_5 = N//5
start_3 = 0

# 5를 0까지 내려도 안될경우.
answer = 9999999
while start_5 != -1:
    remain = N-start_5*5
    if remain % 3 ==0:
        start_3 = remain//3
        answer = min(answer,start_3+start_5)
    start_5 -= 1


if answer == 9999999:
    print(-1)
else:
    print(answer)






