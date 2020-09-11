dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_result = 0
    min_num = N ** 2
    for i in range(N):
        for j in range(N):
            result = 1
            queue = []
            queue.append((i, j))
            while queue:
                r, c = queue.pop(0)
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if A[nr][nc] - A[r][c] == 1:
                        queue.append((nr, nc))
                        result += 1
                        break
            if result > max_result:
                max_result = result
                min_num = A[i][j]
            if result == max_result:
                if A[i][j] < min_num:
                    min_num = A[i][j]
    print('#{} {} {}'.format(t, min_num, max_result))
