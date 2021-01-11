# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 17:22:18 2020

@author: robde
"""

# Import required module

import random

# Define variable to control when the game is in progress
playing = True

# Create classes

# The Card classes is used to create each instance of a card in the game
class Card():
    def __init__(self, suit, rank, available = True):
        self.suit = suit
        self.rank = rank
        self.available = available

    def __str__(self):
        return "[ " + self.suit + " / " + self.rank + " ]"
        
    def get_value(self):
        if (self.rank == "2" or self.rank == "3" or
            self.rank == "4" or self.rank == "5" or
            self.rank == "6" or self.rank == "7" or
            self.rank == "8" or self.rank == "9" or
            self.rank == "10"):
            val = int(self.rank)
        elif (self.rank == "Jack" or self.rank == "Queen" or
              self.rank == "King"):
            val = 10
        elif (self.rank == "Ace"):
            val = 11
        return val

# The Deck class creates the deck of cards and controls whether they are available or have already been dealt
class Deck():
    def __init__(self):
        self.cards = []
        suits = ["HEARTS", "CLUBS", "SPADES", "DIAMONDS"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def get_random_card(self):
        while True:
            index = random.randint(0,51)
            if self.cards[index].available:
                self.cards[index].available = False
                return self.cards[index]
            
    def shuffle(self):
        random.shuffle(self.cards)

# The Hand class contains the hands for the player and the dealer
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):  # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += card.get_value()
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
# Functions for playing the game

# hit adds a new card to a hand
def hit(deck, hand):
    hand.add_card(deck.get_random_card())
    hand.adjust_for_ace()

# hit_or_stand checks if the player wants to add a card (hit) or not (stand)
def hit_or_stand(deck, hand):
    global playing

    while True:
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")

        if ask[:1].lower() == 'h':
            hit(deck, hand)
        elif ask[:1].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Sorry! I did not understand that! Please try again!")
            continue
        break

# hidden displays the opening hands where one of the dealer's cards is hidden from view
def hidden(player, dealer):
    print("\nDealer's Hand: ")
    print(" <Card Hidden>", dealer.cards[1], sep = "\n ")
    print("\nPlayer's Hand: ", *player.cards, sep = "\n ")
    print("Player's Hand =", player.value)

# visible displays both hands after the player's turn is over
def visible(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep = "\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep = "\n ")
    print("Player's Hand =", player.value)

# win_conditions contains the various scenarios for winning or losing the game
def win_conditions(player_hand, dealer_hand):
    
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        visible(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            print("Dealer busts! Player wins!")

        elif dealer_hand.value > player_hand.value:
            print("Dealer wins!")

        elif dealer_hand.value < player_hand.value:
            print("Player wins!")
            
        elif player_hand.value > 21:
            print("Player busts! Dealer wins!")
            
        else:
            print("Push! Player and Dealer tie!")
            
# Game controls
while True:
    print("Blackjack!")

    # create and shuffle deck and then deal two cards to the dealer and the player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.get_random_card())
    player_hand.add_card(deck.get_random_card())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.get_random_card())
    dealer_hand.add_card(deck.get_random_card())


    # show the starting hands, play the game, and check which hand wins
    hidden(player_hand, dealer_hand)
    
    while playing:

        hit_or_stand(deck, player_hand)
        hidden(player_hand, dealer_hand)

        if player_hand.value > 21:
            visible(player_hand, dealer_hand)
            print("\nPlayer busts! Dealer wins!")
            playing = False
        
    win_conditions(player_hand, dealer_hand)

    
# Ask player if they would like to play again
    new_game = input("\nWould you like to play again? Enter 'y' if Yes. Enter any other value to exit the game: ").lower()
    if new_game[:1] == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break
