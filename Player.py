class Player(object):
    
    def __init__(self, name):
        self.hand = []
        self.val = []
        self.name = name
        self.money = 200
        self.bet_money = None
        self.spend = []
        self.spent = None
        self.gain = []
        self.have_gain = None
        #self.value = #[sum(self.hand) if 'Jack', 'Queen', 'King' not in self.hand]

    def append_value(self):
        for card in self.hand:
            for v in card.split(' '):
                if v.isdigit():
                    self.val.append(int(v))
                elif v =='Ace':
                    self.val.append(1)
                elif v in ['King', 'Queen', 'Jack']:
                    self.val.append(10)
        
    def append_value2(self):
        for v in self.hand[-1].split(' '):
            if v.isdigit():
                self.val.append(int(v))
            elif v =='Ace':
                self.val.append(1)
            elif v in ['King', 'Queen', 'Jack']:
                self.val.append(10)     
        print(f'{self.name} new value is {self.val}')

    def show_value(self):
        print(f'{self.name} value is {self.val}')
    
    def sum_value(self):
        return sum(self.val)
    
    def calculate_val(self):
        return self.sum_value()%10

    def show_cal_val(self):
        print(f'{self.name} calculated value is {self.calculate_val()}')

    def show_hand(self):
        #[print(f'your hand have {k}') for k in self.hand]
        # [print(f'{k}') for k in self.hand]
        print(f'card in {self.name} hand is {sorted(self.hand)}')

    def reset_hand(self):
        self.hand.clear()
        self.val.clear()
        self.bet_money = None
    
    def put_bet_money(self, bet_money):
        self.money -= bet_money
        self.bet_money = bet_money

    def append_bet_money(self):
        self.spend.append(self.bet_money)
        self.make_spent()
    
    def make_spent(self):
        self.spent = sum(self.spend)

    def append_gain(self):
        self.gain.append(self.bet_money)
        self.gains()

    def gains(self):
        self.have_gain = sum(self.gain)
    
    def life(self):
        if self.money >= 0:
            return True
        return False