T = input()
cmd = []
L = []
for _ in range(int(T)):
    L += [input()]
for _ in range(len(L[0])):
    cmd += [[]]
for j in range(len(L[0])):
    cmd[j] = L[0][j]
    for i in range(len(L)-1):
        if L[i][j] != L[i+1][j]:
            cmd[j] = '?'
            break
print(''.join(cmd))