L = list(map(float, input().split()))
D = dict()
for i in range(len(L)//2):
    D[f'x{i + 1}', f'y{i + 1}'] = L[2*i], L[2*i+1]
print(D)