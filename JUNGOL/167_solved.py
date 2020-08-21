l = [list(map(int, input().split())) for _ in range(4)]
for i in range(len(l)):
    print(int(sum(l[i])/len(l[i])), end=' ')
print()
for i in range(len(l[0])):
    total = 0
    for j in range(len(l)):
        total += l[j][i]
    print(int(total/len(l)), end= ' ')
print()
total = 0
for i in range(len(l)):
    total += sum(l[i])
print(int(total/(len(l)*len(l[0]))))