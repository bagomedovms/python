class Fighter:
    def __init__(self, name, power, energy, health):
        self.name = ''
        self.power = 100
        self.energy = 100
        self. health = 100
action = input('Enter action (hit/struggle/protection: ')
if action == 'hit':


    def struggle(self, energy):
        self.energy -= 10
        self.power -= 10


    def hit(self, power, energy):
        self.energy -= 5
        self.power -= 5

    def protection(self, energy, health):
        self.energy -= 5
        self.health -= 10

class wrestler(Fighter):
    def __init__(self, name, power, energy, health):
        self.name = name
        self.power = power
        self.energy = energy
        self. health = health

class Boxer(Fighter):
    def __init__(self, name, power, energy, health):
        self.name = name
        self.power = power
        self.energy = energy
        self. health = health