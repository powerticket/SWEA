import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    L.insert(0, [0] * (N+1))
    for i in range(1, N+1):
        L[i].insert(0, 0)
    submat = [[], []]
    rowend = 0
    colend = 0
    rowstart = 0
    colstart = 0
    nor = 0
    noc = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if L[i][j] != 0:
                if L[i-1][j] == 0 and L[i][j-1] == 0:
                    rowstart = i
                    colstart = j
                    for k in range(N-j):
                        if L[i][j+k] == 0:
                            colend = j + k
                            break
                    else:
                        colend = N
                    for k in range(N-i):
                        if L[i+k][j] == 0:
                            rowend = i + k
                            break
                    else:
                        rowend = N
                    submat[0].append(rowend-rowstart)
                    submat[1].append(colend-colstart)
    for j in range(len(submat[0])-1, -1, -1):
        for i in range(j):
            if (submat[0][i] * submat[1][i]) > (submat[0][i+1] * submat[1][i+1]):
                submat[0][i], submat[0][i+1], submat[1][i], submat[1][i+1] = submat[0][i+1], submat[0][i], submat[1][i+1], submat[1][i]
    for j in range(len(submat[0]) - 1, -1, -1):
        for i in range(j):
            if (submat[0][i] * submat[1][i]) == (submat[0][i+1] * submat[1][i+1]) and submat[0][i] > submat[0][i+1]:
                submat[0][i], submat[0][i+1], submat[1][i], submat[1][i+1] = submat[0][i+1], submat[0][i], submat[1][i+1], submat[1][i]

    print('#{} '.format(t), end='')
    print('{} '.format(len(submat[0])), end='')
    for i in range(len(submat[0])):
        print('{} {} '.format(submat[0][i], submat[1][i]), end='')
    print()