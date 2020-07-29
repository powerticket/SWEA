word = input()
word = word.upper()
d = dict()
max_num = 0
max_word = ''
max_count = 0
for w in word:
    d[w] = d.get(w, 0) + 1
for key, val in d.items():
    if val > max_num:
        max_word = key
        max_num = val
        max_count = 1
    elif val == max_num:
        max_count +=1
if max_count == 1:
    print(max_word)
else:
    print('?')