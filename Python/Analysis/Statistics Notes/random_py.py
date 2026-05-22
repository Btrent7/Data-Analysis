import random
for toss in range(1):
    coin = random.choice(["heads", "tails"])
    print(coin)

print()

from random import choice
for toss in range(2):
    coin = choice(["heads", "tails"])
    print(coin)

print()

num = random.randint(1, 10)
print(num)

print()

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)

print()