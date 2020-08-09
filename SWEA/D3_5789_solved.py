T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())
    ls = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            ls[j] = i
    print('#{} '.format(t), end='')
    for l in ls:
        print(l, end=' ')
    print()