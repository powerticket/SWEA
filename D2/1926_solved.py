N = int(input())


for i in range(1, N + 1):
    words = str(i)
    claps = 0
    for word in words:
        if(int(word) % 3 == 0 and int(word) != 0):
            claps += 1
    if(claps == 0):
        print(i, end = ' ')
    else:
        print('-' * claps, end = ' ')