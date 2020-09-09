N = int(input())
arr = [9999] * (N+1)
arr[0] = 0
arr[1] = 0
# N까지의 숫자를 확인하며 3으로 나눠지면 이전 3으로 나눠졌던 수의 +1
# 2로 나눠지면 이전 2로 나눠졌던 수의 +1
# 해당 수와 해당 수 -1의 경우의 수 +1 중 작은 값을 선택
for i in range(2, N+1):
    if not i % 3:
        arr[i] = arr[i//3] + 1
    elif not i % 2:
        arr[i] = arr[i//2] + 1
    arr[i] = min(arr[i], arr[i-1] + 1)
print(arr[N])