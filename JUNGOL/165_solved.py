l = [[0] * 5 for _ in range(5)]
for i in range(3):
    l[0][2*i] += 1
for i in range(1, len(l)):
    for j in range(len(l[i])):
        if j > 0:
            l[i][j] += l[i-1][j-1]
        if j < len(l[i])-1:
            l[i][j] += l[i-1][j+1]
for i in range(len(l)):
    for j in range(len(l[i])):
        print('{} '.format(l[i][j]), end='')
    print()