def palin(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    L = [list(input()) for _ in range(N)]
    L_reverse = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            L_reverse[i][j] = L[j][i]
    for i in range(N):
        for j in range(N-M+1):
            if palin(L[i][j:j+M]):
                print('#{} {}'.format(t, ''.join(L[i][j:j+M])))
            if palin(L_reverse[i][j:j+M]):
                print('#{} {}'.format(t, ''.join(L_reverse[i][j:j+M])))
