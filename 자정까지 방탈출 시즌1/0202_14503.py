# 02/02
# 14503 로봇 청소기

from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(N)]
# 북, 동, 남, 서
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
clean = [[0] * M for _ in range(N)]
q = deque([(r, c)])
# 1. 처음 위치를 청소한다.
clean[r][c] = 1
while q:
    r, c = q.popleft()
    # 2. 현재 위치부터 사방 탐색
    for _ in range(4):
        # Turn left
        d = (d - 1) % 4
        nr = r + direction[d][0]
        nc = c + direction[d][1]
        # 공간 내에 있고, 벽이 아닐 경우
        if 0 <= nr < N and 0 <= nc < M and not wall[nr][nc]:
            # 청소가 되어있지 않을 경우
            if not clean[nr][nc]:
                clean[nr][nc] = 1
                q.append((nr, nc))
                break
    else:
        # 전부 벽이거나 청소가 되어있을 경우 뒤로 후진
        d = (d - 2) % 4
        nr = r + direction[d][0]
        nc = c + direction[d][1]
        # 방향 다시 앞을 본다
        d = (d - 2) % 4
        # 범위 안에 있고 벽이 아닐 경우 q에 추가
        if 0 <= nr < N and 0 <= nc < M and not wall[nr][nc]:
            q.append((nr, nc))
            continue
        break
print(sum(map(sum, clean)))
