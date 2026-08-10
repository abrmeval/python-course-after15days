import random
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = 8
nr_symbols = 3
nr_numbers = 5

def generate_password():
    max_r = nr_letters
    ps_list = []

    for num in range(0, max_r):
        if num < nr_letters:
            rdm_index_letter = random.randint(0, len(LETTERS) - 1)
            ps_list.append(LETTERS[rdm_index_letter])
        if num < nr_symbols:
            rdm_index_symbol = random.randint(0, len(SYMBOLS) - 1)
            ps_list.append (SYMBOLS[rdm_index_symbol])
        if num < nr_numbers:
            rdm_index_number = random.randint(0, len(NUMBERS)  - 1)
            ps_list.append(NUMBERS[rdm_index_number])

    random.shuffle(ps_list)
    return "".join(ps_list)