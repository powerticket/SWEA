'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''
T = int(input())
for t in range(1, T+1):
    L = [list(map(int, input().split())) for _ in range(9)]
    check = 1
    check_list = [0] * 10
    for i in range(9):
        check_list = [0] * 10
        for j in range(9):
            check_list[L[i][j]] = 1
        for j in range(1, 10):
            if check_list[j] != 1:
                check = 0
                break
        if check == 0:
            break
        for j in range(9):22
            check_list[L[j][i]] = 2
        for j in range(1, 10):
            if check_list[j] != 2:
                check = 0
                break
        if check == 0:
            break
    for i in range(3):
        for j in range(3):
            check_list = [0] * 10
            for k in range(3):
                for l in range(3):
                    check_list[L[3*i+k][3*j+l]] = 1
            for k in range(1, 10):
                if check_list[k] != 1:
                    check = 0
                    break
            if check == 0:
                break
        if check == 0:
            break
    print('#{} {}'.format(t, check))
