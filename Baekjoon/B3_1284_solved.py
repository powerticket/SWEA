while 1:
    N = input()
    if N == '0':
        break
    width = 1
    for n in N:
        if n == '0':
            width += 4
        elif n == '1':
            width += 2
        else:
            width += 3
        width += 1
    print(width)