def calculate_love_score(name1, name2):
#     Love Calculator
# 💪 This is a difficult challenge! 💪
#
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
#
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# 2. Then check for the number of times the letters in the word LOVE occurs.
#
# 3. Then combine these numbers to make a 2 digit number and print it out.
#
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
#
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
#
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
#
# Love Score = 53
#
# Example Input
# calculate_love_score("Kanye West", "Kim Kardashian")
#
# Example Output
# 42
#     :param name1:
#     :param name2:
#     :return:

    word1 = "TRUE"
    word2 = "LOVE"
    name1 = name1.upper()
    name2 = name2.upper()

    times_in_word1 = 0
    times_in_word2 = 0

    for l in name1:
        if l in word1:
            times_in_word1 += 1
        if l in word2:
            times_in_word2 += 1

    for l in name2:
        if l in word1:
            times_in_word1 += 1
        if l in word2:
            times_in_word2 += 1

    print(f"{times_in_word1}{times_in_word2}")

calculate_love_score("Kanye West", "Kim Kardashian")