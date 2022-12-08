def caesar_cipher(message, shift):
    # list comprehension to generate list
    msg_list = [ch for ch in (message * 2)]

    # apply rules for shifting letters in list
    x = 0
    while x < shift:
        msg_list.insert(0, msg_list.pop())
        x += 1

    return msg_list

print(caesar_cipher("HELLO GOOD DAY", 1))