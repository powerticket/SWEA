import sys
sys.stdin = open('input.txt')

CODE = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())
for t in range(1, T+1):
    answer = 0
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    candidate = []
    code_set = set()
    # find end of codes
    for row in arr:
        for i in range(M-1, 54, -1):
            if row[i] == '1':
                candidate.append(row[i-55:i+1])
                break
    # decoding
    for codes in candidate:
        code = ''
        for i in range(8):
            code += str(CODE.index(codes[7*i:7*i+7]))
        code_set.add(code)
    # check validation
    for code in code_set:
        check = result = int(code[7])
        for i in range(7):
            number = int(code[i])
            result += number
            if i % 2:
                check += number
            else:
                check += 3 * number
        if not check % 10:
            answer += result
    print('#{} {}'.format(t, answer))
