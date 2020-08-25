for t in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    set_str1 = set(str1)
    max_cnt = 0
    for s1 in set_str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    print('#{} {}'.format(t, max_cnt))