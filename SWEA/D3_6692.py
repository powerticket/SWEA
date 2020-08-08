T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = [list(map(float, input().split())) for _ in range(N)]
    total = 0
    for i in range(len(L)):
        total += L[i][0] * L[i][1]
    print('#{} {:.6f}'.format(t, total))