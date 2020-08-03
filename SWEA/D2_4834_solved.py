T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = input()
    count = [0] * 10
    for n in num:
        count[int(n)] += 1
    max_count = 0
    max_num = 0
    for i in range(len(count)):
        if count[i] >= max_count:
            max_count = count[i]
            max_num = i
    print(f'#{t} {max_num} {max_count}')