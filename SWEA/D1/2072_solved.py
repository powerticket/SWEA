T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case} ', end ='')
    L = list(map(int, input().split()))
    result = 0
    for i in L:
        if(i % 2 == 1):
            result += i
    print(result)