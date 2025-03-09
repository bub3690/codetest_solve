import sys
sys.setrecursionlimit(100000)


N = int(input())
arrs = list(input())

num_arr = [0]*20
oper_arr = [0]*20

opers = ['+','-','*']

oper_count=0
num_count=0
for i in range(N):
    if arrs[i] in opers:
        oper_arr[oper_count]=arrs[i]
        oper_count+=1
    else:
        num_arr[num_count]=int(arrs[i])
        num_count += 1


max_val = -987654321


def oper_calc(num1,num2,oper):
    res = 0
    if oper == '+':
        res = num1+num2
    elif oper =='-':
        res = num1-num2
    else:
        res = num1*num2
    
    return res


def go(here, pre_sum):
    global max_val
    #종료 조건.
    if here >= num_count-1:
        max_val = max(max_val,pre_sum)
        return

    # 바로 앞에걸 더할지. 뒤에 2개 먼저 더할지 경우의수 2개.
    go(here+1 , oper_calc(pre_sum, num_arr[here+1], oper_arr[here]) )
    if here+2 <= num_count-1:
        middle_res =oper_calc( num_arr[here+1],num_arr[here+2], oper_arr[here+1])
        go(here+2, oper_calc(pre_sum,middle_res,oper_arr[here]) )


go(0,num_arr[0]) # here pos, sum

print(max_val)





