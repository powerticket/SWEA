T = int(input())
L = list(map(int, input().split()))
N = int(input())
if N <= max
L.append(N)
L.sort()
f = L.index(N)
r = L[f+1] - L[f-1] - 2
print(r)