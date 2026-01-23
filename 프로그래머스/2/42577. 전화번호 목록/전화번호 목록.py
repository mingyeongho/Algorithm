def solution(phone_book):
    hash = {}
    for phone in phone_book:
        hash[phone] = True
        
    for phone in phone_book:
        temp = ""
        for n in phone:
            temp += n
            if temp in hash and temp != phone:
                return False
    return True