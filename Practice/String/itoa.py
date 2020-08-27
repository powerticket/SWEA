def itoa(num):
    arr = []
    x = num
    y = 0
    while x:
        y = x % 10
        x //= 10
        arr.append(chr(y + ord('0')))
    return ''.join(reversed(arr))

x = 123
print(x, type(x))
str = itoa(x)
print(str, type(str))
print(-11//10)