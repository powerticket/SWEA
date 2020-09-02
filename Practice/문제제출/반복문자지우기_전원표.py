for t in range(1, int(input())+1):
    S = input()
    stack = []
    for s in S:
        stack.append(s)
        if len(stack) > 1:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
    print('#{} {}'.format(t, len(stack)))