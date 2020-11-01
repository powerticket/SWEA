def dfs(n, cur_percent):
    # base
    if n == N:
        global max_percent
        if cur_percent > max_percent:
            max_percent = cur_percent
        return
    # pruning
    if cur_percent <= max_percent:
        return
    # visiting
    for i in range(N):
        if visited[i]:
            visited[i] = 0
            dfs(n+1, cur_percent*work[n][i]/100)
            visited[i] = 1    


T = int(input())
for t in range(1, T+1):
    N = int(input())
    visited = [1] * N
    work = [list(map(int, input().split())) for _ in range(N)]
    max_percent = 0
    dfs(0, 1)
    max_percent *= 100
    print('#{} {}'.format(t, format(max_percent, '0.6f')))
