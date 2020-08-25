import sys
sys.stdin = open('input_circular2.txt', 'r')  #파일로 인풋받기

T = 10
for t in range(1,T+1):
    input()
    N = 100
    arr = [input() for _ in range(N)]
    # print(arr)
    #가로줄 확인
    results=[]
    for i in range(N):
        for M in range(N-1,1,-1):
            if 1 > M:
                break
            for j in range(N-M+1):
                if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                    if len(arr[i][j:j+M]) > 1:
                        results.append(arr[i][j:j+M])
    #세로줄 확인
    for j in range(N):
        # 세로줄 입력 새로하기
        arr_col=[]
        for i in range(N):
            arr_col.append(arr[i][j])
        for M in range(N-1, 1, -1):
            if 1 > M:
                break
        # 회문이면 정답에 넣기
            for k in range(N-M+1):
                if arr_col[k:k+M] == arr_col[k:k+M][::-1]:
                    if len(arr_col[k:k+M]) > 1:
                        results.append(''.join(arr_col[k:k+M]))

    value=''
    for result in results:
        value += result
    print('#{} {}'.format(t,value))