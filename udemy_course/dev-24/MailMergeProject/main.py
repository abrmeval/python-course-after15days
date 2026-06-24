# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as letter_file:
    template = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    namestr = names_file.read()
    names = namestr.split("\n")

for name in names:
    trimmed_name = name.strip()
    letter = template.replace("[name]", trimmed_name)
    with open(f"Output/ReadyToSend/{trimmed_name}.txt", mode="w") as file:
        file.write(letter)
