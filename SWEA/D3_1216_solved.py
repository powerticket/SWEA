def palin(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return 0
    return len(s)


def check(L, L_ver):
    max_p_len = 1
    for i in range(100):
        for j in range(100-max_p_len):
            for k in range(max_p_len, 100-j):
                if L[i][j] == L[i][j+k]:
                    p_len = palin(L[i][j:j+k+1])
                    if p_len > max_p_len:
                        max_p_len = p_len
                if L_ver[i][j] == L_ver[i][j+k]:
                    p_len = palin(L_ver[i][j:j+k+1])
                    if p_len > max_p_len:
                        max_p_len = p_len
    return max_p_len


for _ in range(1, 11):
    t = int(input())
    L = [input() for _ in range(100)]
    L_ver = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            L_ver[i][j] = L[j][i]
    print('#{} {}'.format(t, check(L, L_ver)))