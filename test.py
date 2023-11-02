import random

#lager kortstokk
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

#blander kortstokk
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

fresh_deck()
shuffle_deck(fresh_deck())

#print(shuffle_deck(fresh_deck()))

e = 0 
for x in fresh_deck():
    e += 1

print(e)


def deal_hand(hand):
    random.choices(hand)
    hand.pop()

    return hand