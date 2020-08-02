def list_multiply(L):
    result = 1
    for l in L:
        result *= int(l)
    return result

L = input()
if int(L) < 10:
    print('NO')
else:
    for i in range(1, len(L)-1):
        if list_multiply(L[:i]) == list_multiply(L[i:]):
            print('YES')
            break
    else:
        print('NO')