def comb(n, r):
    if r == N:
        print(sel)
        return
    elif n >= len(arr):
        return
    sel[r] = arr[n]
    comb(n+1, r+1)
    comb(n+1, r)


arr = [1, 2, 3]
N = 2
sel = [0] * N
comb(0, 0)