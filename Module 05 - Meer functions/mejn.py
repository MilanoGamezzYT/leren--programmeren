import random

class Board:
    def __init__(self):
        self.board = [0]*40
    
    def move_pawn(self, pawn, steps):
        old_pos = self.board[pawn]
        new_pos = (old_pos + steps) % 40
        self.board[pawn] = new_pos
    
    def is_winner(self, pawn):
        return self.board[pawn] == 39

class Dice:
    def __init__(self):
        self.value = None
    
    def roll(self):
        self.value = random.randint(1,6)

class Card:
    def __init__(self, text, action):
        self.text = text
        self.action = action
    
    def execute(self, player):
        print(f"Card: {self.text}")
        self.action(player)

class Deck:
    def __init__(self):
        self.cards = [
            Card("Pay $50", lambda player: player.pay(50)),
            Card("Collect $100", lambda player: player.collect(100)),
            Card("Move to start", lambda player: player.move_to(0)),
            Card("Advance to Boardwalk", lambda player: player.move_to(39)),
        ]
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, id):
        self.id = id
        self.pawn = id*4
        self.money = 1500
    
    def pay(self, amount):
        self.money -= amount
    
    def collect(self, amount):
        self.money += amount
    
    def move_to(self, position):
        self.pawn = position

class Game:
    def __init__(self):
        self.board = Board()
        self.dice = Dice()
        self.deck = Deck()
        self.players = [Player(i) for i in range(4)]
        self.current_player = None
    
    def start(self):
        self.current_player = self.players[0]
        while True:
            self.play_turn()
            if self.board.is_winner(self.current_player.pawn):
                print(f"Player {self.current_player.id} wins!")
                break
            self.current_player = self.get_next_player()
    
    def play_turn(self):
        self.dice.roll()
        steps = self.dice.value
        print(f"Player {self.current_player.id} rolls {steps}")
        self.board.move_pawn(self.current_player.pawn, steps)
        
        card = self.deck.draw()
        card.execute(self.current_player)
    
    def get_next_player(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % len(self.players)
        return self.players[next_index]

game = Game()
game.start()
