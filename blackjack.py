import random

def deal_card():
    """Returns a random card from the cards /Kartlar listesinden rastgele bir kart döndürür."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card