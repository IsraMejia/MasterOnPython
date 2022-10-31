
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

    @classmethod
    #def adding_things(n1, n2):
    def adding_things(cls, n1, n2):
        return cls('Alien', n1 + n2) #We can use the decorador classmethod, and cls to instance a object from the class


player1 = PlayerCharacter('Isra', 24)
player2 = PlayerCharacter('Ari', 22)

print(f'\nPlayer 1 created, name: {player1.name}')
print(f'Memory location: {player1} \n')
player1.run()

print(f'\n\nPlayer 2 created, name: {player2.name}')
print(f'Memory location: {player2}')
player2.shout()

player1.phrase('Estoy mamadisimo alv jaja\n\n')

#print(player1.adding_things(2, 3)) #error to have 3 by defect, cls, n2, n1 parameters
print(PlayerCharacter.adding_things(2,3)) #instance a class