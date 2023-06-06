import menu
from menu import Menu
from notebook import Notebook


class Service:
    def __init__(self, flag=True):
        self.flag = flag
        self.menu = Menu()
        self.notebook = Notebook()

    def start(self):
        while True:
            self.menu.functions()
            print("-------------")
            usr_in = int(input("Choose what would you like to do: "))
            if self.menu.usr_val(usr_in-1, self.notebook) == "exit":
                print("You have been exit the program! \nBye.")
                break
            print(str(self.notebook))
            print()
