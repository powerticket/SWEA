for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    Q = [0] + list(map(int, input().split()))
    f, r = 0, N
    SIZE = N + 1

    for _ in range(M):
        r = (r+1) % SIZE
        f = (f+1) % SIZE
        Q[r] = Q[f]

    print(Q[f+1])