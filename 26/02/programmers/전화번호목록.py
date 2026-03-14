def solution(phone_book):
    phone_book = list(sorted(phone_book))
    for i in range(len(phone_book)-1):
        phone_num = phone_book[i]
        length = len(phone_num)
        if length <= len(phone_book[i+1]) and phone_book[i] == phone_book[i+1][:length]:
            return False
    else:
        return True

phone_book = ["123","456","789"]
print(solution(phone_book))