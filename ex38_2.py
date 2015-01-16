import random

face_cards = ["jack", "queen", "king", "ace"]
num_cards = ["2","3","4","5","6","7","8","9","10"]
suites = ["clove","spade","heart","diamond"]
deck = []

all_cards = num_cards + face_cards

for suite in suites:
    for card in all_cards:
        to_add = card + " " + suite
        deck.append(to_add)

picked_card = deck[random.randrange(0,52)]

print picked_card
