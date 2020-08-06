def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = factorial(M)//factorial(M-N)//factorial(N)
    print(result)