from collections import deque
from itertools import combinations


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    store = deque()
    S = 0
    min_res = 200 * N
    for i in range(N):
        for j in range(N):
            if L[i][j] > 1:
                store.append((i, j))
                S += 1
                min_res += L[i][j]
    for i in range(1, S+1):
        for comb in combinations(store, i):
            res = 0
            q = deque(comb)
            v = [[0] * N for _ in range(N)]
            for r, c in comb:
                v[r][c] = 1
                res += L[r][c]
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if not v[nr][nc]:
                            if L[nr][nc] == 1:
                                res += v[r][c]
                            q.append((nr, nc))
                            v[nr][nc] = v[r][c] + 1
            if res < min_res:
                min_res = res
    print('#{} {}'.format(t, min_res))
