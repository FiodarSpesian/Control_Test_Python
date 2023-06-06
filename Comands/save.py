import json
from Comands.comand import Comand


class Save(Comand):

    def __init__(self, description="Save notes."):
        super().__init__()
        self.description = description

    def action(self, notebook):
        with open('notes.json', 'w') as file:
            json.dump(notebook.push(), file, indent=3)
        print("Save successful.")
