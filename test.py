import random

game = True
player_hand = []
dealers_hand = []
chips = 10
bet = 0 

#lager kortstokk    1
def fresh_deck():
    a = 1
    kortstokk = []
    symboler = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Jack", "Queen", "King"]
    for x in symboler:
        for a in range(10):
            a += 1
            kortstokk.append([a,x])
        for y in ranks:
            kortstokk.append([y,x])
    return(kortstokk)

#blander kortstokk    2
def shuffle_deck(kortstokk):
    random.shuffle(kortstokk)
    return(kortstokk)



#Chatgpt opprettet denne funksjonen. Konverterer int til str
def number_to_word(n):
    num_words = {
        1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'
    }
    return(num_words.get(n))



#Tar et kort og fjerner det fra listen (hand parameter)
def deal_hand(hand):
    card = random.choice(hand)
    hand.remove(card)
    return card



while game:
    print("---------")
    print("Blackjack")
    print("---------")
    print(" ")
    print(" ")
    while game:
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
    print(f"You betted {bet} and have {chips} left")
    print(" ")
    #lager kortstokk
    fresh_deck()
    #blander kortstokk
    deck =  shuffle_deck(fresh_deck())
    #ferdig blandet kortstokk  
    #del ut kort
    print("Cards have been dealt!")
    player_hand.append(deal_hand(deck))
    print(f"You got {player_hand} a total value of {number_to_word(player_hand)}")
    dealers_hand.append(deal_hand(deck))
    print(f"Dealer got {dealers_hand[0]}")
