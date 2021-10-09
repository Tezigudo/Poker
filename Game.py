from Card import card
from Player import Player
import random, time

class computer_player(Player):
    def if_call(self):
        if  self.calculate_val() <= 5:
            game.draw(g1, self)
            self.append_value2()

    def if_bet(self):
        if self.money <= 60:
            self.put_bet_money(15)
        else:
            self.put_bet_money(25)

class game:

    def __init__(self, P1, P2 = None, P3 = None, P4 = None, P5 = None):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        self.P5 = P5
        self.deck = card()
        self.deck.deck.remove('Joker')
        self.make_Player()
        self.player_list = [self.P1, self.P2, self.P3, self.P4, self.P5]
        self.player_turple = (self.P1, self.P2, self.P3, self.P4, self.P5)
        self.pp_list = ['P1', 'P2', 'P3', 'P4', 'P5']
        self.pp_turple = ('P1', 'P2', 'P3', 'P4', 'P5')
        self.money_list = [self.P1.money, self.P2.money, self.P3.money, self.P4.money, self.P5.money]
        self.max_money = []
        self.dealer = []

    def make_Player(self):
        if [self.P2, self.P3, self.P4, self.P5] == [None, None, None, None]:
            self.P1 = Player(str(input('Enter your name: ')))
            self.P2 = computer_player('Bot1')
            self.P3 = computer_player('Bot2')
            self.P4 = computer_player('Bot3')
            self.P5 = computer_player('Bot4')
        elif self.P2 != None and [self.P3, self.P4, self.P5] == [None, None, None]:
            self.P1 = Player(str(input('Enter player1 name: ')))
            self.P2 = Player(str(input('Enter player2 name: ')))
            self.P3 = computer_player('Bot1')
            self.P4 = computer_player('Bot2')
            self.P5 = computer_player('Bot3')
        elif [self.P2, self.P3] != [None, None] and [self.P4, self.P5] == [None, None]:
            self.P1 = Player(str(input('Enter player1 name: ')))
            self.P2 = Player(str(input('Enter player2 name: ')))
            self.P3 = Player(str(input('Enter player3 name: ')))
            self.P4 = computer_player('Bot1')
            self.P5 = computer_player('Bot2')
        elif [self.P2, self.P3, self.P4] != [None, None, None] and self.P5 is None:
            self.P1 = Player(str(input('Enter player1 name: ')))
            self.P2 = Player(str(input('Enter player2 name: ')))
            self.P3 = Player(str(input('Enter player3 name: ')))
            self.P4 = Player(str(input('Enter player4 name: ')))
            self.P5 = computer_player('Bot1')
        else:
            self.P1 = Player(str(input('Enter player1 name: ')))
            self.P2 = Player(str(input('Enter player2 name: ')))
            self.P3 = Player(str(input('Enter player3 name: ')))
            self.P4 = Player(str(input('Enter player4 name: ')))
            self.P5 = Player(str(input('Enter player5 name: ')))

    def draw(self, Players):
        Players.hand.append(self.deck.deck[0])
        self.deck.deck.pop(0)
    
    def Deal_card(self):
        for _ in range(2):
            self.draw(self.P1)
            self.draw(self.P2)
            self.draw(self.P3)
            self.draw(self.P4)
            self.draw(self.P5)

    def win_condition(self, Player, deng = None):
        def Pok8():
            return len(Player.hand) == 2 and Player.calculate_val() == 8      
        
        def Pok9():
            return len(Player.hand) == 2 and Player.calculate_val() == 9

        def Twice_card():
            if len(Player.hand) == 2:
                name = []
                for c in Player.hand:
                    for a in c.split(' '):
                        if a.isdigit() or (a in ['King', 'Queen', 'Jack', 'Ace']):
                            name.append(a)
                return len(set(name)) == 1

        def Thrice_card():
            if len(Player.hand) == 3:
                name = []
                for c in Player.hand:
                    for a in c.split(' '):
                        if a.isdigit() or (a in ['King', 'Queen', 'Jack', 'Ace']):
                            name.append(a)
                return len(set(name)) == 1
                    
        if Pok8():
            print(f'{Player.name} Pok 8!')
            return False
        elif Pok9():
            print(f'{Player.name} Pok 9!')
            return False
        elif Twice_card():
            print(f'{Player.name} Twice card!')
            deng = 2
            return True
        elif Thrice_card():
            print(f'{Player.name} Thrice card!')
            deng = 3
            return True

        if deng != None and self.if_more_than_dealer_val(Player) == '5':
            if deng == 2:
                Player.money -= Player.bet_money
                Player.bet_money*2
            elif deng == 3:
                Player.money -= Player.bet_money*2
                Player.bet_money*3
    
        return True

    def show_win_con(self, computer):
        if not self.win_condition(computer):
            computer.show_hand()
        else:
            computer.if_call()
        self.win(computer)

    def Player_play(self, Players):
        def ask():
            ans = input('Do you want to draw?\n(y/n)')
            if ans in ['Y', 'y']:
                self.draw(Players)
                Players.show_hand()
                Players.append_value2()
                Players.show_cal_val()
            elif ans not in ['N', 'n']:
                print('invalid input')
                ask()
        Players.show_hand()
        Players.append_value()
        Players.show_value()
        Players.show_cal_val()
        if not self.win_condition(Players):
            Players.show_hand()
        else:
            ask()
        self.win(Players)
        print()

    def Computer_play(self, computer):
        computer.append_value()
        self.show_win_con(computer)
        computer.show_hand()
        computer.show_cal_val()
        print()

    def Player_bet_money(self, Players):
        Players.put_bet_money(int(input(f'Now {Players.name} Money is {Players.money}.\nput your bet here: ')))
        print(f'{Players.name} had bet {Players.bet_money}.\n{Players.name} has {Players.money} left.')

    def computer_bet_money(self, computer):
        computer.if_bet()
        print(f'{computer.name} had bet {computer.bet_money}')

    def compu_bet_money(self):
        for p in self.player_list:      
            if str(type(p)) == "<class 'Player.Player'>":
                self.Player_bet_money(self.__getattribute__(str(self.pp_list[self.player_list.index(p)]))) 
            elif str(type(p)) == "<class '__main__.computer_player'>":
                self.computer_bet_money(self.__getattribute__(str(self.pp_list[self.player_list.index(p)]))) 

    def append_peep_max_money(self):
        for money in self.money_list:
            if money == max(self.money_list):
                self.max_money.append(money)

    def show_all_spent_money(self):
        for pla in self.player_turple:
            print(f'{pla.name} has spent {pla.spent} and gain {pla.have_gain}')
    
    def select_dealer(self): #select dealer from richest player
        self.append_peep_max_money()
        
        if len(self.max_money) != 1:
            wakko = random.choice(self.player_turple)
            self.dealer.append(wakko)
            self.player_list.remove(wakko)
            self.pp_list.pop(self.player_turple.index(wakko))

        for x in self.player_turple:
            if (x.money == self.max_money) and (len(self.max_money) == 1):
                self.dealer.append(x)
                self.player_list.remove(self.dealer)
                self.pp_list.pop(self.player_turple.index(x))
        print(f'Dealer in this turn is {self.dealer_player().name}')
                
    def dealer_player(self):
        return self.dealer[0]
   
    def show_all_player_money(self):
        for P in self.player_turple:
            print(f'{P.name} has {P.money} left')

    def show_lose_peep(self):
        for pla in self.player_turple:
            if pla.money <= 0:
                print(f'{pla.name} lose and have money {pla.money}')
            else:
                print(f'{pla.name} win with have money {pla.money}')

    def if_more_than_dealer_val(self, Players):
        if Players in self.player_list:
            if Players.calculate_val() > self.dealer_player().calculate_val():
                return '5'
            elif Players.calculate_val() < self.dealer_player().calculate_val():
                return '6'
            elif Players.calculate_val() == self.dealer_player().calculate_val():
                return '7'
            
    def win(self, peep):
        if peep  in self.player_list:
            if self.if_more_than_dealer_val(peep) == '5':
                self.dealer_player().money -= peep.bet_money
                peep.money += peep.bet_money*2
                self.dealer_player().spend.append(peep.bet_money)
                peep.append_gain()
                print(f'{peep.name} gains {peep.bet_money}')

            elif self.if_more_than_dealer_val(peep) == '6':
                self.dealer_player().money += peep.bet_money
                peep.append_bet_money()
                self.dealer_player().gain.append(peep.bet_money)
                print(f'{peep.name} lost {peep.bet_money}')
            
            elif self.if_more_than_dealer_val(peep) == '7':
                peep.money += peep.bet_money
                print('Draw!')

    def if_win(self):
        if not self.win_condition(self.dealer_player()):
            for o in self.player_turple: #need to fix
                self.win(o)
    
    def play_comp(self):
        for p in self.player_turple:
                if str(type(p)) == "<class 'Player.Player'>":
                    self.Player_play(self.__getattribute__(str(self.pp_turple[self.player_turple.index(p)]))) 
                elif str(type(p)) == "<class '__main__.computer_player'>":
                    self.Computer_play(self.__getattribute__(str(self.pp_turple[self.player_turple.index(p)])))
        
    def clear_game(self):
        self.dealer.clear()
        self.pp_list.clear()
        self.player_list.clear()
        for i in self.player_turple:
            i.reset_hand()
        for k in self.player_turple:
            self.player_list.append(k)
        for j in self.pp_turple:
            self.pp_list.append(j)
        self.deck.reset_deck()

    def if_play(self):
        life = [cbt.life() for cbt in self.player_turple]
        return all(life)

    def play(self): #dealer has no bet need to fix next time. 
        i = 0
        while self.if_play():
            i += 1
            print(f'round {i}')
            self.select_dealer()
            self.compu_bet_money()
            self.Deal_card()
            if not self.win_condition(self.dealer_player()):
                for o in self.player_list:
                    o.show_hand()
                    o.append_value()
                    o.show_value()
                    o.show_cal_val()
                self.win(o)
            else:    
                self.play_comp()
            self.show_all_player_money()
            self.show_all_spent_money()
            self.clear_game()
        else:
            self.show_lose_peep()
            
def lobby():
    print('''
Welcome to Pok-Deng Game
Develop by God
dont forget to subscribe me 
''')
    anss = str(input('''please choose what you want to do 
    Play ----1
    Quit ----2\n :'''))
    if anss == '1':
        into_game()
    elif anss == '2':
        for t in range(3, 0, -1):
            print(f'Program going to quit in {t} secs', end = '\r')
            time.sleep(1)
    else:
        print('Invalid input')
        lobby()

def into_game():
    global g1
    try:
        ans = int(input('how many player did you play? (max=5): '))
        if ans == 1:
            g1 = game('')
        elif ans == 2:
            g1 = game('', '')
        elif ans == 3:
            g1 = game('', '', '')
        elif ans == 4:
            g1 = game('', '', '', '')
        elif ans == 5:
            g1 = game('', '', '', '', '')
        else:
            print('Invalid input')
            quit()
        g1.play()
    except ValueError:
        print('Invalid input')
        into_game()

if __name__ == '__main__':
    g1 = None
    lobby()