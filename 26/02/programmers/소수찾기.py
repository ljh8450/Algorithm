from itertools import permutations
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    length = len(numbers)
    checker = []
    for i in range(1, length+1):
        combination_list = list(permutations(numbers, i))
        for number in combination_list:
            number = int(''.join(number))
            if is_prime(number) and number not in checker:
                answer += 1
                checker.append(number)
    return answer

numbers = "17"
print(solution(numbers))