from threading import Thread
import queue
from time import sleep
from random import randint
class Table:
     def __init__(self, namber):
         self.namber = namber
         self.guest = None
class Guest(Thread):
    def __init__(self, name_):
        super().__init__()
        self.name_ = name_
    def run(self):
        n = randint(3, 10)
        sleep(n)
class Cafe:
    def __init__(self, *tables):
        self.tables = []
        for i in tables:
            if isinstance(i, Table):
                self.tables.append(i)
        self.queue = queue.Queue()
    def guest_arrival(self, *guests):
        gost = list(guests)
        count = 0
        while count < len(self.tables):
            for table in self.tables:
                if table.guest is None:
                    g = gost.pop(0)
                    table.guest = g
                    table.guest.start()
                    print(f'{g.name_} сел(-а) за стол номер {table.namber}')
                    count += 1
        else:
            while len(gost) > 0:
                g = gost.pop(0)
                self.queue.put(g)
                print(f'{g.name_} в очереди')
    def discuss_guests(self):
        while all(map(lambda table: table.guest != None, self.tables)):
            for table in self.tables:
                if table.guest != None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name_} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.namber} свободен')
                        table.guest = None
                if not self.queue.empty():
                    if table.guest == None:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name_} вышел(-ла) из очереди и сел(-а) за стол номер {table.namber}')
                        table.guest.start()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()