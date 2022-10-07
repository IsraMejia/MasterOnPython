
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
    #Class Object atributte
    membership = True

    def __init__(self, name = 'default_name' , age = 0) :
        #if (self.membership):
        #if (PlayerCharacter.membership): #if the instance has membership
        if (age > 18):
            self.name = name #Instance Attributes
            self.age =age
    
    def run (self): #Method
        print('run')

    def shout(self):
        print(f'My name es {self.name}')
    
    def phrase(self, text):
        print(f'My name is {self.name}, and I want say: {text}')


player1 = PlayerCharacter('Isra', 24)
player2 = PlayerCharacter('Pam', 22)

print(f'\nPlayer 1 created, name: {player1.name}')
print(f'Memory location: {player1} \n')
player1.run()

print(f'\n\nPlayer 2 created, name: {player2.name}')
print(f'Memory location: {player2}')
player2.shout()

player1.phrase('Estoy mamadisimo alv jaja')
