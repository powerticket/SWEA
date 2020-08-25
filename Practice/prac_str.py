def str_rev(s):
    arr = list(s)
    # swap
    for i in range(len(arr)//2):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]

    s = "".join(arr)
    return s


str1 = "algorithm"
str2 = str_rev(str1)
print(str2)