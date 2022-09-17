# class Character:            #Создаем первый класс
#     pass
#
# peter = Character()         #Создаем объект peter - отдельный представитель класса
# # print(type(peter))          #<class '__main__.Character'>
#
# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#     backpack = []    #добавляем атрибут с изменяемым типом - списком, т.е создаем персонажу инвентарь, куда можно помещать какие то экземпляры класса
#
#
#     def eat(self, food):  # пишем функцию в которой если энергия персонажа меньше ста она прибавляется на количетсво еды
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def do_exercise(self, hours):  # функция зарядки перса: если энергия > 0 то она падает, а сила растет
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):  # фукнция смены имени
#         print(self)  # просто смотрим для чего тут self
#         self.alias = new_alias
#
#
#     def beat_up(self, foe):
#         if not isinstance(foe, Character):   #метод isinstance проверяет является ли объект экземпляром класса указанного через запятую
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat')
#
# #все атрибуты после объявления класса хранятся в (Character.__dict__)
#
#
# #при вызове класса мы всегда создаем новый объект
# #у конкретного экземпляра будут все те же атрибуты, что и у его класса
# peter = Character()
# # print(peter.name)
# # print(peter.power)
# # print(peter.energy)
# # print(peter.hands)
#
# #присваеваем экземпляру свои атрибуты:
# peter.name = 'Peter Parker'
# peter.power = 70
#
# #и даже те которых изначально в классе нет
# peter.alias = 'Spider-Man'
#
# #измененные атрибуты уже будут храниться в словаре самого класса peter.__dict__
# #все что осталось неизменным относительно класса(чертежа) в нем и хранится
#
# # интерфейсом назывваются все описанные и предназначение для вызова методы которые в нем
#
# #еще раз проинициализируем создание экземпляра
# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85
# bruce.alias = 'Batman'
#
# # print(bruce.alias)  #пока нет псевдонима, выдается ошибка атрибута
#
# bruce.change_alias('Batman')  #добавим псевдоним
# # print(bruce.alias)
#
# bruce.change_alias('Dark Knight')     #изменим псевдоним
# # print(bruce.alias)
#
# # bruce.do_exercise(1)        #теперь тренируемся и видим как работает эта функция
# # print(bruce.power)
# # print(bruce.energy)
# # bruce.do_exercise(2)
# # print(bruce.power)
# # print(bruce.energy)
#
# peter = Character()
# bruce = Character()
#
# peter.backpack.append('web-shooters') #добавим питеру веб-шутеры
# # print(peter.backpack)
#
# #наглядный пример работы<class 'int'> классов:
# num1 = 5        #числа являются экземплярами класса int т.е <class 'int'>
# num2 = 10
# # print(num1 + num2)  #мы видим понятную нам визуальную оболочку
# # print(num1.__add__(num2))   #то что происходит на самом деле
#
# # peter = Character('Peter Parker', 80)
# # bruce = Character('Bruce Wayne', 85)
# # bruce.beat_up(peter)
# # print(peter.status)
# # print(bruce.status)

# НАСЛЕДОВАНИЕ

class Character:
    name = ''
    power = 0
    energy = 100
    hands = 2

class Spider:
    power = 0
    energy = 50
    hands = 8

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMam(Character, Spider):
    pass

peter_parker = SpiderMam()
# print(peter_parcer.name)
# print(peter_parcer.power)
# print(peter_parcer.energy)
# print(peter_parcer.hands)
# peter_parcer.webshoot()

# чтобы понять какой метод откуда наследуется, воспользуемся методом МРО(или Линеаризация - способ пердставления дерева в линейном виде)

# print(SpiderMam.mro())      #[<class '__main__.SpiderMam'>, <class '__main__.Character'>, <class '__main__.Spider'>, <class 'object'>]


# ПОЛИМОРФИЗМ
# Полиморфизм - это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта т.е
# он позволяет методам с одинаковыми именами реализовывать разную функциональность для разных классов


#ПЕРЕОПРЕДЕЛЕНИЕ
#если в дочернем классе создать свой метод, который одноименный с родительским, то мы будем не наследовать родительский, а использовать его
#ПЕРЕГРУЗКА - в питоне перегрузки не существует, в нем все переопределяется

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):                 #метод который сообщает о том что перс просто двтгается
        print('Changing position')

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

    def move(self):               #тот же метод что и у класса Character, только двигается на паутине, до движения вызывается метод webshoot
        self.webshoot()
        print('Changing position')

class SpiderMan(Character, Spider):
    def turn_spider_sence(self):
        self.energy -= 10
        self.power += 20

# peter_parker = SpiderMan('Peter Parker', 80)
# peter_parker.move()

#Функция super() позволяет из дочернего класса обращаться к родительским методам, даже если одноименный метод есть в дочернем
#т.е она пропускает этап поиска в себе, обходя линию мро
#еще проще - мы не смотрим в себе, смотрим только в родителе и берем из него
#он нужен только в тех ситуациях когда нужен род-й метод, но одн оименный уже есть в текущем

class SpiderMan(Character, Spider):
    #польностью наследуем от родителя инициализацию и добавляем новый атрибут для экземпляра
    def __init__(self, name, power):    #полностью вызываем ини-ю родителя
        super().__init__(name, power)   #и добавляем к ней рюкзак
        self.backpack = []

# peter_parker = SpiderMan('Peter Parker', 80)
# print(peter_parker.backpack)
# print(peter_parker.power)
# print(peter_parker.energy)
# print(peter_parker.hands)

# еще один пример с функцией super():

    def webshoot(self):
        if 'web' in self.backpack:
            self.webshoot()
        else:
            print('No web!')

    def move(self):
        self.webshoot()
        print('Moving on 3 square')

# peter_parker = SpiderMan('Peter Parker', 80)
# peter_parker.webshoot()                         #проверяем метод webshoot
# peter_parker.backpack.append('web')             #теперь добавляем паутину в рюкзак
# peter_parker.webshoot()                     #RecursionError: maximum recursion depth exceeded

#это ошибка рекурсии. это происходит потому что вызывая метод webshoot(), в нем выполняется условие на проверку паутины
#и т.к мы ее добавили то переходит на след строку где где вызывается этот же метод. так происходит  рекурсия

        #исправляем:
    def webshoot(self):
        if 'web' in self.backpack:
            super().webshoot()      #берем метод не из своего класса, а из родительского
        else:
            print('No web!')

peter_parker = SpiderMan('Peter Parker', 80)
peter_parker.webshoot()
peter_parker.backpack.append('web')
peter_parker.webshoot()