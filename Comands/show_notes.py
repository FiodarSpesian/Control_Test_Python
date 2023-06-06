from Comands.comand import Comand
from notebook import Notebook


class Show(Comand):
    description = "Show list of notes."

    def action(self, notebook=None):
        for el in notebook['notes']:
            print(el)
