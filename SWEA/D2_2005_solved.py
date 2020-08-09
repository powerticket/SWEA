T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = [[0] * (N+1) for _ in range(N+1)]
    L[0][0] = 1
    print('#{}'.format(t))
    for i in range(1, N+1):
        for j in range(1, i+1):
            L[i][j] = L[i-1][j-1] + L[i-1][j]
            print(L[i][j], end=' ')
        print()