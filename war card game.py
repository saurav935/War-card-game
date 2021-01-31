import random

suit=['Hearts','Clubs','Spades','Diamond']
rank=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

# Card Class
class Card:
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit
        self.value=value[rank]

    def __str__(self):
        return (self.rank+' of '+self.suit)


# Deck Class
class Deck:

    def __init__(self):
        self.all_cards=[]
        for i in suit:
            for o in rank:
                self.all_cards.append(Card(i,o))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()




# Player Class
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# Game Setup
player1=Player('One')
player2=Player('Two')

new_deck=Deck()
new_deck.shuffle()




for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

game_on=True

round=0
while game_on:
    round+=1
    print(f'round {round}')

    if len(player1.all_cards)==0:
       print('player 1 is unable to play. GAME OVER!')
       print('player 2 WINS !!')
       game_on=False
       break

    elif len(player2.all_cards)==0:
        print('player 2 is unable to play')
        print('player 1 WINS !!')
        game_on=False
        break

# Starting a new game
    player_one_cards=[]
    player_one_cards.append(player1.remove_card())

    player_two_cards=[]
    player_two_cards.append(player2.remove_card())

    at_war= True

    while at_war:
        if player_one_cards[-1].value < player_two_cards[-1].value:

            player2.add_cards(player_two_cards)
            player2.add_cards(player_one_cards)

            at_war=False


        elif player_two_cards[-1].value < player_one_cards[-1].value:

            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)

            at_war=False

        else:
            print('WAR!')

            if len(player1.all_cards) < 5:
                print('player 1 is unable to play. GAME OVER!')
                print('player 2 WIN!')

                game_on=False
                break


            elif len(player2.all_cards) < 5:
                print('player 2 is unable to play. GAME OVER!')
                print('player 1 WiINS!')

                game_on=False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player1.remove_card())
                    player_two_cards.append(player2.remove_card())


