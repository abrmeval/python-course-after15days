#Final function
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar Cipher Function
def caesar(direction, original_text, shift_amount):
    length =  26
    processed_text = ""
    step = 0

    if direction == "encode":
        step = 1
    elif direction == "decode":
        step = - 1

    if step != 0:
        shift_amount = step * shift_amount
        for char in original_text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + shift_amount) % length
                processed_text +=  alphabet[new_index]
            else:
                processed_text += char
        print(f"Here is the {direction}d result: {processed_text}")

go_again = True
print(logo)
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if answer == "no":
        go_again = False
print("Goodbye")
