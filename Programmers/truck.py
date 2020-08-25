def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight = 0
    current_truck = []

    while truck_weights or current_truck:
        if truck_weights and weight >= current_weight + truck_weights[0]:
            current_weight += truck_weights[0]
            current_truck.append(answer)
            current_truck.append(truck_weights.pop(0))
        if answer - current_truck[0] >= bridge_length:
            current_truck.pop(0)
            current_weight -= current_truck.pop(0)
            answer -= 1
        answer += 1
    answer += 1
    return answer
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))