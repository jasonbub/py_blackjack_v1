# -*- coding: utf-8 -*-
"""
Black Jack
Version: Alpha 0.1
Created on Wed Jan  2 23:41:46 2019

@author: Jason Bubenicek
"""

import random
from IPython.display import clear_output
import os
from colorama import init
init()
from colorama import Fore

PLAYERS = []
HOUSE = []

def cls():
    # https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    os.system('cls' if os.name=='nt' else 'clear')
    

class Card():
    '''
    Usage:
    Create instances of each card in the deck.
    As you hand them out, make sure to appropriately set
    the .visible attribute to True or False based on
    whether or not it should be shown to all players, such as
    the Dealer's 2nd Card, or 
    '''
    
    # Use the 'visible' attribute to determine
    # whether or not to show this card to the
    # players.
    hidden = False
    
    def __init__(self,suit,name,value, color, suit_no, name_short):
        
        self.suit = suit
        self.name = name
        self.value = value
        self.color = color
        self.suit_no = suit_no
        self.name_short = name_short
        
        self.suit_icon = '♥♦♣♠'[suit_no]
        
        if self.color == "Red":
            self.suit_icon = Fore.RED + self.suit_icon + Fore.WHITE 
    
        self.card_line1 = f'┌───────┐'
        self.card_line2 = f'| {self.name_short:<2}    |'
        self.card_line3 = f'|       |'
        self.card_line4 = f'|   {self.suit_icon}   |'
        self.card_line5 = f'|       |'
        self.card_line6 = f'|    {self.name_short:>2} |'
        self.card_line7 = f'└───────┘' 
    
    def set_hidden(self):
        self.hidden = True
        
        self.card_line1 = f'┌───────┐'
        self.card_line2 = f'| {"?":<2}    |'
        self.card_line3 = f'|       |'
        self.card_line4 = f'|   {"?"}   |'
        self.card_line5 = f'|       |'
        self.card_line6 = f'|    {"?":>2} |'
        self.card_line7 = f'└───────┘' 

    def set_visible(self):
        self.hidden = False
        
        self.card_line1 = f'┌───────┐'
        self.card_line2 = f'| {self.name_short:<2}    |'
        self.card_line3 = f'|       |'
        self.card_line4 = f'|   {self.suit_icon}   |'
        self.card_line5 = f'|       |'
        self.card_line6 = f'|    {self.name_short:>2} |'
        self.card_line7 = f'└───────┘' 

    def show_card(self):
                
        print(self.card_line1)
        print(self.card_line2)
        print(self.card_line3)
        print(self.card_line4)
        print(self.card_line5)
        print(self.card_line6)
        print(self.card_line7)

class Deck():
    
    # Create a blank list to hold the cards that are
    # added to this Deck
    # cards = []
    
    # These lists will be used to populate the Deck
    suits = [("Hearts","Red",0),("Diamonds","Red",1),("Clubs","Black",2),("Spades","Black",3)]
    names = [("Two",2,"2"),("Three",3,"3"),("Four",4,"4"),("Five",5,"5"),("Six",6,"6"),("Seven",7,"7"),("Eight",8,"8"),("Nine",9,"9"),("Ten",10,"10"),("Jack",10,"J"),("Queen",10,"Q"),("King",10,"K"),("Ace",11,"A")]
    
    def __init__(self):
        self.cards = []
        
        # When the Deck class is instanstiated, populate it with a fresh
        # deck of cards
        for suit in self.suits:
            for name in self.names:
                display_suit, color, suit_no = suit
                display_name, value, name_short = name
                card = Card(suit, display_name, value, color,suit_no, name_short)
                self.cards.append(card)
                
                # Shuffle the desk to randomize the next card.
                random.shuffle(self.cards)
                
    def hit(self,player):
    
        # Select the next card in the deck.
        # card = self.cards.pop()
        card = self.cards[0]
                
        card.set_visible()
        player.add_card(card)
    
        # Once the card has been given out, we need to make sure to
        # remove it from the Deck, so that no one else gets the same
        # card.
        del self.cards[0]
    
    def deal(self,at_table):
        '''
        Usage:
        At the beginning of the game, deal the cards to each player.
        '''
        
        for card_number in [1,2]:
            for player in at_table:
                
                card = self.cards[0]
                
                if player.player == "Dealer" and card_number == 2:
                    # The Dealer shows their 2nd card to all players.  Let's
                    # make it visible.
                    card.set_hidden()
                    
                player.add_card(card)
                
                # Once the card has been given out, we need to make sure to
                # remove it from the Deck, so that no one else gets the same
                # card.
                del self.cards[0]
    
    def show_deck(self):
        for card in self.cards:
            print(card.show_card())
    
    # Use the print() command to get a message that contains the
    # number of cards remaining in the deck. This is good to ensure
    # that you are removing cards from the Deck as you hand them out
    # to players.
    def __str__(self):
        return f"There are {len(self.cards)} in the deck"
        
    
    # This will provide you a numeric count of cards in the deck.  You
    # should use this to ensure that the deck has been populated with
    # the standard 52 and as you hand them out that the number is reducing
    # appropriately.
    def __len__(self):
        return len(self.cards)

