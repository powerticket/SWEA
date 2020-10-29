def perm(k):
    if k == N-1:
        print(field)
    else:
        for i in range(k, N):
            field[k], field[i] = field[i], field[k]
            perm(k+1)
            field[k], field[i] = field[i], field[k]


field = list(range(2, 6))
N = len(field)
perm(0)
