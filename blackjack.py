import random
import os
from artblack import logo

# Yeniden oyuna başladığımızda ekranı temizlemek için küçük bir fonksiyon:
def clear_terminal():
   os.system("cls" if os.name == "nt" else "clear")

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

# Kullanıcı ve bilgisayarın skorlarını karşılaştırıp sonucu söyleyen fonksiyon:
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

# Oyunu tekrar oynamak için fonksiyon içerisine alıyoruz.
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []

    # Oyun sonunu sağlayacağımız kontrol noktası:
    is_game_over = False

    # Kullanıcı ve bilgisayarın eline rastgele iki kart veren döngü:
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Kart çekme işlemini isteğe bağlı devam ettirecek while döngüsü:
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards : {user_cards}, current score : {user_score}")
        print(f"    Computer's first card : {computer_cards[0]}")

        # Oyun sonu şartlarını taşıyan koşul:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Oyun sonu koşulu sağlanmazsa kart çekme sorusu:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Bilgisayarın kartları 0 ile 17 arasındaysa onun destesine otomatik kart ekleyecek while döngüsü:
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Oyun sonu kimin kazandığını öğrenebilmek için compare() fonksiyonunu burada çağırıyoruz:
    print(compare(user_score, computer_score))

# Oyunu tekrar tekrar oynamak için while döngüsü içerisine fonksiyonu alıyoruz.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_terminal()
    play_game()