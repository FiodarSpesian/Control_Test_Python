from Comands.comand import Comand
from notebook import Notebook


class Show(Comand):
    description = "Show list of notes."

    def action(self, notebook=None):
        pass
        if notebook is None:
            print("You don't have notes.")
        for el in notebook:
            print(el)
