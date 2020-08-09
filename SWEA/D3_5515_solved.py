T = int(input())
L = [i for i in range(7)]
for t in range(1, T+1):
    M, D = map(int, input().split())
    day = 0
    for i in range(1, M):
        if i in [4, 6, 9, 11]:
            day += 30
        elif i == 2:
            day += 29
        else:
            day += 31
    day += D
    print('#{} {}'.format(t, L[(day+3)%7]))