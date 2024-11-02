from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name_, power):
        self.name_ = str(name_)
        self.power = int(power)
        super().__init__()
    def run(self):
        enemy = 100
        day = 0
        print(f'{self.name_}, на нас напали!')
        while enemy > 0:
            enemy = enemy - self.power
            sleep(1)
            day += 1
            print(f'{self.name_} сражается {day} день(дня, дней), осталось {enemy} воинов.')
        else:
            print(f'{self.name_} одержал победу спустя {day} дней(дня)!')
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')