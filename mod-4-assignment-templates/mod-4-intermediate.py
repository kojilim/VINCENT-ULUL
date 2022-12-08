def shift_letter(letter, shift):
    # declare list
    ltr_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    if letter in ltr_list:  # conditional to evaluate if input ⊆ list
        idx = ltr_list.index(letter)  # contain index

        # position letter as first element in list
        x = 0
        while x < idx:
            ltr_list.insert(len(ltr_list), ltr_list.pop(0))
            x += 1

        # shift letter in list
        y = 0
        while y < shift:
            ltr_list.insert(len(ltr_list), ltr_list.pop(0))
            y += 1

        return ltr_list[0]

    elif letter == " ":  # conditional if " " is the input
        return " "

def caesar_cipher(message, shift):
    msg_list = [ch for ch in (message * 2)]  # list comprehension to generate list
    
    # apply rules for shifting letters in list
    x = 0
    while x < shift:
        msg_list.insert(0, msg_list.pop())
        x += 1

    return msg_list

def shift_by_letter(letter, letter_shift):
    ltr_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ltr_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
    
    if letter in ltr_list:  # conditional to evaluate if input ⊆ list
        ltr_idx = ltr_list.index(letter)  # contain index

        # position letter as first element in list
        x = 0
        while x < ltr_idx:
            ltr_list.insert(len(ltr_list), ltr_list.pop(0))
            x += 1

        ltrsft = ltr_list.index(letter_shift)  # get index of letter shift
        sft = ltr_index[ltrsft]  # attain numerical equivalent of letter shift
        
        # shift letter in list
        y = 0
        while y < sft:
            ltr_list.insert(len(ltr_list), ltr_list.pop(0))
            y += 1

    elif letter == " ":  # conditional if " " is the input
        return " "

def vigenere_cipher(message, key):
    fw = ""
    ns = 0
    if len(key) % len(message) == 0:
        vk = key * (len(message)//len(key))
    else:
        vk = key * (len(message)//len(key)) + \
            key[:(len(message) % len(key))]

    for letter in message:
        if letter != " ":
            finalLetter = ord(letter) + (ord(vk[ns]) - 65)
            if finalLetter > 90:
                finalLetter -= 26
        else:
            finalLetter = ord(letter)
        space = chr(finalLetter)
        fw += space
        ns += 1
    return (fw)
