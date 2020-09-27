sentence = input().split()
spare_of_space = int(input())
spare_of_char = list(map(int, input().split()))
len_sentence = len(sentence)
result = ''
if spare_of_space - len_sentence + 1 >= 0:
    for word in sentence:
        if word[0].islower():
            result += word[0].upper()
            spare_of_char[ord(word[0])-97] -= 1
            if spare_of_char[ord(word[0])-97] < 0:
                result = -1
                break
        else:
            result += word[0]
            spare_of_char[ord(word[0])-65] -= 1
            if spare_of_char[ord(word[0])-65] < 0:
                result = -1
                break
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                if word[i].islower():
                    spare_of_char[ord(word[i])-97] -= 1
                    if spare_of_char[ord(word[i])-97] < 0:
                        result = -1
                        break
                else:
                    spare_of_char[ord(word[i])-65] -= 1
                    if spare_of_char[ord(word[i])-65] < 0:
                        result = -1
                        break
        else:
            continue
        break
else:
    result = -1
print(result)