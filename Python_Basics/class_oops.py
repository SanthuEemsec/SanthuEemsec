class PlayerCharacter:
    #class object attribute
    membership = True
    #def __init__(self, name, age):
    def __init__(self, name='anonymous', age=0):# To safeguard can have a default name and age
        #if(self.membership == True):
        #if(PlayerCharacter.membership == True):
         if(age > 18):
            self.name = name #Attributes
            self.age = age

    @classmethod
        def adding_method((cls, num1, num2):


    def run(self):
        print('run')
        return 'done'

Player1 = PlayerCharacter('Santhu', 27)
Player2 = PlayerCharacter("ABHI", 28)

print(Player1.name)
print(Player1.age)
print(Player1.run())
print(Player2.name)
print(Player2.age)
print(Player1)
print(Player1.membership)


#help(Player1)


