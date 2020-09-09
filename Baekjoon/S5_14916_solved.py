N = int(input()) # 1 ~ 100,000
arr = [N] * 100001
arr[0] = 0
for i in (2, 5):
    for j in range(1, N+1):
        if j < i or arr[j] == 1:
            continue
        arr[j] = min(arr[j], arr[j-i] + 1)
if arr[N] == N:
    print(-1)
else:
    print(arr[N])