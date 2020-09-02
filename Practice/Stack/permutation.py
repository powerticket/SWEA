def perm(n, k):
    global total
    total += 1
    print('시작')
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]
    print('끝')

total = 0
arr = [1, 2, 3]
N = len(arr)
perm(N, 0)
print(total)