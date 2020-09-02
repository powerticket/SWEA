for t in range(1, int(input())+1):
    stack = []
    tokens = input().split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == '.':
            break
        elif len(stack) > 1:
            b = stack.pop()
            f = stack.pop()
            if token == '+':
                stack.append(f+b)
            elif token == '-':
                stack.append(f-b)
            elif token == '*':
                stack.append(f*b)
            elif token == '/':
                stack.append(f//b)
            else:
                stack.append('error')
                break
        else:
            stack.append('error')
            break
    if len(stack) == 1:
        print('#{} {}'.format(t, stack.pop()))
    else:
        print('#{} error'.format(t))