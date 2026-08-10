# NATO app improved to handle exceptions
import pandas

# Keyword Method with iterrows()
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict = {row["letter"]: row["code"] for (index, row) in data_frame.iterrows()}
# print(dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try :
        word = input("Enter a word: ")
        if word:
            word = word.upper()
            list = [dict[letter] for letter in word]
            print(list)

        else:
            print("NONE")
        break
    except KeyError:
        print ("Sorry, only letters in the alphabet please")
