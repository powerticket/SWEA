import sys
sys.stdin = open('sample_input.txt', 'r')


for t in range(1, int(input())+1):
    bracket = ['(', ')', '{', '}', '[', ']']
    stack = []
    S = input()
    for s in S:
        if s in bracket:
            stack.append(s)

            if len(stack) > 1:
                if bracket.index(stack[-2]) - bracket.index(stack[-1]) == -1:
                    stack.pop()
                    stack.pop()
    print('#{} {}'.format(t, int(not bool(stack))))