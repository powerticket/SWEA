S = input()
S = S.upper()
D = dict()
for s in S:
    D[s] = D.get(s, 0) + 1
D_max = max(D.values())
max_word = ''
count = 0
for key, value in D.items():
    if value == D_max:
        count += 1
        max_word = key
if count != 1:
    print('?')
else:
    print(max_word)