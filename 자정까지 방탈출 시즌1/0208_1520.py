import sys
sys.stdin = open('0208_1520.txt', 'r')

# 02/08
# 1520 내리막 길

import sys
sys.setrecursionlimit(1000000)


def find_path(r, c):
    # 목적지에 도달하면 1 반환
    if r == M - 1 and c == N - 1:
        return 1
    # 방문한 적이 있으면 해당 값 반환
    if visited[r][c] != -1:
        return visited[r][c]
    # 방문 표시
    visited[r][c] = 0
    # 사방 탐색
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < M and 0 <= nc < N:
            # 해당 좌표에서 갈 수 있는 방법은 네 방향에서 갈 수 있는 방법의 합
            if arr[nr][nc] < arr[r][c]:
                visited[r][c] += find_path(nr, nc)
    return visited[r][c]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]
print(find_path(0, 0))