class Hand():
    '''
    Usage:
    You should create an instance of Hand for each player in the game.  It will
    contain a list of the cards that the player has in their hand.  Initially, the
    .cards attribute will have 0 cards.  You can use the .add_card() method to 
    pass in a card.
    '''
    cards = []
    busted = False
    amount_bet = 0
    
    def __init__(self, player, amount_bet):
        self.cards = []
        self.player = player
        self.amount_bet = amount_bet
        # print("Hand created.")
        
    def add_card(self, card):
        '''
        Pass in a Card object and don't forget to remove it from the deck afterward.
        '''
        self.cards.append(card)
        # print(f"Card added, {self.player} now has {len(self.cards)} in their hand.")


    def hand_total(self):
        '''
        Usage:
        Call .hand_total to get a numeric representation of the current Hand value.
        '''
        aces = 0
        hand_value = 0

        for card in self.cards:
            if not card.hidden:
                hand_value += card.value
            if card.name == "Ace":
                aces += 1

        if hand_value <= 21:
            # print(f"NOT BUST: Hand value is: {hand_value}")
            return hand_value
        elif hand_value > 21 and aces == 0:
            # print(f"BUST: This hand has a value of {hand_value}, which is over 21 and there are {aces} Aces.")
            return hand_value
        else:
            # print(f"This hand has a value of {hand_value}, but has {aces} Ace(s), will attempt to convert to 1")

#            while aces > 0:
            while aces:
                # This hand as at least 1 Ace, we will attempt to convert it to a 1 and then
                # sum the hand again to see if it is 21 or less.  This will be repeated
                # if there are more Aces in the hand and the sum total remains over 21.
                aces -= 1
                hand_value -= 10
                if hand_value <= 21:
                    # print(f"NOT BUST: Hand value is: {hand_value}")
                    return hand_value
                elif hand_value > 21 and aces == 0:
                    # print(f"BUST: This hand after changing the Aces to a value 1, is now {hand_value}, which is over 21 and it has {aces} Aces left.")
                    return hand_value
                else:
                    # print("Changing another Ace to 1")
                    continue
                    

    def check_bust(self):
        '''
        Usage:
        Call .check_bust() to see if this Hand is in BUST state or not.
        '''
        if self.hand_total() > 21:
            self.busted = True
            return True
        else:
            self.busted = False
            return False

     
    def show_hand(self):
        for card in self.cards:
            print(card.card_line1, sep=' ', end='', flush=True)

        print()

        for card in self.cards:
            print(card.card_line2, sep=' ', end='', flush=True)

        print()

        for card in self.cards:
            print(card.card_line3, sep=' ', end='', flush=True)

        print()

        for card in self.cards:
            print(card.card_line4, sep=' ', end='', flush=True)

        print()

        for card in self.cards:
            print(card.card_line5, sep=' ', end='', flush=True)

        print()

        for card in self.cards:
            print(card.card_line6, sep=' ', end='', flush=True)

        print()

        for card in self.cards:
            print(card.card_line7, sep=' ', end='', flush=True)
            
        print(f"\n{self.player} Total: {self.hand_total()}")
    
    def __str__(self):
        hand_value = 0
        hand_display = []
        print(f"{self.player} has the following cards:")
        print("===============================================")
        for card in self.cards:
            hand_value += card.value
            # print(f"{card.name} of {card.suit} with a value of {str(card.value)} and a visibility of {str(card.visible)}")
            hand_display.append(f"{card.name} {card.suit[0]}")
        
        return str(f"{self.player}: {self.hand_value()}")
    
    def __len__(self):
        '''
        Usage:
        Use the len() function to return the number of cards in the Hand
        '''
        return len(self.cards)
    

