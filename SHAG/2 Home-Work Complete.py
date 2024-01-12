import random

class Student:

    def __init__(self, name):
        self.name = name  
        self.progress = 0
        self.gladness = 0
        self.money = 0
        self.alive = True
        self.day = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.day += 1
        self.live(self.day)  
        if not self.alive:
            raise StopIteration
        return self

    def study(self):
        print('time to lear smth new')
        self.progress += 0.12
        self.gladness += 5
        self.money += 10
        
        def live(self, day):
            print(f"Day {day} of {self.name}'s life")

    def sleep(self):
        print("Time to sleep")
        self.gladness += 3
        self.money -= 1

    def chill(self):
        print('Time to relax')
        self.gladness += 4
        self.progress -= 0.1
        self.money -= 1

    def work(self):
        print('Time to work')
        self.money += 5

    def is_alive(self):
        if self.progress < -0.5:
            print('Opps..')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression..')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {round(self.progress, 2)}')
        print(f'Money - {self.money}')

    def live(self, day):
        print(f'Day {day} of {self.name} life')
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.chill()
        else:
            self.work()

        self.end_of_day()
        self.is_alive()

nick = Student('Nick')
for day in nick:
   print(day)