import sys


dat = input().strip().upper()

counter = {}

for v in dat:
    
    counter[v] = counter.get(v,0) + 1


max_val = 0
for char,val in counter.items():
    max_val = max(max_val,val)

duplicated = 0
res = ''
for char,val in counter.items():
    if max_val == val:
        duplicated +=1
        res = char

if duplicated>=2:
    print("?")
else:
    print(res)




