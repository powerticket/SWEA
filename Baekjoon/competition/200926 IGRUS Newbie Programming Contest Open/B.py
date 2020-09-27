N = int(input())
result = len(format(N, '0b'))
if N < 0:
    result = 32
print(result)