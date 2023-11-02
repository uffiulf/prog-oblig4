import random

blackjack = 21
chips = 100
Hit = 1
Stand = 2
player_hand_value = 0    #summen av kortene til spilleren
dealer_hand_value = 0    #summen av kortene til dealer

#dictionary med kortverdier
card_values = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}


#Lager liste med kortstokk, legger suits og ranks i en ny liste deck
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "Two", "Three","Four", "Five", "Six", "Seven", "Eight", "Nine", "Jack", "Queen", "King"]
    deck = []
    for x in ranks:
        for y in suits:
            deck.append([x,y])    
    return deck

#Fjerner kort fra kortstokk etter utdeling 
def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


def change_ace(hand):
    if sum(hand) > blackjack:
        for x in hand:
            if x == Ace:
                    hand - 10
                    return hand


while True:
    player = input("Press enter to start a new game")
    print(f"You have {chips} chips")
    while True:
        bet = int(input("How many chips do you want to bet? "))
        chips -= bet  #trekker innsatsen fra total chips
        print(f"You bet {bet} chips")
        if bet > chips:
            print("You don't have enough chips")
        else:
            break
    deck = create_deck()
    player_hand = []
    dealer_hand = []
    #Spiller
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    #Dealer
    dealer_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    #Fikk hjelp av chatgpt til å lage en funksjon som regner ut summen av kortene til spilleren
    for x in player_hand:
        player_hand_value += card_values[x[0]]
    
    for x in dealer_hand:
        dealer_hand_value += card_values[x[0]]



   # print(player_hand[0])
    #player_hand_value = player_hand

    #Viser kortene til spiller og dealer (dealer viser bare ett kort)
    print(f"Your hand is {player_hand} with a value of {player_hand_value}")
    #Fikk hjelp av chatgpt å vise verdien av det ene kortet til dealer
    print(f"The dealers visible card is a {dealer_hand[0]} with a value of {card_values[dealer_hand[0][0]]} ")

    #Spillerens tur
    while True:
        action = int(input("Press 1 to hit or 2 to stand "))
        if action == Hit:
            player_hand.append(deal_card(deck))
           #legg inn funksjon som endrer Ace om summen er over 21
            player_hand = change_ace(player_hand) 

            print(f"Your hand is {player_hand}")
            if sum(player_hand) > blackjack:
                print("You went bust")
                break
        elif action == Stand:
            break
        else:
            print("Invalid input")

    #Dealerens tur
    
