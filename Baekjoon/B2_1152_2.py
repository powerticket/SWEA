S = input()
cnt = 0
words = False

for ch in S:
    if ch == ' ':
        if words:
            cnt += 1
            words = False
    else:
        words = True
if words:
    cnt += 1
print(cnt)