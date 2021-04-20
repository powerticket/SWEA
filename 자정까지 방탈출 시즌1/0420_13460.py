import sys
sys.stdin = open('0420_13460.txt', 'r')

# 04/20
# 13460 구슬 탈출 2

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
rr = rc = br = bc = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rr, rc = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            br, bc = i, j
            arr[i][j] = '.'
answer = -1
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = [(rr, rc, br, bc, 1)]
# bfs
while q:
    rr, rc, br, bc, depth = q.pop(0)
    # depth check
    if depth > 10:
        break
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # red move
        red_dist = 0
        nrr, nrc = rr, rc
        while 1:
            nrr += dr
            nrc += dc
            if 0 <= nrr < N and 0 <= nrc < M and arr[nrr][nrc] != '#':
                if arr[nrr][nrc] == 'O':
                    answer = depth
                    break
                red_dist += 1
            else:
                nrr -= dr
                nrc -= dc
                break
        # blue move
        blue_dist = 0
        nbr, nbc = br, bc
        while 1:
            nbr += dr
            nbc += dc
            if 0 <= nbr < N and 0 <= nbc < M and arr[nbr][nbc] != '#':
                if arr[nbr][nbc] == 'O':
                    answer = 0
                    break
                blue_dist += 1
            else:
                nbr -= dr
                nbc -= dc
                break
        # goal in check
        if answer != -1:
            if answer:
                break
            answer = -1
            continue
        # same point check
        if nrr == nbr and nrc == nbc:
            if red_dist > blue_dist:
                nrr -= dr
                nrc -= dc
            else:
                nbr -= dr
                nbc -= dc
        if visited[nrr][nrc][nbr][nbc]:
            continue
        # visiting
        visited[nrr][nrc][nbr][nbc] = 1
        # enqueue
        q.append((nrr, nrc, nbr, nbc, depth+1))
    else:
        continue
    break
print(answer)
