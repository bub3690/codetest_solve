from collections import deque


S = input()
s1 = input()
len_s1 = len(s1)

s_list = []
for v in S:
    s_list.append(v)
    if len(s_list) >= len_s1:
        #체크
        if "".join(s_list[-len_s1:]) == s1:
            del s_list[-len_s1:]

   
s_list="".join(s_list)
if len(s_list) ==0:
    print("FRULA")
else:
    print(s_list)




