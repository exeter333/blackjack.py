import random
import sys
cards = list(range(1,14))
deck = cards * 4
random.shuffle(deck)
class Player:
    cards = []
    def __init__(self, money=0, bet=0):
        self.money = money
        self.bet = bet
    def change_bet(self, bet):
        self.bet = bet
    def add_card(self):
        card = deck.pop()
        if card==1:
            self.cards.append("A")
        elif card==11:
            self.cards.append("J")
        elif card==12:
            self.cards.append("Q")   
        elif card==13:
            self.cards.append("K")
        else:
            self.cards.append(card)
    def check_cards(self):
        total = 0
        for card in self.cards:
            if(card=="A"):
                if(len(self.cards)==2):
                    total += 10
                else:
                    total += 1
            if(card=="J" or card=="Q" or card=="K"):
                total += 10
            elif(isinstance(card, int)):
                total += card
        return total
    def can_split(self):
        if self.cards[0] == self.cards[1]:
            return True
        return False
    def check_win(self, playerPts, dealerPts, deal):
        if(playerPts>21 and dealerPts>playerPts):
            print(deal.cards)
            print(dealerPts)
            print("You win!!!")
            self.money += self.bet*2
            return True
        elif(playerPts>21 and dealerPts<playerPts):
            print(deal.cards)
            print(dealerPts)
            print("You lose!!!")
            return True
        elif(playerPts<21 and dealerPts>21):
            print(deal.cards)
            print(dealerPts)
            print("You win!!!")
            self.money += self.bet*2
            return True
        elif(player_points==21):
            print("Blackjack!! You win!!!")
            self.money += self.bet*2
            return True
        elif(dealer_points==21):
            print(deal.cards)
            print(dealerPts)
            print("Blackjack!! You lost!!!")
            return True
        else:
            print("\nDealer: " + str(deal.cards[:-1]) + " X")
            return False
            

class Dealer:
    cards = []
    def __init__(self):
        self.money = 999999
    def add_card(self):
        card = deck.pop()
        if card==1:
            self.cards.append("A")
        elif card==11:
            self.cards.append("J")
        elif card==12:
            self.cards.append("Q")   
        elif card==13:
            self.cards.append("K")
        else:
            self.cards.append(card)
        #random generator for card numbers when pulled
    def check_cards(self):
        total = 0
        for card in self.cards:
            if(card=="A"):
                if(len(self.cards)==2):
                    total += 10
                else:
                    total += 1
            if(card=="J" or card=="Q" or card=="K"):
                total += 10
            elif(isinstance(card, int)):
                total += card
        return total


p1 = Player(1000, 0)
deal = Dealer()
player_points = 0
dealer_points = 0
print("WELCOME TO BLACKJACK")
play = True
while(play==True):
    cards = list(range(1,14))
    deck = cards * 4
    random.shuffle(deck)
    p1.cards = []
    deal.cards = []
    real_bet = False
    bet = 0
    while(real_bet==False):
        bet = int(input("Place your bets!: "))
        if(bet<1):
            print("You think this is kindergarten? Fuck with the house and the house fucks with you! Please input a real bet:")
        else:
            real_bet = True
    p1.change_bet(bet)
    p1.money -= bet
    print("Bets placed! These are your cards!")
    p1.add_card()
    p1.add_card()
    deal.add_card()
    deal.add_card()
    print(p1.cards)
    print(p1.check_cards())
    split = p1.can_split()
    firstHandPoints = 0
    secondHandPoints = 0
    if(split):
        choice = input("Would you like to split? Y for yes and N for no").upper()
        if choice=="Y":
            temp = p1.cards
            splitCard1 = [temp[0]]
            p1.cards = splitCard1
            p1.add_card()
            splitCard2 = [temp[1]]
            p1.cards = splitCard2
            p1.add_card()
            print("First hand: " + str(splitCard1))
            print("Second hand: " + str(splitCard2))
        else:
            split = False
    print("\nDealer: " + str(deal.cards[0]) + " X")
    player_points = p1.check_cards()
    dealer_points = deal.check_cards()
    end = False
    while(end==False):
        hit_or_stand = input("\nHit or Stand? Press 1 for hit, 0 for stand: ")
        if hit_or_stand=="1":
            if(split):
                p1.cards = splitCard1
                p1.add_card()
                firstHandPoints = p1.check_cards()
                print("First hand of cards: " + str(p1.cards) + " " + str(firstHandPoints))
                p1.cards = splitCard2
                p1.add_card()
                secondHandPoints = p1.check_cards()
                print("Second hand of cards: " + str(p1.cards) + " " + str(secondHandPoints))
                deal.add_card()
                dealer_points = deal.check_cards()
                if(firstHandPoints>21):
                    print("First hand is out")
                    bet -= bet/2
                    p1.cards = splitCard2
                    player_points =  p1.check_cards()
                    dealer_points =  deal.check_cards()
                    split = False
                    end = p1.check_win(secondHandPoints, dealer_points, deal)
                if(secondHandPoints>21):
                    print("Second hand is out")
                    bet -= bet/2
                    p1.cards = splitCard1
                    dealer_points =  deal.check_cards()
                    split = False
                    end = p1.check_win(firstHandPoints, dealer_points, deal)
                if(secondHandPoints>21 and firstHandPoints>21):
                    print("Both hands over 21. You lose!!!")
                    split = False
                    end = True
                elif(secondHandPoints==21 or firstHandPoints==21):
                    print("You win!!!")
                    p1.money += bet/2
                    split = False
                    end = True
            else:
                p1.add_card()
                print(p1.cards)
                player_points = p1.check_cards()
                print(player_points)
                if(player_points>21):
                    print("You lose!!!")
                    end = True
                else:
                    deal.add_card()
                    dealer_points = deal.check_cards()
                    end = p1.check_win(player_points, dealer_points, deal)
                
        if(hit_or_stand=="0"):
            if(split):
                if(firstHandPoints>secondHandPoints):
                    p1.cards = splitCard1
                elif(secondHandPoints>firstHandPoints):
                    p1.cards = splitCard2
            player_points = p1.check_cards()
            dealer_points = deal.check_cards()
            print("\nPlayer: " + str(p1.cards))
            print(player_points)
            print("\nDealer: " + str(deal.cards))
            print(dealer_points)
            if(player_points>dealer_points):
                dealer_under = True
                while(dealer_under):
                    deal.add_card()
                    print("\nDealer: " + str(deal.cards))
                    dealer_points = deal.check_cards()
                    print(dealer_points)
                    if(dealer_points>21):
                        print("You win!!!")
                        p1.money += bet*2
                        end = True
                        dealer_under = False
                    else:
                        if(dealer_points>player_points):
                            print("You lose!!!")
                            end = True
                            dealer_under = False
            elif(player_points==dealer_points):
                print("It's a draw!!!")
                p1.money += bet
                end = True
            else:
                if dealer_points<21:
                    print("You lose!!!")
                    end = True
                else:
                    print("You win!!!")
                    end = True
        if hit_or_stand=="9":
            sys.exit()
        if(end==True):
            another = input("Press Y for another round! If you wish to exit, press N: ").upper()
            if another=="N":
                print("Total money: " + str(p1.money))
                play = False
            else:
                print("Total money: " + str(p1.money))
                continue
sys.exit()
