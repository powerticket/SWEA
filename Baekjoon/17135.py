import sys
from itertools import combinations
from collections import deque


def move(stage):
    for i in range(M):
        for j in range(N-1, 0, -1):
            enemy[j][i] = enemy[j-1][i]
    if stage == 0:
        for i in range(M):
            enemy[0][i] = 0


dr = [0, -1, 0]
dc = [-1, 0, 1]
N, M, D = map(int, sys.stdin.readline().split())
enemy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
comb = list(combinations(range(N), 3))
visited = [[0] * M for _ in ' '*N]
shot = [[0] * M for _ in ' '*N]
q = deque()
shot_clear = deque()
result = 0
for stage in range(N):
    max_kill = 0
    for archers in comb:
        kill = 0
        for archer in archers:
            q.append((N, archer))
            dist = 0
            len_q = len(q)
            cnt = 0
            while q:
                if len_q == cnt:
                    len_q = len(q)
                    cnt = 0
                    dist += 1
                if dist == D:
                    q.clear()
                    break
                cnt += 1
                r, c = q.popleft()
                for d in range(3):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        if enemy[nr][nc]:
                            if not shot[nr][nc]:
                                kill += 1
                                shot[nr][nc] = 1
                                shot_clear.append((nr, nc))
                            q.clear()
                            break
                        q.append((nr, nc))
            while shot_clear:
                r, c = shot_clear.popleft()
                enemy[r][c] = 0
                shot[r][c] = 0
        if kill > max_kill:
            max_kill = kill
    result += max_kill
    move(stage)
print(result)
