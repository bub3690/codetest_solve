import sys
sys.setrecursionlimit(100000)

K = int(input())
exp_list = input().split()
num_list = [-1]*11



min_val = sys.maxsize
max_val = -1

min_answer = sys.maxsize
max_answer = -1




def getnum(num_ls):
    ret = 0
    for i in range(K,-1,-1):

        if num_ls[i] ==-1:
            continue
        ret += num_ls[i]*(10**(K-i) )

    return ret

def get_str(num_ls):
    ret = ''
    for i in range(K+1):

        if num_ls[i] ==-1:
            continue
        ret += str(num_ls[i] )
    return ret

def check_val(idx):
    # 부등호 검사
    if idx ==0:
        return True
    
    if exp_list[idx-1] =='<':
        return num_list[idx-1]<num_list[idx] 
    
    elif exp_list[idx-1] =='>':
        return num_list[idx-1]>num_list[idx] 



def go(here):
    global max_answer
    global min_answer
    global max_val
    global min_val


    if here == K:
        now_ans= getnum(num_list)
        max_val = max(max_val,now_ans )
        min_val = min(min_val,now_ans )
        
        if max_val == now_ans:
            max_answer = get_str(num_list)
        if min_val == now_ans:
            min_answer = get_str(num_list)
        return


    for num in range(0,10):
        if num not in num_list:
            # 부등호가 성립하는지 체크.
            num_list[here+1] = num
            if check_val(here+1):
                go(here+1)
            num_list[here+1] = -1
    

    return



go(-1)
print(max_answer)
print(min_answer)


