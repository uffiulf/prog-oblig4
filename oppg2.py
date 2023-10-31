import random

Ace =1
Two =2
Three =3
Four =4
Five =5
Six =6
Seven =7
Eight =8
Nine =9
Jack =10
Queen =10
King =10

chips = 0
Hit = 1
Stand = 2

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Jack, Queen, King]
    deck = [f"{rank} of {suit}" for x in suits for y in ranks]
    return deck

def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

