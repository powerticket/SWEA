def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                break
    print(bucket)
    i = 0
    while i < len(bucket)-1:
        if bucket[i] == bucket[i+1]:
            bucket.pop(i+1)
            bucket.pop(i)
            answer += 2
            i =- 1
        i += 1
    print(bucket)
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
