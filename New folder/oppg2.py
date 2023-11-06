import random

state = 1
chips = 10
bet = 0 

#lager kortstokk    1
def fresh_deck():
    a = 0
    kortstokk = []
    symboler = ["Hearts", "Diamonds", "Clubs", "Spades"]
    for x in symboler:
        for a in range(13):
            a += 1
            kortstokk.append([a,x])
    return(kortstokk)

#blander kortstokk    2
def shuffle_deck(kortstokk):
    random.shuffle(kortstokk)
    return(kortstokk)



#Chatgpt opprettet denne funksjonen. Konverterer int til str
def number_to_word(n):
    num_words = {
        1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Jack', 12: 'Queen', 13: 'King'
    }
    return(num_words.get(n))   #Finner match med .get og returnerer verdien



#Tar et kort og fjerner det fra listen (hand parameter)  ,hjelp fra chatgpt her også
def deal_hand(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def value_card(card):
    value = 0
    for x in card:
        if isinstance(x[0], int):    #Sjekker om det er en int, lærte av chatgpt
            value += x[0]
        elif card[0] == "Ace":     
            value = 11 if card >= 21 else 1 
        elif x[0] in ["Jack", "Queen", "King"]:
            value = 10
    return value
        



while state == 1:    
    player_hand = []
    dealers_hand = []
    total_value = 0
    print("---------")
    print("Blackjack")
    print("---------")
    print(" ")
    print(" ")
    while state == 1:
        try:
            bet = int(input(f"You have {chips} chips, bet to start :"))
            if bet > chips:
                print(f"you have only {chips} chips, try again")
            elif bet != int(bet):
                print("Only value of integer are allowed")
            elif bet < 0 or bet == 0:
                print("No cheating!")
            else: 
                break
        except ValueError:
               print("Only value of integer are allowed")

    chips -= bet
    print(f"You betted {bet} and have {chips} chips left")
    print(" ")
    #lager kortstokk
    fresh_deck()
    #blander kortstokk
    deck =  shuffle_deck(fresh_deck())
    #ferdig blandet kortstokk  

    #del ut kort
    print("Cards have been dealt!")
    player_hand.append(deal_hand(deck))
    player_hand.append(deal_hand(deck))
   
    card_dealt1 =number_to_word(player_hand[0][0])
    card_dealt2 =number_to_word(player_hand[1][0])
    print(f"You got dealt {card_dealt1} of {player_hand[0][1]} and {card_dealt2} of {player_hand[1][1]}")

    total_value = value_card(player_hand)
    print(f"Your total value is: {total_value}")
    print(" ")

    
    #dealer kort
    dealers_hand.append(deal_hand(deck))
    dealers_hand.append(deal_hand(deck))
    dealers_card1 = number_to_word(dealers_hand[0][0])
    dealer_value = value_card(dealers_hand)
    print(f"The Dealers visible card {number_to_word(dealers_hand[0][0])} of {dealers_hand[0][1]} ")
    state = 2
    #spilleren får valg
    while(state == 2):
        answer = 0
        if total_value == 21:
            print("You got 21! You win!")
            chips += bet * 2
            state = 1 
            break
        elif total_value > 21:
            print("You got over 21! You lose!")
            state = 1
            break
        elif total_value < 21:
            answer = input("Do you want to hit(2) or stand(1)? ")
            if answer == "1":
                print("You chose to stand")
                print(f"Your total value is: {total_value}")
                print(" ")
                print(" ")
                print(" ")
                state = "dealers_turn"
                #dealer sin tur
                while state == "dealers_turn":
                    if value_card(dealers_hand) < 17:
                        print(f"Dealers hiddeen card is: {number_to_word(dealers_hand[1][0])} of {dealers_hand[1][1]}")
                        dealers_hand.append(deal_hand(deck))
                        print(f"Dealer got dealt {number_to_word(dealers_hand[2][0])} of {dealers_hand[2][1]}")
                        print(f"Dealer total value is: {value_card(dealers_hand)}")
                        if value_card(dealers_hand) > 21:
                            print("Dealer got over 21! You win!")
                            chips += bet * 2
                            state = 1
                            break
                        elif value_card(dealers_hand) > total_value:
                            print("Dealer got higher than you! You lose!")
                            state = 1
                            break
                        elif value_card(dealers_hand) == total_value:
                            print("You got the same as the dealer! No one wins!")
                            chips + bet
                            state = 1
                            break
                        elif value_card(dealers_hand) < total_value:
                            print("You got higher than the dealer! You win!")
                            chips += bet * 2
                            state = 1
                            break
                
            elif answer == "2":
                state = 3
                while state == 3:
                    print("You chose to hit")
                    player_hand.append(deal_hand(deck))
                    card_dealt3 = number_to_word(player_hand[2][0])
                    print(f"You got dealt {card_dealt3} of {player_hand[2][1]}")
                    total_value = value_card(player_hand)
                    print(f"Your total value is: {total_value}")
                    state = 2
        