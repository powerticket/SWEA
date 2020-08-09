import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, C = input().split()
    L = [int(i) for i in N]
    C = int(C)
    count = 0
    for i in range(len(N)-1):
        max = L[i]
        max_idx = i
        for j in range(i+1, len(N)):
            if max <= L[j]:
                max = L[j]
                max_idx = j
        if max != L[i]:
            L[i], L[max_idx] = L[max_idx], L[i]
            count += 1
            if count == C:
                break
    else:
        for _ in range(C-count):
            L[-1], L[-2] = L[-2], L[-1]
    print('#{} {}'.format(t, "".join([str(i) for i in L])))