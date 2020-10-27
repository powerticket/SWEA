import sys
sys.stdin = open('sample_input.txt')

def htob(h):
    result = ''
    if h.isdigit():
        num = int(h)
    else:
        num = ord(h) - 55
    for i in range(4):
        if num & 8 >> i:
            result += '1'
        else:
            result += '0'
    return result


CODE = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())
for t in range(1, T+1):
    answer = 0
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(input())
    base2_arr = []
    candidate = []
    code_set = set()
    for a in arr:
        base2 = ''
        for char in a:
            base2 += htob(char)
        base2_arr.append(base2)
    # find end of codes
    for row in base2_arr:
        i = M * 4 - 1
        while i > 54:
            if row[i] == '1':
                j = 1
                while 1:
                    c = row[i-(7*j-1):i+1:j]
                    if c in CODE:
                        break
                    j += 1
                candidate.append(row[i-(56*j-1):i+1:j])
                i -= 56 * j
            else:
                i -= 1
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
