"""
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
"""


def traverse(v):
    if v == 0:
        return 0
    return traverse(L[v]) + traverse(R[v]) + 1


for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)

    arr = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        p, c = arr[i], arr[i+1]

        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p

    ans = traverse(N)
    print('#{} {}'.format(t, ans))
