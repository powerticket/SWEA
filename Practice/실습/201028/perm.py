def perm(n, k, m):
    if n == k:
        print(A[0:3])
    else:
        for i in range(n, m):
            A[n], A[i] = A[i], A[n]
            perm(n+1, k, m)
            A[n], A[i] = A[i], A[n]

A = [1, 2, 3, 4, 5]
perm(0, 3, 5)