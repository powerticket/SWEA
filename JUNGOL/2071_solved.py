N, D = map(int, input().split())
l = [[0] * N for _ in range(N)]
l[0][0] = 1
for i in range(1, N):
    for j in range(N):
        if j > 0:
            l[i][j] += l[i-1][j-1]
        l[i][j] += l[i-1][j]
if D == 1:
    for i in range(N):
        for j in range(i+1):
            print(l[i][j], end=' ')
        print()
elif D == 2:
    for i in range(N-1, -1, -1):
        print(' '*(N-i-1), end='')
        for j in range(i+1):
            print(l[i][j], end=' ')
        print()
else:
    for i in range(N):
        for j in range(i+1):
            print(l[-1-j][-1-i], end=' ')
        print()