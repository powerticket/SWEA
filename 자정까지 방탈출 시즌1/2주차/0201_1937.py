# 02/01
# 1937 욕심쟁이 판다쉑

import sys
sys.setrecursionlimit(1000000)

# dp 배열을 만들어서 dp 배열 존재 시 바로 반환
# 해당 dp 배열 값과 다음 대나무에서의 수명 + 1을 비교
def dfs(r, c):
    if visited[r][c]:
        return visited[r][c]
    visited[r][c] = 1
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if arr[nr][nc] > arr[r][c]:
                visited[r][c] = max(visited[r][c], dfs(nr, nc) + 1)
    return visited[r][c]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result = max(result, dfs(i, j))

print(max(map(max, visited)))
