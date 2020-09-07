arr = [0] * 82
arr[0] = 0
arr[1] = 1
arr[2] = 1
N = int(input())
for i in range(3, N+2):
    arr[i] = arr[i-1] + arr[i-2]

print(2*arr[N]+2*arr[N+1])
