from Comands.comand import Comand


class Exit(Comand):
    description = "Exit."

    def __init__(self):
        self.flag = True

    def action(self):
        self.flag = False
