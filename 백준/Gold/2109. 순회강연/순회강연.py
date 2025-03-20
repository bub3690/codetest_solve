import heapq


N = int(input())

col_list = []
for i in range(N):
    price,day = tuple(map(int,input().split()))
    col_list.append((day,price))

col_list.sort()


price_list = []
for i in range(N):
    heapq.heappush(price_list,col_list[i][1])
    if len(price_list) > col_list[i][0]:
        heapq.heappop(price_list)

result = 0
for v in price_list:
    result+=v

print(result)



