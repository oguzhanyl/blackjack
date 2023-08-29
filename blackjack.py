import random

def deal_card():
    """Returns a random card from the cards /Kartlar listesinden rastgele bir kart döndürür."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards./Kartların bir listesini al ve kartlardan hesaplanan puanı döndür."""
    # Blackjack olursa koşul:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Kartlar 21'in üstünde ancak içerisinde as varsa 11'i 1 ile değiştiren koşul:
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Koşulların içerisine girerse değişen haliyle girmezse orijinal haliyle kartları toplayıp döndürüyoruz.
    return sum(cards)
