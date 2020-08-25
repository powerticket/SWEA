S = input()
S_list = list(S)
for i in range(len(S_list)):
    if ord(S_list[i]) > 96:
        S_list[i] = chr(ord(S_list[i])-32)
S_list.sort()
same = 0
count = 1
max_count = 0
max_word = S_list[0]
cmp_word = S_list[0]
for i in range(1, len(S_list)):
    if cmp_word == S_list[i]:
        count +=1
    else:
        if count > max_count:
            max_count = count
            max_word = cmp_word
            same = 0
        elif count == max_count:
            same = 1
        count = 1
        cmp_word = S_list[i]
if count > max_count:
    max_count = count
    max_word = S_list[i]
    same = 0
elif count == max_count:
    same = 1
if same == 1:
    print('?')
else:
    print(max_word)