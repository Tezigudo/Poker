import random

class card:
    def __init__(self):
        self.deck = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
       # self.deck.append([[deckzaza(v, s) for v in range(13)] for s in ['Heart', 'Diamonds', 'Clubs', 'Spades' ]])

       self.deck.append('Joker')
       for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades' ]:
           for v in range(1, 14):
                if v == 1:
                    v = 'Ace' 
                elif v == 11:
                    v = 'Jack'
                elif v == 12:
                    v = 'Queen'
                elif v == 13:
                    v = 'King'
                            
                self.deck.append(f'{v} of {s}')
    
    def show_deck(self):
        [print(_) for _ in self.deck]

    def shuffle(self):
        return random.shuffle(self.deck)
    
    def reset_deck(self):
        self.deck.clear()
        self.create_deck()
        self.shuffle()