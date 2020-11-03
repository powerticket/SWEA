def find(k, percent):
    if k == N:
        global maxV
        if percent > maxV:
            maxV = percent
            return
    if percent <= maxV:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            find(k+1, percent * p[k][i])
            visited[i] = False


T = int(input())
for t in range(1, T+1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j] /= 100
    sel = [0] * N
    visited = [False] * N
    maxV = 0
    find(0, 1)
    print('#{} {:.6f}'.format(t, maxV*100))
