from menu import Menu
from notebook import Notebook


class Service:
    notebook = Notebook()

    def __init__(self):
        self.menu = Menu()

    def start(self):
        flag = True
        while flag:
            self.menu.print()
            print("--------")
            chose = int(input("Choose what would you like to do: "))
            print(chose)
