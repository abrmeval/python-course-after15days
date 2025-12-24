import random
from art import logo

#Deals the cards
def deal_cards(cards, n):
    table_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(0, n):
        index = random.randint(0, len(table_cards) - 1)
        number = table_cards[index]
        cards.append(number)

def check_blackjack(user_cards, computer_cards, user_score, computer_score):
    # If computer gets a blackjack (Ace + 10 value card).
    if len(computer_cards) == 2 and  computer_score == 21:
        return "COMPUTER"

    # If user gets a blackjack (Ace + 10 value card).
    if len(user_cards) == 2 and user_score == 21:
        return "USER"

    return "NONE"

def print_final_score(user_cards, computer_cards, user_score, computer_score, message):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(message)

def print_current_score(user_cards, computer_cards, user_score):
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")


#Recalculate score if there is an Ace and score is above 21
def validate_ace(cards, score):
    if 11 in cards and score > 21:
        return score - 10
    return score

def print_logo():
    print("\n" * 20)
    print(logo)

want_play = True
while want_play:
    playing_choice = input("Do you wany to play a game of Blackjack? Type 'y' or 'n': ")
    if playing_choice == "y":
        print_logo()
        computer_cards =[]
        user_cards = []
        deal_cards(computer_cards, 2)
        deal_cards(user_cards, 2)
        user_score = validate_ace(user_cards, sum(user_cards))
        computer_score = validate_ace(computer_cards, sum(computer_cards))
        winner = check_blackjack(user_cards, computer_cards, user_score, computer_score)

        #If there is a winner
        if winner != "NONE":
            message = ""
            if winner == "COMPUTER":
                message = "Lose, opponent has a Blackjack 😱"
                print_final_score(user_cards, computer_cards, user_score, computer_score, message)
            else:
                message = "You win 😁"
                print_final_score(user_cards, computer_cards, user_score, computer_score, message)

        else:
            can_ask_another = True
            while can_ask_another:
                print_current_score(user_cards, computer_cards, user_score)
                another_card = input("Type 'y' to get another card, type 'n' to pass  ").lower()
                if another_card == "y":
                    deal_cards(user_cards, 1)
                    user_score = validate_ace(user_cards, sum(user_cards))
                    if user_score > 21:
                        print_final_score(user_cards, computer_cards, user_score, computer_score, "You went over. You lose 😭")
                        can_ask_another = False
                        winner = "COMPUTER"
                else:
                    can_ask_another = False
            #No winner
            if winner == "NONE":
                while computer_score < 17:
                    computer_score = validate_ace(computer_cards, sum(computer_cards))
                    deal_cards(computer_cards, 1)

                # If user score above 21
                if computer_score > 21:
                    print_final_score(user_cards, computer_cards, user_score, computer_score, "Opponent went over. You win 😁")
                    can_ask_another = False
                    winner = "USER"
                # If equal scores
                elif user_score == computer_score:
                     print_final_score(user_cards, computer_cards, user_score, computer_score, "It is a draw")
                     can_ask_another = False
                     winner = "DRAW"

                # If user score greater than computer score
                elif user_score > computer_score:
                    print_final_score(user_cards, computer_cards, user_score, computer_score, "You win 😁")
                    can_ask_another = False
                    winner = "USER"

                # Computer score is greater than user score
                else:
                    print_final_score(user_cards, computer_cards, user_score, computer_score, "You lose 😤")
                    can_ask_another = False
                    winner = "COMPUTER"
    else:
        want_play = False