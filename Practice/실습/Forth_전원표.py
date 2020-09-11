for t in range(1, int(input())+1):
    tokens = input().split()
    stack = []
    error = 0
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token == '.':
            break
        elif len(stack) < 2:
            error = 1
            break
        else:
            b = stack.pop()
            f = stack.pop()
            if token == "+":
                stack.append(f+b)
            elif token == "-":
                stack.append(f-b)
            elif token == "*":
                stack.append(f*b)
            elif token == "/":
                stack.append(f//b)
    if len(stack) > 1:
        error = 1
    if not error:
        print('#{} {}'.format(t, stack[-1]))
    else:
        print('#{} error'.format(t))