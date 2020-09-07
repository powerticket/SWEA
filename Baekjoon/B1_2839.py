N = int(input())
MAX = 9999
arr = [MAX] * (N+1)
if N > 2:
    arr[3] = 1
if N > 4:
    arr[5] = 1
for i in (3, 5):
    for j in range(4, len(arr)):
        if j < i or arr[j] == 1:
            continue
        arr[j] = min(arr[j], arr[j-i]+1)
if arr[N] == MAX:
    print(-1)
else:
    print(arr[N])