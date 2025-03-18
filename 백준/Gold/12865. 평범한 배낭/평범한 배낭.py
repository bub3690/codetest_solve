import sys

input = sys.stdin.readline


N,K = tuple(map(int,input().split()))
weight_list = []
value_list = []

dp=[0]*100002

for i in range(N):
    W,V= tuple(map(int,input().split()))
    weight_list.append(W)
    value_list.append(V)

sorted_weight_list, sorted_value_list= zip(*sorted(zip(weight_list,value_list)))

sorted_weight_list = list(sorted_weight_list)
sorted_value_list = list(sorted_value_list)


#k무게에 최대는 아니기에 매번 최대를 찾자.
answer = 0
for item_idx in range(N):
    weight = sorted_weight_list[item_idx]
    value = sorted_value_list[item_idx]
    for j in range(K,weight-1,-1):
        dp[j] = max(dp[j-weight] + value, dp[j])
        answer = max(answer,dp[j])


print(answer)


