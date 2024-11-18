import threading
import random
from time import sleep

class Bank:
    lock = threading.Lock()
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            rand = random.randint(50, 500)
            self.balance = self.balance + rand
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance = self.balance - rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')