def comb(n, r):
    if r == 6:
        print(*sel)
        return
    elif n == arr[0]:
        return
    sel[r] = lotto[n]
    comb(n+1, r+1)
    comb(n+1, r)
    

while 1:
    arr = input()
    if arr == '0':
        break
    arr = list(map(int, arr.split()))
    lotto = arr[1:]
    sel = [0] * 6
    comb(0, 0)
    print()