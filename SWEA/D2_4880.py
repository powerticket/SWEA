def fight(s, e):
    if L[e] - L[s] == 1:
        return e
    if L[e] == 1 and L[s] == 3:
        return e
    return s


def relay(start, end):
    if start == end:
        return start
    if start + 1 == end:
        return fight(start, end)
    mid = (start + end) // 2
    f1 = relay(start, mid)
    f2 = relay(mid+1, end)
    return fight(f1, f2)


for t in range(1, int(input())+1):
    N = int(input())
    L = list(map(int, input().split()))
    result = relay(0, len(L)-1) + 1
    print('#{} {}'.format(t, result))