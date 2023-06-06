from menu import Menu
from notebook import Notebook


class Service:
    def __init__(self):
        self.menu = Menu()
        self.notebook = Notebook()

    def start(self):
        flag = True
        while flag:
            print(len(self.menu))
            self.menu.functions()
            print("--------")
            usr_in = int(input("Choose what would you like to do: "))
            self.menu.usr_val(usr_in-1, self.notebook)
            print()
