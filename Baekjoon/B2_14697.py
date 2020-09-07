import sys


A, B, C, P = map(int, sys.stdin.readline().split())
arr = [0] * (P+1)
arr[A] = arr[B] = arr[C] = 1
for i in [A, B, C]:
    for j in range(A+1, len(arr)):
        if j < i or arr[j] == 1:
            continue
        if arr[j-i]:
            arr[j] = 1
print(arr[P])