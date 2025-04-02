
N = int(input())


# 에라토스 테네스의 체
prime_lst = []

lst = [i for i in range(N+1)]

for val in lst:
    if val <2 or val==0:
        continue

    temp_val = val
    multi = 2
    temp_val = val* multi
    while temp_val <=N:
        lst[temp_val]=0
        multi += 1
        temp_val = val* multi

for val in lst:
    if val != 0 and val>=2:
        prime_lst.append(val)


# 투포인터
left = 0
right = 0
len_prime = len(prime_lst)

answer = 0
temp_sum = 0
# 연속합?
while True:

    if temp_sum >= N:
        temp_sum -= prime_lst[left]
        left += 1
    elif right == len_prime:
        break # 답을 못찾은 경우
    else:
        temp_sum += prime_lst[right]        
        right += 1

    if temp_sum==N:
        answer += 1


print(answer)







