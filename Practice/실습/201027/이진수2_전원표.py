T = int(input())
for t in range(1, T+1):
    fbase2 = ''
    f = float(input())
    for i in range(13):
        div = 1 / (2 << i)
        if f >= div:
            f -= div
            fbase2 += '1'
        else:
            fbase2 += '0'
        if f == 0:
            break
    if f != 0:
        fbase2 = 'overflow'
    print('#{} {}'.format(t, fbase2))
