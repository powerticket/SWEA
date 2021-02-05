from itertools import combinations

N = int(input())
str_num = [str(n) for n in range(9, -1, -1)]
arr = []
for i in range(1, 11):
    comb_nums = list(combinations(str_num, i))
    for comb_num in reversed(comb_nums):
        arr.append(''.join(comb_num))
if N < len(arr):
    print(arr[N])
else:
    print(-1)
