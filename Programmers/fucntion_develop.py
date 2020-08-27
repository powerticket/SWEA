def solution(progresses, speeds):
    answer = []
    while progresses:
        today = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            today += 1
        if today:
            answer.append(today)
    return answer

print(solution([95, 95, 95, 95], [4, 3, 2, 1]))