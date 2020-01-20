# BLACK JACK GAME ---

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = [] # Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_cmp = ''
        for card in self.deck:
            deck_cmp += '\n'+card.__str__()
        return "The deck has: "+deck_cmp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
class Hand:
    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0 # Add an attribute to keep track of ace

    def add_card(self,card):
        self.cards.append(card)
        self.values += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips would you like to bet: "))
        except:
            print("\nSorry! Please provide an integer")
        else:
            if chips.bet > chips.total:
                print("\nSorry you don't have enough chips to bet")
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("\nHit or Stand? Enter H or S : ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("\nPlayer stands Dealer's turn")
            playing = False
        else:
            print("\nSorry, didn't understand that, please hit H or S only")
            continue
        break

def show_some(player, dealer):
    print("\nDealer Hand:-")
    print("One card hidden")
    print(dealer.cards[1])
    print("\nPlayer Hand:-")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("\nDealer Hand:-")
    for card in dealer.cards:
        print(card)
    print("\nPlayer Hand:-")
    for card in player.cards:
        print(card)

def player_busts(player, dealer, chips):
    print("\nDealer Won!! Player Busted.")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPlayer Won!! Dealer Busted")
    chips.win_bet()

def push(player, dealer):
    print("\nDealer & Player Tie!!")

while True:
    print("________________Welcome to BlackJack____________________")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.values > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        
        if player_hand.values <= 21:
            while dealer_hand.values < player_hand.values:
                hit(deck,dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.values > 21:
                player_wins(player_hand, dealer_hand, player_chips)
                break
            elif dealer_hand.values > player_hand.values:
                player_busts(player_hand, dealer_hand, player_chips)
                break
            elif dealer_hand.values < player_hand.values:
                player_wins(player_hand, dealer_hand, player_chips)
                break
            else:
                push(player_hand, dealer_hand)
                break

    print("\nPlayer has total chips at : {}".format(player_chips.total))

    new_game = input("\nWould you like to play another hand? Y/N : ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nGood Bye!! See you soon.")
        break

    

