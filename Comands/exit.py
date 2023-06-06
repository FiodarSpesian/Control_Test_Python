from Comands.comand import Comand


class Exit(Comand):
    description = "Exit."

    def action(self, notebook):
        return "exit"
