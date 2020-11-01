def combination(n):
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
    for i in range(n, token_len):
        token_arr[i], token_arr[n] = token_arr[n], token_arr[i]
        combination(n+1)
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
    max_result = 0
    min_result = 0xffffffff
    combination(0)
    result = max_result - min_result
    print('#{} {}'.format(t, result))

"""
2
5
2 1 0 1
3 5 3 7 9
6
4 1 0 0
1 2 3 4 5 6
"""