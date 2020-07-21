T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case} ', end = '')
    L = list(map(int, input().split()))
    L.sort()
    min_num = L[0]
    max_num = L[-1]
    sum = 0
    count = 0
    for i in L:
        if(i != min_num and i != max_num):
            sum += i
            count += 1
    print(int(round(sum / count, 0)))