from Service.menu import Menu
from Service.notebook import Notebook


class Service:
    def __init__(self, flag=True):
        self.flag = flag
        self.menu = Menu()
        self.notebook = Notebook()

    def start(self):
        while True:
            self.menu.functions()
            usr_in = input("Choose what would you like to do: ")
            try:
                usr_in = int(usr_in)
                if self.menu.usr_val(usr_in - 1, self.notebook) == "exit":
                    print("You have been exit the program! \nBye.")
                    break
                print()
            except ValueError:
                print('\nEntered wrong value.\n')


