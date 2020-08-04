T = int(input())

for t in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    count = [0] * 101
    for l in L:
        count[l] += 1
    max_count = 0
    max_num = 0
    for i in range(len(count)):
        if count[i] >= max_count:
            max_count = count[i]
            max_num = i
    print('#{} {}'.format(t, max_num))