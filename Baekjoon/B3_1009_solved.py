T = int(input())
for _ in range(T):
    L = list(map(int, input().split()))
    a = L[0]
    b = L[1] % 4 if L[1] % 4 != 0 else 4
    test = pow(a, b)
    if test % 10 == 0:
        print(10)
    else:
        print(test % 10)