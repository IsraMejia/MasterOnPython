
"""
class Dog: #Class
    pass 

Rex = Dog() #Instanciate of class Dog
Coco = Dog() #Instanciate of class Dog
Golis = Dog() #Instanciate of class Dog

print(f"Cree una clase rex : { type(Dog) }")
print(f"I created a object  : { type(Rex) }")
"""

class PlayerCharacter :
    def __init__(self, name ) :
        self.name = name
    
    def run (self):
        print('run')

player1 = PlayerCharacter('Isra')
player2 = PlayerCharacter('Pam')

print(f'Player 1 created, name: {player1.name}')
print(f'Memory location: {player1}')

print(f'\n\nPlayer 2 created, name: {player2.name}')
print(f'Memory location: {player2}')

