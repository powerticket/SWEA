import sys
result = []
for i in range(3):
    T = int(sys.stdin.readline())
    S = 0
    for t in range(T):
        S += int(sys.stdin.readline())
    if S == 0:
        result += '0'
    elif S > 0:
        result += '+'
    else:
        result += '-'
for i in range(3):
    print(result[i])