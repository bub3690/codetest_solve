import sys
from collections import deque

# 입력 받기
R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

# 방향 벡터 (우, 하, 좌, 상)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 범위 체크 함수
def range_check(x, y):
    return 0 <= x < R and 0 <= y < C

# 스택을 이용한 DFS
def stack_based_dfs():
    max_count = 1  # 최대 탐색 깊이
    stack =deque() # (x, y, count, visited_mask)
    stack.appendleft((0, 0, 1, 1 << (ord(grid[0][0]) - ord('A')) ))
    
    while stack:
        
        x, y, count, visited_mask = stack.popleft()
        max_count = max(max_count, count)

        if max_count == 26:  # 모든 알파벳을 방문했을 경우
            return 26

        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if range_check(nx, ny):
                char_idx = ord(grid[nx][ny]) - ord('A')
                if not (visited_mask & (1 << char_idx)):  # 방문한 적 없는 알파벳이면
                    stack.appendleft((nx, ny, count + 1, visited_mask | (1 << char_idx)))

    return max_count

# 결과 출력
print(stack_based_dfs())
