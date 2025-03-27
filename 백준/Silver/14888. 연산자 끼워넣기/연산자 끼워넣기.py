import sys

sys.setrecursionlimit(100000)


N = int(input())
num_lst = list(map( int,input().split() ))
operator_count = list(map( int,input().split() ))


min_answer = sys.maxsize
max_answer = -sys.maxsize

def calc(oper_id, num1,num2):
    if oper_id==0:
        #+,-,*,/
        return num1+num2
    elif oper_id==1:
        return num1-num2
    elif oper_id==2:
        return num1*num2
    else:
        if num1 <0:
            num1_oper = -1
            num1=-num1
        else:
            num1_oper =1
        
        if num2 <0:
            num2_oper = -1
            num2 = -num2
        else:
            num2_oper = 1

        return (num1//num2)*num1_oper*num2_oper


def go(here,result):
    global min_answer
    global max_answer
    
    if here == N-1:
        min_answer = min(min_answer,result)
        max_answer = max(max_answer,result)
        return


    for i in range(4):
        if operator_count[i]<=0:
            continue
        
        operator_count[i] -= 1
        now_res = calc(i,result,num_lst[here+1])
        #print(now_res)
        go(here+1,now_res)
        operator_count[i] += 1

    return


go(0,num_lst[0])


print(max_answer)
print(min_answer)



