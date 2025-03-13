import sys
sys.setrecursionlimit(100000)


R,C = tuple(map(int,input().split()))

grid = [ list(input().strip()) for _ in range(R)]

visit = [[-1]*C for _ in range(R) ]

# print( ord('Z')- ord('A') )
dxs= [0,1,0,-1]
dys= [1,0,-1,0]

def range_check(x,y):
    return 0<=x<R and 0<=y<C


answer = -1
find_answer= False
def go(here,count):
    global answer
    global find_answer
    now_x, now_y = here

    answer = max(answer,count)

    if answer>=26:
        find_answer = True
        return
    
    for i in range(4):
        next_x = now_x+dxs[i]
        next_y = now_y+dys[i]

        if range_check(next_x,next_y):
            if grid[next_x][next_y] not in check_set:
                check_set.add(grid[next_x][next_y])
                go( (next_x,next_y), count+1)
                
                if find_answer:
                    break

                check_set.remove(grid[next_x][next_y])



check_set = set()
check_set.add(grid[0][0])
go((0,0),1)

print(answer)





