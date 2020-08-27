s = "Reverse this string"
s_new = ''
for ch in s:
    s_new = ch + s_new
print(s_new)


s = "Reverse this string"
s_list = list(s)
s_list.reverse()
s = ''.join(s_list)
print(s)

s = "Reverse this string"
print(''.join(reversed(s)))

s = "Reverse this string"
s_new = s[::-1]
print(s_new)
