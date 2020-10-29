def perm(k):
    if k == N-1:
        candidate.append(field + [0])
    else:
        for i in range(k, N):
            field[k], field[i] = field[i], field[k]
            perm(k+1)
            field[k], field[i] = field[i], field[k]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    golfmap = [list(map(int, input().split())) for _ in range(N)]
    field = list(range(N))
    candidate = []
    perm(1)
    min_battery = 100 * N ** 2
    for arr in candidate:
        battery = 0
        for i in range(N):
            start, end = arr[i], arr[i+1]
            battery += golfmap[start][end]
        if battery < min_battery:
            min_battery = battery
    print('#{} {}'.format(t, min_battery))
