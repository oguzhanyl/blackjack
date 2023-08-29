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

user_cards = []
computer_cards = []

# Oyun sonunu sağlayacağımız kontrol noktası:
is_game_over = False

# Kullanıcı ve bilgisayarın eline rastgele iki kart veren döngü:
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"    Your cards : {user_cards}, current score : {user_score}")
print(f"    Computer's first card : {computer_cards[0]}")

# Oyun sonu şartlarını taşıyan koşul:
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True