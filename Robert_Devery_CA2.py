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

# The Card class is used to create each instance of a card in the game
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

# The Hand class creates the hands for the player and the dealer
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):  # add a card to the player's or dealer's hand
        self.cards.append(card)
        self.value += card.get_value()
    
# Functions for playing the game

# hit adds a new card to a hand
def hit(deck, hand):
    hand.add_card(deck.get_random_card())

# hit_or_stand checks if the player wants to add a card (hit) or not (stand)
def hit_or_stand(deck, hand):
    global playing

    while True:
        h_or_s = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")

        if h_or_s[:1].lower() == 'h':
            hit(deck, hand)
        elif h_or_s[:1].lower() == 's':
            print("\nPlayer stands, Dealer is playing.")
            playing = False
        else:
            print("Invalid entry. Please enter 'h' or 's'.")
            continue
        break

# hidden displays the opening hands where one of the dealer's cards is hidden from view
def hidden(player_hand, dealer_hand):
    print("\nDealer's Hand: ")
    print(" <Card Hidden>", dealer_hand.cards[1], sep = "\n ")
    print("\nPlayer's Hand: ", *player_hand.cards, sep = "\n ")
    print("Player's Hand =", player_hand.value)

# visible displays both hands after the player's turn is over
def visible(player_hand, dealer_hand):
    print("\nDealer's Hand: ", *dealer_hand.cards, sep = "\n ")
    print("Dealer's Hand =", dealer_hand.value)
    print("\nPlayer's Hand: ", *player_hand.cards, sep = "\n ")
    print("Player's Hand =", player_hand.value)

# win_conditions contains the various scenarios for winning or losing the game
def win_conditions(player_hand, dealer_hand):
    
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        visible(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            print("\nDealer busts! Player wins!")

        elif dealer_hand.value > player_hand.value:
            print("\nDealer wins!")

        elif dealer_hand.value < player_hand.value:
            print("\nPlayer wins!")
        else:
            print("\nPush! Player and Dealer tie!")

# This is where the user-facing part of the game begins
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

    # show the starting hands
    hidden(player_hand, dealer_hand)
    
    # play the game
    while playing:

        hit_or_stand(deck, player_hand)
        hidden(player_hand, dealer_hand)

        if player_hand.value > 21:      # this checks if the player busts and ends the game if necessary, the dealer doesn't need to play if the player busts
            visible(player_hand, dealer_hand)
            print("\nPlayer busts! Dealer wins!")
            playing = False
    
    # when the player has finished (and did not bust) the dealer plays and then the hands are compared to see who wins
    win_conditions(player_hand, dealer_hand)

    
# Ask player if they would like to play again
    new_game = input("\nWould you like to play again? Enter 'y' if Yes. Enter any other value to exit the game: ").lower()
    if new_game[:1] == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break
