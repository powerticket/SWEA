def room_check(a, b, c, p):
    p = A*a + B*b + C*c
    if p == P:
        return 1
    if p > P:
        return 0
    if room_check(a+1, b, c, p):
        return 1
    if room_check(a, b+1, c, p):
        return 1
    if room_check(a, b, c+1, p):
        return 1
    return 0


A, B, C, P = map(int, input().split())
print(room_check(0, 0, 0, 0))