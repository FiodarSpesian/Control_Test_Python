import json
from Comands.comand import Comand
from Service.notebook import Notebook


class Save(Comand):

    def __init__(self, description="Save new notes."):
        super().__init__()
        self.description = description

    def action(self, notebook):
        if notebook == Notebook():
            with open('notes.json', 'w') as file:
                json.dump(notebook.push(), file, indent=5)
        else:
            with open('notes.json', 'w') as file:
                json.dump(notebook, file, indent=5)
        print("Save successful.")
