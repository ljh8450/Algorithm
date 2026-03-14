from collections import deque
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0], -x[1]))
    routes = deque(routes)
    
    start, end = routes.popleft()
    while routes:
        this_start, this_end = routes.popleft()
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))