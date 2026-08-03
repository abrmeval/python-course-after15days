import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

max_r = 0
inputs = [nr_letters, nr_symbols, nr_numbers]

for maxnu in inputs:
    if maxnu > max_r:
        max_r = maxnu

ps_list = []

for num in range(0, max_r):
    if num < nr_letters:
        rdm_index_letter = random.randint(0, len(letters) - 1)
        ps_list.append(letters[rdm_index_letter])
    if num < nr_symbols:
        rdm_index_symbol = random.randint(0, len(symbols) - 1)
        ps_list.append (symbols[rdm_index_symbol])
    if num < nr_numbers:
        rdm_index_number = random.randint(0, len(numbers)  - 1)
        ps_list.append(numbers[rdm_index_number])

    # rdm_position = random.randint(1, 3)
    # ps[rdm_position]

random.shuffle(ps_list)
ps = "".join(ps_list)
print(ps)