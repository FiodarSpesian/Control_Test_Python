from menu import Menu
from notebook import Notebook


class Service:
    notebook = Notebook()

    def __init__(self):
        self.menu = Menu()

    def start(self):
        flag = True
        while flag:
            print(len(self.menu))
            self.menu.functions()
            print("--------")
            chose = int(input("Choose what would you like to do: "))
            print(chose)
            """
            for i in range(len(self.menu)):
                if chose == self.menu[i]:
                    self.menu[i].action()
            """