def check_for_naturals(dealer, player):
    '''
    Usage:
    Use this function after the hands have been dealt by calling
    it with each player and the dealer hand.  It will return one
    of four values; Both, Dealer, Player, None
    '''
    result = None
    
    if dealer.hand_total() == 21 and player.hand_total == 21:
        result = "Both"
    elif dealer.hand_total() == 21:
        result = "Dealer"
    elif player.hand_total() == 21:
        result = "Player"
    else:
        result = "None"
    
    return result 

class Player():
    
    win_loss_amount = 0
    current_hand = None
    previous_hands = []
    
    def __init__(self, name):
        self.name = name
    
    def set_current_hand(self, hand):        
        Player.current_hand = hand

    def set_previous_hand(self,hand):
        Player.previous_hands.append(hand)
        
    def get_winnings(self):
        result = 0
        
        for hand in self.previous_hands:
            result += hand.amount_won
            
        return result
    
    def __len__(self):
        return len(self.previous_hands)
    
    def __str__(self):
        return f"{self.name} has played {len(self.previous_hands)} and won/loss: ${self.get_winnings()}."
    
def dealer_play(dealer, d):
    
    # Make sure that all of the dealer cards are now visible and
    # able to be counted.
    for card in dealer.cards:
        card.set_visible()
        
    # Have the dealer continue to Hit until their hand is greater than
    # 17 and less than 21 (in other words, haven't BUSTED)
    while 17 > dealer.hand_total() < 21:

        # print(f"{dealer.player} has to HIT with Hand of {dealer.hand_total()}.")
#        hit(dealer, d)
        d.hit(dealer)

        clear_output()
        cls()
        dealer.show_hand()

        if dealer.check_bust():
            print(f"{dealer.player} busted!")
            # x = input("Ready to proceed")
            
def player_play(player, dealer, d):

    clear_output()
    cls()
      
    dealer.show_hand()
    player.show_hand()

    hit_continue = True

    while player.hand_total() < 21 and hit_continue:

        response = ""

        while response.lower() not in ['y','yes', 'n', 'no']:

            response = input(f"{player.player}: Would you like a card? Enter 'Yes', 'No'").lower()

        if response[0] == 'y':
            print(f"{player.player} wants card")
#            hit(player, d)
            d.hit(player)

            clear_output()
            cls()
            dealer.show_hand()
            player.show_hand()

            if player.check_bust():
                print("Sorry, you busted")
                hit_continue = False

        else:
            print(f"{player.player} wants to 'stay'")  
            hit_continue = False


def get_bets(player_hands):
    
    for player_hand in player_hands:
        bet = 0
        
        while bet not in range(20,100):
            try:
                bet = int(input(f"{player_hand.player}, how much would you like to bet? ($20 to $100)?"))
            except:
                print("You must enter a numeric value between 20 and 100.")
                bet = 0
            
        player_hand.amount_bet = bet

