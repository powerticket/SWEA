import sys
sys.stdin = open('0310_14502.txt', 'r')

# 03/10
# 14502 연구소

from itertools import combinations

# 바이러스 확산 재귀
def spread(r, c):
    arr[r][c] = 2
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                spread(nr, nc)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
# 빈 공간 및 바이러스 위치 확인
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))
max_safe = 0
# 빈 공간에 벽을 3개 세울 수 있는 조합 생성
candidate = combinations(empty, 3)
# 벽을 3개 세울 수 있는 모든 경우의 수 순회
for wall in candidate:
    # 벽 세우기
    for r, c in wall:
        arr[r][c] = 1
    # 바이러스 확산
    for r, c in virus:
        spread(r, c)
    # 안전 지역 계산 및 바이러스 제거
    safe = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safe += 1
            elif arr[i][j] == 2:
                arr[i][j] = 0
    # 안전 지역 갯수 확인
    if safe > max_safe:
        max_safe = safe
    # 벽 원복
    for r, c in wall:
        arr[r][c] = 0
print(max_safe)
