from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    total_weight = 0
    trucks = deque(truck_weights)

    while bridge:
        time += 1
        total_weight -= bridge.popleft()

        if trucks:
            if total_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
    return time

bridge_length=2
weight=10
truck_weights=[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))