student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict = {row["letter"]: row["code"] for (index, row) in data_frame.iterrows()}
# print(dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
if word:
    word = word.upper()
    list = [dict.get(letter, "-") for letter in word]
    print(list)

else:
    print("NONE")
