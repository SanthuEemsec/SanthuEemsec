#Private
class PlayerCharacter:
    def __init__(self, name, age): #dunger methods part of python we never code it like __init__
        self._name = name #_name is understandable as a private
        self._age = age

    def run(self):
        print('run')

    def speack(self):
        print(f'my name is {self._name}, and age is {self._age}')
        print('done')

Player1 = PlayerCharacter('santhu', 27)
Player1._name = 'San'
print(Player1.speack())
print(Player1._name)
