def printSet(n, cursum):
    pass


def powerset(n, k, cursum):
    global total
    if cursum > 10:
        return
    total += 1
    if n == k:
        printSet(n, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum+arr[k])
        A[k] = 0
        powerset(n, k+1, cursum)


powerset(N, 0, 0)
print("호출횟수: {}".format(total))