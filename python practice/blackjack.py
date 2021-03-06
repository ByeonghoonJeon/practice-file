import random
from time import sleep
# Function 1.
# Thousand separator function.


def thousand_separator(number):
    return "{:,}".format(number)


# 1. Greeting
print("Welcome to Jeon's Blackjack.")

# 2. Give $ 1,000 to user. And explain this game's goal.
print("Your seed money is $ 1,000. Reach to the highest balance!")
balance = 1000
thousand_separated_balance = thousand_separator(balance)


# 3. Ask ID.
user_id = input("Please input an ID\n")


# 4. Make a dictionary for recording performance of users and add player's current balance.
balance_record = {}
balance_record[user_id] = balance

while True:
    # 5. Ask how much user will bet.
    print(
        f"Hello, {user_id}. Your Balance: $ {thousand_separator(balance_record[user_id])}")
    if balance == 0:
        print("Balance is not enough. Time to go home!")
        break
    betting = input("Betting minimum is $ 100\nYour betting: ")

    # 5-1. Check if the input is valid number.
    while betting.isdigit() == False or int(betting) > balance or int(betting) <= 0:
        betting = input(
            f"Please bet within your balance.\nYour balance: $ {thousand_separated_balance}\n"
        )
    betting = int(betting)
    thousand_separated_betting = thousand_separator(betting)
    balance -= betting
    balance_record[user_id] = balance
    print(
        f"Your betting: $ {thousand_separated_betting}\nYour balance: $ {balance_record[user_id]}"
    )

    # 6. Make a card lists.
    number_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
    symbol_list = ["♠", "♣", "♦", "♥"]

    # 7. Make an empty dictionary to store picked cards.
    revealed_cards = {}

    # 8. Pick player's first card.
    random_symbol = random.choice(symbol_list)
    random_number = random.choice(number_list)
    player_first_card = random_symbol, random_number
    revealed_cards[random_symbol] = random_number
    print(f"Player's card: {player_first_card}")
    for i in range(0, 3):
        sleep(0.7)

    # 9. Pick player's second card.
    random_symbol = random.choice(symbol_list)
    random_number = random.choice(number_list)
    player_second_card = random_symbol, random_number
    # TestCode
    player_first_card = "♣", "A"
    player_second_card = "♥", "A"

    # 10. If player's second card is already existed in the revealed card dictionary, differentiate it.
    while player_second_card in revealed_cards:
        random_symbol = random.choice(symbol_list)
        random_number = random.choice(number_list)
        player_second_card = random_symbol, random_number
    revealed_cards[random_symbol] = random_number
    # 11. Exhibit player's card pair.
    player_card_pair = player_first_card, player_second_card
    print("Player's cards:", (player_card_pair))
    for i in range(0, 3):
        sleep(0.7)
    # 12. Pick dealer's first card.
    random_number = random.choice(number_list)
    random_symbol = random.choice(symbol_list)
    dealer_first_card = random_symbol, random_number

    # 13. If dealer's first card is in the revealed card dictionary, differentiate it.
    while dealer_first_card in revealed_cards:
        random_number = random.choice(number_list)
        random_symbol = random.choice(symbol_list)
        dealer_first_card = random_symbol, random_number
    revealed_cards[random_symbol] = random_number

    # 14. Pick dealer's second card.
    random_number = random.choice(number_list)
    random_symbol = random.choice(symbol_list)
    dealer_second_card = random_symbol, random_number

    # 15. If dealer's second card is in the revealed card dictionary, differentiate it.
    while dealer_second_card in revealed_cards:
        random_number = random.choice(number_list)
        random_symbol = random.choice(symbol_list)
        dealer_second_card = random_symbol, random_number
    revealed_cards[random_symbol] = random_number
    dealer_card_pair = dealer_first_card, dealer_second_card
    # TestCode
    dealer_first_card = "♣", "A"
    dealer_second_card = "♣", "4"
    # 16. Show dealer's first card.
    print(f"Dealer's cards: {dealer_first_card}")
    for i in range(0, 3):
        sleep(0.7)
    print(f"Dealer's cards: {dealer_first_card}, (Hidden card)")
    # 17. If dealer's first card is King, Queen, Jack, or 10, check if dealer's card is black jack.
    if dealer_first_card[1] in ("K", "Q", "J", 10):
        print(f"Oh! is dealer Black Jack?")
        for i in range(0, 3):
            print("Dealer is checking his cards." + "." * i)
            sleep(1.0)
    # 17-1. If dealer's card pair is blackjack, player looses and ask if the player wants to continue or quit.
        if dealer_second_card[1] == ("A"):
            print(dealer_card_pair)
            print("Dealer is Black Jack!")
            want_to_continue = input("Do you want to play more? (Y/N)\n")
            while want_to_continue.lower() not in ("y", "yes", "n", "no"):
                want_to_continue = input(
                    "If you want to keep play, please input 'Y'. If you want to finish card playing, input 'N'\n")
            if want_to_continue.lower() in ("y", "yes"):
                continue
            elif want_to_continue.lower() in ("n", "no"):
                break
    # 17-2. If dealer is not black jack, continue game.
        else:
            print("Dealer is not Black Jack.")

    # 18. If dealer's first card is Ace, check if dealer's card is black jack.
    if dealer_first_card[1] == "A":
        print(f"Oh! is dealer Black Jack?")
        for i in range(0, 3):
            print("Dealer is checking his cards." + "." * i)
            sleep(1.0)
    # 18-1. If dealer's card pair is black jack, ask the player whether continue or not.
        if dealer_second_card[1] in ("K", "Q", "J", 10):
            print(dealer_card_pair)
            print("Dealer is Black Jack!")
            want_to_continue = input("Do you want to play more? (Y/N)\n")
            while want_to_continue.lower() not in ("y", "yes", "n", "no"):
                want_to_continue = input(
                    "If you want to keep play, please input 'Y'. If you want to finish card playing, input 'N'\n")
            if want_to_continue.lower() in ("y", "yes"):
                continue
            elif want_to_continue.lower() in ("n", "no"):
                break
    # 18-2. If dealer is not black jack, continue game.
        else:
            print("Dealer is not Black Jack.")
    # 19. If player's card is a pair, ask whether split or not.
    print(
        f"Your card pair: {player_card_pair},\nDealer's card pair: ({dealer_first_card}, (Hidden card))")
    if player_card_pair[0][1] == player_card_pair[1][1]:
        # 19-1. Check if balance is sufficent to bet more.
        if balance >= betting:
            do_you_want_to_split = input("Would you like to split? (Y/N)\n")
            while do_you_want_to_split.lower() not in ("y", "yes", "n", "no"):
                do_you_want_to_split = input(
                    "If you want to split your card, please input 'Y'. If you want to keep go, input 'N'\n")
    # 19-2. If player wants to split, reduce player's balance.
            if do_you_want_to_split.lower() in ("y", "yes"):
                balance -= betting
                balance_record[user_id] = balance
                print("Your balance: $ {balance_record[user_id]}")
    # 19-3. Give a new card to the first card.
                first_split_card_pair_second = random_symbol, random_number
    # 19-3-1. Differentiate the new card from already revealed cards.
                while first_split_card_pair_second in revealed_cards:
                    random_number = random.choice(number_list)
                    random_symbol = random.choice(symbol_list)
                    first_split_card_pair_second = random_symbol, random_number
                    revealed_cards[random_symbol] = random_number
    # 19-4. Give a new card to the second card.
                second_split_card_pair_second = random_symbol, random_number
    # 19-4-1. Differentiate the new card from already revealed cards.
                while first_split_card_pair_second in revealed_cards:
                    random_number = random.choice(number_list)
                    random_symbol = random.choice(symbol_list)
                    first_split_card_pair_second = random_symbol, random_number
                    revealed_cards[random_symbol] = random_number
    # 19-5. Bind cards along with pair.
                first_split_card_pair = player_first_card, first_split_card_pair_second
                second_split_card_pair = player_second_card, second_split_card_pair_second
    # 19-6. Print card pairs.
                print(f"Player's card: {player_first_card}")
                for i in range(0, 1):
                    sleep(1)
                print(f"Player's card: {first_split_card_pair}")
                for i in range(0, 1):
                    sleep(1)
                print(f"Player's card: {player_second_card}")
                for i in range(0, 1):
                    sleep(1)
                print(f"Player's card: {second_split_card_pair}")
                print(
                    f"Player's card: {first_split_card_pair} {second_split_card_pair}")

    # 19-7. When player does not want to split.
            elif do_you_want_to_split.lower() in ("n", "no"):
                print("No split")
    # 19-8. If player's balance is not sufficient to bet more, print that you can't.
        elif balance < betting:
            print("Hmm, you don't have enough money to split.")

    # 20. Ask hit or stay(##When no split##) and show the sum of player's card pair.
    # 20-1 Substitute J, Q, K, in player's card to number 10 and A to 11 so that sum of the card numbers can be calculated.

    cal_player_first_card = 0
    if player_first_card[1] == "J":
        cal_player_first_card = 10
    elif player_first_card[1] == "Q":
        cal_player_first_card = 10
    elif player_first_card[1] == "K":
        cal_player_first_card = 10
    elif player_first_card[1] == "A":
        cal_player_first_card = 11
    else:
        cal_player_first_card == player_first_card[1]

    cal_player_second_card = 0
    if player_second_card[1] == "J":
        cal_player_second_card = 10
    elif player_second_card[1] == "Q":
        cal_player_second_card = 10
    elif player_second_card[1] == "K":
        cal_player_second_card = 10
    elif player_second_card[1] == "A":
        cal_player_second_card = 11
    else:
        cal_player_second_card == player_second_card[1]
    # 20-2 Calculate sum of player's card pair 
    sum_of_player_card = cal_player_first_card+cal_player_second_card

    # 20-3 Print sum of player's cards.
    print(f"Your card number: {sum_of_player_card}")

    # 20-4 Substitute J, Q, K, in Dealer's card to number 10 and A to 11 so that sum of the card numbers can be calculated.
    cal_dealer_first_card = 0
    if dealer_first_card[1] == "J":
        cal_dealer_first_card = 10
    elif dealer_first_card[1] == "Q":
        cal_dealer_first_card = 10
    elif dealer_first_card[1] == "K":
        cal_dealer_first_card = 10
    elif dealer_first_card[1] == "A":
        cal_dealer_first_card = 11
    else:
        cal_dealer_first_card == dealer_first_card[1]

    cal_dealer_second_card = 0
    if dealer_second_card[1] == "J":
        cal_dealer_second_card = 10
    elif dealer_second_card[1] == "Q":
        cal_dealer_second_card = 10
    elif dealer_second_card[1] == "K":
        cal_dealer_second_card = 10
    elif dealer_second_card[1] == "A":
        cal_dealer_second_card = 11
    else:
        cal_dealer_second_card == dealer_second_card[1]

    # 20-5 Calculate sum of dealer's card pair 
    sum_of_dealer_card = cal_dealer_first_card+cal_dealer_second_card
    
    # 20-6 Print sum of dealer's cards.
    print(f"Dealer's card number: {sum_of_dealer_card}")

    hit_or_stay = input("Would you like to hit? (Y) or stay? (N)")
    while hit_or_stay.lower() not in ("y", "yes", "n", "no"):
        hit_or_stay = input(
            "If you want to split your card, please input 'Y'. If you want to keep go, input 'N'\n")
    # 21. If player wants hit, give a new cards.
    if hit_or_stay.lower() in ("y", "yes"):
        player_hit_card_1 = random_symbol, random_number
        
    # 21-1. Make sure the new card is not duplicated with revealed cards.
        while player_hit_card_1 in revealed_cards:
            random_number = random.choice(number_list)
            random_symbol = random.choice(symbol_list)
            player_hit_card_1 = random_symbol, random_number
            revealed_cards[random_symbol] = random_number
    print (player_card_pair, player_hit_card_1)


    # 22. Show new card to the player.
    print(f"Player's card: {first_split_card_pair}")
    for i in range(0, 1):
        sleep(1)

       # remove
    a = 1


print("See you later!")
