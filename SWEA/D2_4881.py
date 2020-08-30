def min_sum(r, c, total, visited):
    visited = visited[:]
    total += L[r][c]
    global ms
    if total >= ms:
        return
    visited[c] = 1
    if r == N-1:
        if total < ms:
            ms = total
    for i in range(N):
        if not visited[i]:
            min_sum(r+1, i, total, visited)


for t in range(1, int(input())+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    ms = 9 * N
    visited = [0] * N
    for i in range(N):
        min_sum(0, i, 0, visited)
    print('#{} {}'.format(t, ms))