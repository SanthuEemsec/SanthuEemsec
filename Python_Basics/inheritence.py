#Inheritence
class User(object):
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self, name, power): #dunger methods part of python we never code it like __init__
        self.name = name #_name is understandable as a private
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):  # dunger methods part of python we never code it like __init__
        self.name = name  # _name is understandable as a private
        self.age = num_arrows

    def attack(self):
        print(f'attacking with power of {self.num_arrows}')

Player1 = Wizard('santhu', 27)
print(Player1.sign_in())
Player1.attack()
print(isinstance(Player1, object)) #imp to know this
#print(Player1.speack())
#print(Player1._name)
