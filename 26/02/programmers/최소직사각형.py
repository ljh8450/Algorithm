def solution(sizes):
    width, height = 0, 0
    for size in sizes:
        size.sort()
        x, y = size
        width = max(width, x)
        height = max(height, y)
    
    answer = width * height
    return answer

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	
print(solution(sizes))