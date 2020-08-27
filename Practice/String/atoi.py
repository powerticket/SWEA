def atoi(s1):
    value = 0
    for i in range(len(s1)):
        c = s1[i]
        if '0' <= c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = value * 10 + digit
    return value



a = "123"
print(type(a))
b = atoi(a)
print(type(b))
print(b)