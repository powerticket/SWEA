# 01/26
# 1992 쿼드트리

def quad(r, c, k):
    # 한 칸 단위로 쪼개지면 바로 해당 값 return
    if k == 1:
        return arr[r][c]
    # K x k 행렬이 모두 같은 값이면 해당 값 return
    for i in range(k):
        for j in range(k):
            if arr[r][c] != arr[r+i][c+j]:
                break
        else:
            continue
        break
    else:
        return arr[r][c]
    # k를 2로 나누어 4분할한 행렬에 대해 quad 함수 호출
    result = ''
    k //= 2
    result += quad(r, c, k)
    result += quad(r, c+k, k)
    result += quad(r+k, c, k)
    result += quad(r+k, c+k, k)
    return '(' + result + ')'


N = int(input())
arr = [input() for _ in range(N)]
result = quad(0, 0, N)
print(result)