def play():
    # Get the Deck populated and shuffled
    d = Deck()
    
    if input("Would you like to review the deck, first (y/n)?") == "y":
        d.show_deck()
        
        input("Press any key to continue.")
    
    # Generate a list of Hands one for each players
    playing_hands = []

    for hand_id in range(0,len(PLAYERS)):
        playing_hands.append(Hand(f"{PLAYERS[hand_id].name}", 20))
    
    dealer_hand = Hand("Dealer", 0)


    # Populate the player_hands and the players (including the Dealer) in the at_table lists
    player_hands = []
    at_table = []
    
    for playing_hand in playing_hands:
        player_hands.append(playing_hand)    
        at_table.append(playing_hand)

    at_table.append(dealer_hand)
    
    # Deal the cards to the players.
#    deal(at_table, d)
    d.deal(at_table)
    
    # Ask each player to determine how much they are going to bet this round.
    get_bets(player_hands)
    
    # Iterate through each of the player, and allow
    # them to select as many cards as they'd like
    # until they BUST or STAY

    # print(f"# of Players playing the Dealer is: {len(players)}")
    # a = input("Ready to proceed")
    for player_hand in player_hands:
        
        player_play(player_hand,dealer_hand, d)
        
    dealer_play(dealer_hand, d)

    # Check to see who won
    clear_output()
    cls()
    dealer_hand.show_hand()
    player_index = 0
    
    for player_hand in player_hands:
        
        player_hand.show_hand()
        print("\n===============================================")

        print(f"Checking {player_hand.player}'s results.")


        if player_hand.busted:
            print(f"{player_hand.player} BUSTED!")
            print(f"Removing ${player_hand.amount_bet} from {PLAYERS[player_index].name}'s Win/Loss balance.")
            PLAYERS[player_index].win_loss_amount -= player_hand.amount_bet
            HOUSE[0].win_loss_amount += player_hand.amount_bet
            
        elif ((dealer_hand.busted) and (not player_hand.busted)) or ((not player_hand.busted) and player_hand.hand_total() > dealer_hand.hand_total()):
            print(f"{player_hand.player} Won!")
            print(f"Adding ${player_hand.amount_bet} to {PLAYERS[player_index].name}'s Win/Loss balance.")
            PLAYERS[player_index].win_loss_amount += player_hand.amount_bet
            HOUSE[0].win_loss_amount -= player_hand.amount_bet
            
        elif (not player_hand.busted) and player_hand.hand_total() == dealer_hand.hand_total():
            print(f"Push!")
        else:
            print("Dealer Won!")
            print(f"Removing ${player_hand.amount_bet} from {PLAYERS[player_index].name}'s Win/Loss balance.")
            PLAYERS[player_index].win_loss_amount -= player_hand.amount_bet
            HOUSE[0].win_loss_amount += player_hand.amount_bet
        
        player_index += 1
            
    print("Game over.")
    
    
def start_game():
    '''
    Usage:
    Call start_game() to start the game.
    '''
    
    ready = ""
    clear_output()
    cls()
    print("=========================================================================================================")
    print("=                                                                                                       =")
    print("=                                                                                                       =")
    print("= Black Jack                                                                                            =")
    print("= At the famous, Casino Bub                                                                             =")
    print("=                                                                                                       =")
    print("=                                                                                                       =")
    print("=                                                                                                       =")
    print("=========================================================================================================\n\n\n")
          

    # Ask how many players
    
    
    # Setup player objects
    player_player1 = Player("Jason Bubnicek")
    player_player2 = Player("Dayna Bubenicek")
    PLAYERS.append(player_player1)
    PLAYERS.append(player_player2)
    
    HOUSE.append(Player("Dealer"))

          
    # Continue to ask if the player would like to play until
    # they indicate that they want to Quit the game.
    while ready.lower() not in ["q", "quit", "exit", "end"]:

        print(f"House has won: ${HOUSE[0].win_loss_amount}")
        
        for player in PLAYERS:
            print(f"{player.name} has won: ${player.win_loss_amount}")

        ready = input("Would you like to play? ('Yes', 'No', 'Quit')")

        if ready.lower() in ["y", "yes"]:

            print("Let's play Black Jack")
            
            # input("Right before play")
            play()
            
            ready = ""


    print("Thanks for playing!")  

if __name__ == "__main__":
    
    start_game()

