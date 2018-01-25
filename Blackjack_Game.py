# Here are the requirements:

# Use OOP and classes in some portion of your game
# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the players total money.
# You need to alert the player of wins, losses, or busts, etc...

#create a deck of cards
import random
deck = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']*4

#specify that face cards = 10 and 'Ace' is either 1 or 11

class Player(object):
    
    def __init__(self):
        print ('Player joins the table')
    
    def stand(self):
        pass 
    
    def hit(self):
        pass
    
class Dealer(object):
    
    def __init__(self):
        print ('Dealer welcomes the Player. ')
    
    def deal(self):
        print ('Dealer deals...')
        print (random.choice())
            
        
        
        
player = Player()
dealer = Dealer()

dealer.deal()

