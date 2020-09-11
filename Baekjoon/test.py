from itertools import combinations

all = []
for i in range(1, 4 + 1):
    all.extend([k for k in combinations([j for j in range(4)], i)])

print(set(5))