def subset(k):
    if k == N:
        print(bit)
        for i in range(N):
            if bit[i]:
                print(arr[i], end=' ')
        print()
        return
    bit[k] = 0
    subset(k+1)
    bit[k] = 1
    subset(k+1)


arr = [1, 2, 3]
N = len(arr)
bit = [0] * N
subset(0)
