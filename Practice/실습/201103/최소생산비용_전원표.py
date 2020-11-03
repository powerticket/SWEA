def permutation(k, cur_sum):
    global min_sum
    if cur_sum >= min_sum:
        return
    if k == N:
        if cur_sum < min_sum:
            min_sum = cur_sum
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            permutation(k+1, cur_sum+factory[k][i])
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 0xffffffff
    permutation(0, 0)
    print('#{} {}'.format(t, min_sum))
