# 올바른 문자열 검사
def check(u):
    u_copy = u[:]
    stack = []
    while u_copy:
        p_pop = u_copy.pop(0)
        if p_pop == '(':
            stack.append(p_pop)
        else:
            if stack:
                stack.pop()
            else:
                return 0
    if not stack:
        return 1
    return 0


def recur(v):
    if not v:
        return ''
    u = [v.pop(0)]
    while u.count('(') != u.count(')'):
        u.append(v.pop(0))
    if check(u):
        u_return = ''.join(u)
        return u_return + recur(v)
    else:
        u.pop(0)
        u.pop(-1)
        u_return = ''.join(u).replace('(', '1').replace(')', '(').replace('1', ')')
        return '(' + recur(v) + ')' + u_return


def solution(v):
    if check(list(v)):
        return v
    answer = recur(list(v))
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))