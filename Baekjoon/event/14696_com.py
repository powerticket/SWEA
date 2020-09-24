N = int(input())
input_list = []
for _ in range(2*N):
    input_list.append(list(map(int, input().split())))
for i in range(N):
    A = input_list[2*i]
    B = input_list[2*i+1]
    a_score = 0
    b_score = 0
    for a in A[1:]:
        if a == 4:
            a_score += 1010101
        elif a== 3:
            a_score += 10101
        elif a== 2:
            a_score += 101
        elif a== 1:
            a_score += 1
    for b in B[1:]:
        if b == 4:
            b_score += 1010101
        elif b== 3:
            b_score += 10101
        elif b== 2:
            b_score += 101
        elif b== 1:
            b_score += 1
    if a_score > b_score:
        print('A')
    elif a_score < b_score:
        print('B')
    else:
        print('D')
