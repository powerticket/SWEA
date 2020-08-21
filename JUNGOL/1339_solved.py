N = int(input())
if not 0 < N < 100 or N % 2 == 0:
    print("INPUT ERROR")
else:
    M = N // 2 + 1
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = 0
    l = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(M-1-i, M-i+2*i):
            l[i][j] = alpha[idx%26]
            idx += 1
    for i in range(N):
        for j in range(M-1, -1, -1):
            if l[j][i] == 0:
                break
            print(l[j][i], end=' ')
        print()