T = int(input())
for t in range(1, T+1):
    N = int(input())
    a = 1
    total = 0
    for i in range(1, N+1):
        total += a * i
        a *= -1
    print('#{} {}'.format(t, total))