def f(n, s , N, r):
    if n == r:
        print(c)
    else:
        for i in range(s, N-r+n+1):
            c[n] = i
            f(n+1, i+1, N, r)


N = 10
r = 3
c = [0] * 3
f(0, 0, N, r)
