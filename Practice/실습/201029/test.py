from itertools import permutations
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    list_res = []
    N_list = []
    a = []
    cnt = -N - 1
    for i in range(N - 1):
        a.append(i + 1)
    permute = list(permutations(a, N - 1))
    # print('permute :', permute)
    for i in range(len(permute)):
        N_list.append(0)
        for j in range(len(permute[0])):
            N_list.append(permute[i][j])
        N_list.append(0)
    # print('Nlist :', N_list)
    # print('arr :', arr)
    for i in range(len(N_list) // (N + 1)):
        result = 0
        cnt += N + 1
        for j in range(N):
            result += arr[N_list[cnt + j]][N_list[cnt + j + 1]]
        list_res.append(result)
    print('#{} {}'.format(tc, min(list_res)))