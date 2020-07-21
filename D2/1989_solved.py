T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case} ', end = '')
    words = input()
    incorrect = 0
    for i in range(len(words)):
        if(words[i] != words[-i - 1]):
            incorrect += 1
    if(incorrect != 0):
        print(0)
    else:
        print(1)