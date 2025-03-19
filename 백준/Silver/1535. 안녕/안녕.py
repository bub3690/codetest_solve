import sys

input = sys.stdin.readline


N = int(input())
hp_list = list(map(int,input().split()))
joy_list = list(map(int,input().split()))

dp = [0] *105  # hp dp

# hp_list,joy_list=zip(*sorted(zip(hp_list,joy_list)))

# hp_list = list(hp_list)
# joy_list = list(joy_list)


max_answer = 0
for attack_idx,attack in enumerate(hp_list):
    for hp in range(100,attack,-1): ## 여기서 주의! 0이되면 행복안차게
        dp[hp] = max(dp[hp], dp[hp-attack]+ joy_list[attack_idx] )
        max_answer = max(max_answer,dp[hp])

print(max_answer)




