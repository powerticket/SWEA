# 대괄호 [ ], 중괄호 { }, 소괄호 ( )가 짝이 맞게 적절히 배치되어 있는지를 판별하는 프로그램을 작성하십시오.

# 각 괄호의 우선순위는 상관하지 않습니다. 예를 들어, {[]} 와 같이 중괄호 안에 대괄호가 들어있어도 적절히 배치되어 있는 것으로 판별합니다.



# 괄호 외에도 -,+ 문자가 존재 할 수 있으며, 

# - 가 입력될 경우, 왼쪽으로 가장 가까운 괄호와 동일하게 취급합니다. (입력의 가장 왼쪽에는 -가 입력되지 않습니다.)

# + 가 입력될 경우, 오른쪽으로 가장 가까운 괄호와 동일하게 취급합니다. (입력의 가장 오른쪽에는 -가 입력되지 않습니다.)



# ex. [(-))] , ((-++) , {{-(-+)}+}는 짝이 맞게 배치되어 있다고 판별합니다.



# 입력 설명

# 임의의 괄호와 +,- 배치
# 출력 설명

# 짝이 맞는 적절한 배치의 경우 True 출력, 그렇지 않을 경우 False 출력


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
L = list(user_input)


for i in range(len(L)):
    if L[i] == "-":
        L[i] = L[i-1]
for i in range(len(L)-1, -1, -1):
    if L[i] == "+":
        L[i] = L[i+1]



if "".join(L).find("(") > "".join(L).find(")") or "".join(L).find("{") > "".join(L).find("}") or "".join(L).find("[") > "".join(L).find("]"):
    print(False)
elif L.count("(") != L.count(")") or L.count("{") != L.count("}") or L.count("[") != L.count("]"):
    print(False)
else:
    num_a = 0
    num_b = 0
    num_c = 0
    first_close = []
    for l in L:
        if l == '(':
            first_close.append(')')
            num_a += 1
        elif l == ')':
            num_a -= 1
            if first_close[-1] != ')':
                print(False)
                break
            first_close.pop()
        elif l == '}':
            num_b += 1
            first_close.append('}')
        elif l == '}':
            num_b -= 1
            if first_close[-1] != '}':
                print(False)
                break
            first_close.pop()
        elif l == '[':
            num_c += 1
            first_close.append(']')
        elif l == ']':
            num_c -= 1
            if first_close[-1] != ']':
                print(False)
                break
            first_close.pop()
        if num_a < 0 or num_b < 0 or num_c <0:
            print(False)
            break
    else:
        print(True)