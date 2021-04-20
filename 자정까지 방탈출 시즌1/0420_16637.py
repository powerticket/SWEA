import sys
sys.stdin = open('0420_16637.txt', 'r')

# 04/20
# 16637 괄호 추가하기

def calculate(a, token, b):
    a = int(a)
    b = int(b)
    if token == '+':
        return a + b
    if token == '-':
        return a - b
    return a * b


def dfs(cur_index, cur_value):
    global answer
    if cur_index >= len_exp:
        if cur_value > answer:
            answer = cur_value
        return
    dfs(cur_index+2, calculate(cur_value, exp[cur_index], exp[cur_index+1]))
    if cur_index + 3 < len_exp:
        dfs(cur_index+4, calculate(cur_value, exp[cur_index], calculate(exp[cur_index+1], exp[cur_index+2], exp[cur_index+3])))


N = int(input())
exp = list(input())
len_exp = len(exp)
answer = -2**31
dfs(1, int(exp[0]))
print(answer)
