import sys
sys.stdin = open('0312_9935.txt', 'r')

# 03/12
# 9935 문자열 폭발

string = input()
bomb = input()
len_bomb = len(bomb)

# result를 문자열이 아닌 배열로 하는 이유는 문자열 폭발 시, del이 문자열을 재조정하는 속도보다 빠르기 때문이다.
result = []
for s in string:
    result.append(s)
    if s == bomb[-1]:
        if ''.join(result[-len_bomb:]) == bomb:
            del result[-len_bomb:]

result = ''.join(result)

if not result:
    result = 'FRULA'

print(result)
