for t in range(1, int(input())+1):
    ptn = input()
    text = input()
    pl = len(ptn)
    tl = len(text)
    i, j = 0, 0
    while i < tl and j < pl:
        if text[i] != ptn[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    print('#{} '.format(t), end='')
    if j == pl:
        print(1)
    else:
        print(0)