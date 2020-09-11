for t in range(1, int(input())+1):
    N = int(input())
    score = list(map(int, input().split()))

    visit = [[0] * (sum(score) + 1) for _ in range(N+1)]


    def dfs(k, s):
        if visit[k][s]:
            return
        visit[k][s] = 1
        if k == N:
            return
        else:
            dfs(k+1, s)
            dfs(k+1, s+score[k])
    dfs(0, 0)

    print('#{} {}'.format(t, sum(visit[N])))
