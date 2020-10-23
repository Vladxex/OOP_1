LOP = []
class Person:
    def __init__(self, FIO, balance):
        self.FIO = FIO
        self.balance = balance
    def getInfo(self):
        return self.FIO, self.balance


def recurs():
    x = int(input("Нажмите 1, если хотите добавить клиента в базу, нажмите 2, если хотите вывести информацию о клиенте"))
    if x==1:
        y = Person(str(input('Введите Имя Фамилию:')), input('Введите баланс:'))
        LOP.append(y)
        recurs()
    elif x==2:
        z = str(input('Введите Имя Фамилию'))
        for i in range(len(LOP)):
            if z == LOP[i].getInfo()[0]:
                print("Клиент «{}». Баланс: {} руб.".format(LOP[i].getInfo()[0], LOP[i].getInfo()[1]))
        recurs()
    else:
        return "Helo"

recurs()
