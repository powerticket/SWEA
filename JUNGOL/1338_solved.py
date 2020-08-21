N = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx = 0
l = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        l[i][j] = alpha[idx%26]
        idx += 1
for i in range(N):
    print('  '*(N-i-1), end='')
    for j in range(i+1):
        print(l[j][i], end=' ')
    print()