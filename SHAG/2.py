import random

class Student:

    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 0
        self.money = 100
        self.alive = True

    def study(self):
        print('Час вчити щось нове')
        self.progress += 0.12
        self.gladness += 5
        self.money -= 10

    def sleep(self):
        print("Час спати")
        self.gladness += 3

    def chill(self):
        print('Час розслабитися')
        self.gladness += 4
        self.progress -= 0.1
        self.money -= 20

    def work(self):
        print('Час працювати')
        self.money += 50

    def is_alive(self):
        if self.progress < -0.5:
            print('Ой..')
            self.alive = False
        elif self.gladness <= 0:
            print('Депресія..')
            self.alive = False
        elif self.money <= 0:
            print('Брак коштів..')
            self.alive = False

    def end_of_day(self):
        print(f'Радість - {self.gladness}')
        print(f'Прогрес - {round(self.progress, 2)}')
        print(f'Гроші - {self.money}')

    def live(self, day):
        print(f'День {day} життя {self.name}')
        if self.money <= 0:
            self.work()
        elif self.progress < 0:
            self.study()
        else:
            rnd = random.randint(1, 3)
            if rnd == 1:
                self.study()
            elif rnd == 2:
                self.sleep()
            else:
                self.chill()

        self.end_of_day()
        self.is_alive()

class Cat:

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.sleepiness = 0
        self.happiness = 10
        self.alive = True

    def eat(self):
        print(f'{self.name} is eating')
        self.hunger -= 5
        self.happiness += 1

    def sleep(self):
        print(f'{self.name} is sleeping')
        self.sleepiness -= 5
        self.happiness += 1

    def play(self):
        print(f'{self.name} is playing')
        self.hunger += 2
        self.sleepiness += 2
        self.happiness += 3

    def is_alive(self):
        if self.hunger > 10:
            print('Starvation..')
            self.alive = False
        elif self.sleepiness > 10:
            print('Exhaustion..')
            self.alive = False
        elif self.happiness < 0:
            print('Depression..')
            self.alive = False

    def end_of_day(self):
        print(f'Happiness - {self.happiness}')
        print(f'Hunger - {self.hunger}')
        print(f'Sleepiness - {self.sleepiness}')

    def live(self, day):
        print(f'Day {day} of {self.name}\'s life')
        if self.hunger > 7:
            self.eat()
        elif self.sleepiness > 7:
            self.sleep()
        else:
            self.play()

        self.end_of_day()
        self.is_alive()

nick = Student(name='Nick')
KotRuguk228 = Cat(name='KotRuguk228')

for day in range(365):
    if not nick.alive:
        break
    nick.live(day)

for day in range(365):
    if not KotRuguk228.alive:
        break
    KotRuguk228.live(day)
