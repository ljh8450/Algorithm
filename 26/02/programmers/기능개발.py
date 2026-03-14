from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        count = 0
        for i, speed in enumerate(speeds):
            progresses[i] += speed
        for progress in list(progresses):
            if progress >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                break
        if count > 0:
            answer.append(count)
    return answer

progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))