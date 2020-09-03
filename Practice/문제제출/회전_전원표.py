for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    for _ in range(M):
        r = L.append(L.pop(0))
    print('#{} {}'.format(t, L[0]))