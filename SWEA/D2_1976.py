for t in range(1, 1+int(input())):
    h1, m1, h2, m2 = map(int, input().split())
    m = h1*60 + h2*60 + m1 + m2
    h = m//60
    print('#{} {} {}'.format(t, h%12 if h%12 != 0 else 12, m%60))