def perm(k):
    if k == N:
        print(arr)
        new_arr.append(arr[:])
        return arr
    for i in range(k, N):
        arr[k], arr[i] = arr[i], arr[k]
        perm(k+1)
        arr[k], arr[i] = arr[i], arr[k]
    return


arr = [1, 2, 3]
N = len(arr)
new_arr = []
perm(0)
print(new_arr)
