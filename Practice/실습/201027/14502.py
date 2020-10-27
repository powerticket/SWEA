from itertools import combinations


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
zero = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
len_zero = len(zero)
max_safe = 0
comb = combinations(range(len_zero), 3)
for s1, s2, s3 in comb:
    for y, x in [zero[s1], zero[s2], zero[s3]]:
        arr[y][x] = 1
    cur_safe = len_zero - 3
    q = []
    visited = [[0] * M for _ in range(N)]
    for r, c in virus:
        q.append((r, c))
        visited[r][c] = 1
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cur_safe -= 1
                    if cur_safe < max_safe:
                        break
        else:
            continue
        break
    if cur_safe > max_safe:
        max_safe = cur_safe
    for y, x in [zero[s1], zero[s2], zero[s3]]:
        arr[y][x] = 0
print(max_safe)

# for s1 in range(len_zero):
#     for s2 in range(len_zero):
#         if s1 != s2:
#             for s3 in range(len_zero):
#                 if s1 != s3 and s2 != s3:
#                     for y, x in [zero[s1], zero[s2], zero[s3]]:
#                         arr[y][x] = 1
#                     cur_safe = len_zero - 3
#                     q = []
#                     visited = [[0] * M for _ in range(N)]
#                     for r, c in virus:
#                         q.append((r, c))
#                         visited[r][c] = 1
#                     while q:
#                         r, c = q.pop(0)
#                         for d in range(4):
#                             nr = r + dr[d]
#                             nc = c + dc[d]
#                             if 0 <= nr < N and 0 <= nc < M:
#                                 if arr[nr][nc] == 0 and not visited[nr][nc]:
#                                     q.append((nr, nc))
#                                     visited[nr][nc] = 1
#                                     cur_safe -= 1
#                                     if cur_safe < max_safe:
#                                         break
#                         else:
#                             continue
#                         break
#                     if cur_safe > max_safe:
#                         max_safe = cur_safe
#                     for y, x in [zero[s1], zero[s2], zero[s3]]:
#                         arr[y][x] = 0
# print(max_safe)