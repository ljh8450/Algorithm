from itertools import product
def find(W, dictinary):
    for i, word in enumerate(dictinary):
        if W == word:
            return i+1
def solution(word):
    words = []
    alphabet = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        words.append(list(map(''.join, product(alphabet, repeat=i))))
    words = [x for sub in words for x in sub]
    words.sort()
    answer = find(word, words)
    return answer

word = "AAAAE"
print(solution(word))