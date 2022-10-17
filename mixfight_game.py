class Fighter:
    def __init__(self, name, power, energy, health=100):
        self.name = name
        self.power = power
        self.energy = energy
        self.health = health
# action = input('Enter action (hit/struggle/protection: ')
# if action == 'hit':

    def choise_style(self):
        if self.power < self.energy:
            Fighter == wrestler
            print('Ваш боец класса "борец"')
        else:
            Fighter == boxer
            print('Ваш боец класса "боксер"')



    def struggle(self, energy):
        self.energy -= 10
        self.power -= 10


    def hit(self, power, energy):
        self.energy -= 5
        self.power -= 5

    def protection(self, energy):
        self.energy -= 5
        self.health -= 10

class wrestler(Fighter):
    def __init__(self, name, power, energy, health=100):
        self.name = name
        self.power = power
        self.energy = energy
        self. health = health

class boxer(Fighter):
    def __init__(self, name, power, energy, health=100):
        self.name = name
        self.power = power
        self.energy = energy
        self. health = health

khabib = Fighter('haba', 70, 90)
konor = Fighter('konor', 95, 70)
khabib.choise_style()
konor.choise_style()