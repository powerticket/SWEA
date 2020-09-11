for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for c in range(N):
        obstacle = 0
        for r in range(N):
            if arr[r][c] ==  0:
                continue
            elif arr[r][c] == 2 and obstacle == 0:
                continue
            elif arr[r][c] == 2 and obstacle != 0:
                cnt += 1
                obstacle = 0
            elif arr[r][c] == 1:
                obstacle += 1
    print('#{} {}'.format(t, cnt))
