T = int(input())
for t in range(1, T+1):
    N, H = input().split()
    base2 = ''
    for h in H:
        if h.isdigit():
            num = int(h)
        else:
            num = ord(h) - 55
        for i in range(4):
            if (1 << 3) >> i & num:
                base2 += '1'
            else:
                base2 += '0'
    print('#{} {}'.format(t, base2))
