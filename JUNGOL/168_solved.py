N = int(input())
l = [[0] * N for _ in range(N)]
l[0][0] = 1
for i in range(1, N):
    for j in range(N):
        if j > 0:
            l[i][j] += l[i-1][j-1]
        l[i][j] += l[i-1][j]
for i in range(N-1, -1, -1):
    for j in range(i+1):
        print(l[i][j], end=' ')
    print()