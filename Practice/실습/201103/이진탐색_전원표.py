def bin_search(left, right, d):
    mid = (left + right) // 2
    if A[mid] == b:
        global result
        result += 1
        return
    if left == right:
        return
    if A[mid] < b:
        if d != 1:
            bin_search(mid+1, right, 1)
        else:
            return
    else:
        if d != -1:
            bin_search(left, mid-1, -1)
        else:
            return


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    len_A = len(A)
    result = 0
    for b in B:
        bin_search(0, len_A-1, 0)
    print('#{} {}'.format(t, result))
