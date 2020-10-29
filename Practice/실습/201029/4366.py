def make_base3(n):
    if n < 3:
        return str(n)
    return make_base3(n//3) + str(n%3)


T = int(input())
for t in range(1, T+1):
    base2 = input()
    base3 = input()
    base2_candidate = []
    base2_digit = 0
    len_base2 = len(base2)
    len_base3 = len(base3)
    # make mistaken base2
    for i in range(len_base2):
        base2_digit += int(base2[i]) << (len_base2-1-i)
    for i in range(len_base2-1):
        base2_candidate.append(base2_digit ^ 1 << i)
    final_candidate = []
    for candidate in base2_candidate:
        final_candidate.append(make_base3(candidate))
    for candidate in final_candidate:
        if len(candidate) == len_base3:
            cnt = 0
            for i in range(len_base3):
                if base3[i] != candidate[i]:
                    cnt += 1
            if cnt == 1:
                break
    result = 0
    for idx, num in enumerate(reversed(candidate)):
        result += int(num) * 3 ** idx
    print('#{} {}'.format(t, result))
