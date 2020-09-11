S = input()
S = S.strip()
S_list = list(S)
count = 0
if S_list:
    count += 1
for ch in S_list:
    if ch == ' ':
        count += 1
print(count)