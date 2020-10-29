T = int(input())
for t in range(1, T+1):
    N = int(input())
    time = [(end - start, start, end) for start, end in [list(map(int, input().split())) for _ in range(N)]]
    result = 0
    schedule = [0] * 25
    time.sort()
    for diff, start, end in time:
        for i in range(diff):
            if schedule[start+i] == 1:
                break
        else:
            for i in range(diff):
                schedule[start+i] = 1
            result += 1
    print('#{} {}'.format(t, result))
