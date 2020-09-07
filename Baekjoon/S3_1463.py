N = int(input())
arr = [9999] * (N+1)
arr[0] = 0
arr[1] = 0

for j in range(i, N+1):
    if not j % 3:
        arr[j] = min(arr[j], arr[j//3] + 1)
        