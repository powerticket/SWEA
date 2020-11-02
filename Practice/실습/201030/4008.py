import sys
sys.stdin = open('sample_input.txt')


def permutation(n):
    if n == token_len:
        global max_result, min_result
        result = number[0]
        for i in range(token_len):
            if token_arr[i] == 0:
                result += number[i+1]
            elif token_arr[i] == 1:
                result -= number[i+1]
            elif token_arr[i] == 2:
                result *= number[i+1]
            else:
                result = int(result / number[i+1])
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
        return
    perm = int(''.join(map(str, token_arr)))
    if perm in visited[n]:
        return
    visited[n].add(perm)
    for i in range(n, token_len):
        token_arr[i], token_arr[n] = token_arr[n], token_arr[i]
        permutation(n+1)
        token_arr[i], token_arr[n] = token_arr[n], token_arr[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    token_number = list(map(int, input().split()))
    number = list(map(int, input().split()))
    token_arr = []
    for idx, num in enumerate(token_number):
        for _ in range(num):
            token_arr.append(idx)
    token_len = len(token_arr)
    visited = [set() for _ in range(token_len)]
    max_result = -0xffffffff
    min_result = 0xffffffff
    permutation(0)
    result = max_result - min_result
    print('#{} {}'.format(t, result))
