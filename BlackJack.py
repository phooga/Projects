import random

cardlist = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

card1 = random.choice(cardlist)
card2 = random.choice(cardlist)
dealer_card = random.choice(cardlist)
dealer_card2 = random.choice(cardlist)

card1_value = int
card2_value = int
card3_value = int
card4_value = int
card5_value = int
dealer_card_value = int
dealer_card2_value = int
dealer_card3_value = int
dealer_card4_value = int
dealer_card5_value = int

def card_values(cardtype):
    if cardtype == "K" or cardtype == "Q" or cardtype == "J":
        cardint = 10
    elif cardtype == "A":
        cardint = 1
    else:
        cardint = cardtype

    return cardint

# Set card values and face cards to integers
card1_value = card_values(card1)
card2_value = card_values(card2)
dealer_card_value = card_values(dealer_card)
dealer_card2_value = card_values(dealer_card2)

# Keep track of cards
dsum = dealer_card_value + dealer_card2_value
sum = card1_value + card2_value

# Info for user and input
print(f"Your starting hand is: {card1} {card2}")
print(f"Dealer's card is: {dealer_card}")
choice = input("Would you like to hit or stand? (h/s): ")

# If user decides to hit
if choice.lower() == "h":
    print("")
    card3 = random.choice(cardlist)
    card3_value = card_values(card3)
    print(f"Your hand is now: {card1} {card2} {card3}")
    sum = sum+card3_value
    if sum > 21:
        print("Dang you lost")
        exit()
    if dsum < 17:
        dealer_card3 = random.choice(cardlist)
        dealer_card3_value = card_values(dealer_card3)
        print("Dealer hit")
        dsum = dsum + dealer_card3_value
        if dsum > 21:
            print("Dealer bust, you win!")
            exit()
    else:
        print("Dealer did not hit")


        # player second choice
    choice2 = input("Would you like to hit or stand? (H/S): ")
    if choice2.lower() == "h":
        print("")
        card4 = random.choice(cardlist)
        card4_value = card_values(card4)
        print(f"Your hand is now: {card1} {card2} {card3} {card4}")
        sum = sum + card4_value
        if sum > 21:
            print("Dang you lost")
            exit()
        if dsum < 17:
            dealer_card4 = random.choice(cardlist)
            dealer_card4_value = card_values(dealer_card4)
            print("Dealer hit")
            dsum = dsum + dealer_card4_value
            if dsum > 21:
                ("Dealer bust, you won!")
                exit()
        else:
            print("Dealer did not hit")


        choice3 = input("Would you like to hit or stand? (H/S): ")
        if choice3.lower() == "h":
            print("")
            card5 = random.choice(cardlist)
            card5_value = card_values(card5)
            print(f"Your hand is now: {card1} {card2} {card3} {card4} {card5}")
            sum = sum + card5_value
            if sum > 21:
                print("Dang you lost")
                exit()
            if dsum < 17:
                dealer_card5 = random.choice(cardlist)
                dealer_card5_value = card_values(dealer_card5)
                print("Dealer hit")
                dsum = dsum + dealer_card5_value
                if dsum > 21:
                    ("Dealer bust, you won!")
                    exit()
            else:
                print("Dealer did not hit")
        elif choice3.lower() == "s":
            print("")
            if dsum < 17:
                dealer_card5 = random.choice(cardlist)
                dealer_card5_value = card_values(dealer_card5)
                print("Dealer hit")
                dsum = dsum + dealer_card5_value
                if dsum > 21:
                    ("Dealer bust, you won!")
                    exit()
            else:
                print("Dealer did not hit")
            print(f"Dealer's cards: {dealer_card} {dealer_card2} {dealer_card3}")
            if sum > dsum:
                print("Yoo you actually won")
                exit()
            else:
                print("Dang you lost")
                exit()

    elif choice2.lower() == "s":
        print("")
        if dsum < 17:
            dealer_card4 = random.choice(cardlist)
            dealer_card4_value = card_values(dealer_card4)
            print("Dealer hit")
            dsum = dsum + dealer_card4_value
            if dsum > 21:
                ("Dealer bust, you won!")
                exit()
        else:
            print("Dealer did not hit")
        print(f"Dealer's cards: {dealer_card} {dealer_card2} {dealer_card3}")
        if sum > dsum:
            print("Yoo you actually won")
            exit()
        else:
            print("Dang you lost")
            exit()

# If user decides to stand first time
elif choice.lower() == "s":
    print("")
    if dsum < 17:
        dealer_card3 = random.choice(cardlist)
        if dealer_card3 == "K" or dealer_card3 == "Q" or dealer_card3 == "J":
            dealer_card3_value = 10
        elif dealer_card3 == "A":
            dealer_card3_value = 1
        else:
            dealer_card3_value = dealer_card3
        dsum = dsum + dealer_card3_value
        if dsum > 21:
            print("Dealer bust, you win!")
            exit()
        print("Dealer hit")
        print(f"Dealer's cards: {dealer_card} {dealer_card2} {dealer_card3}")
    else:
        print(f"Dealer's cards: {dealer_card} {dealer_card2}")
    print("")
    if sum > dsum:
        print("Yoo you actually won")
        exit()
    else:
        print("Dang you lost")
        exit()