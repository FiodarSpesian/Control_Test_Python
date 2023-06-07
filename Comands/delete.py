import json
from Comands.comand import Comand
from Comands.save import Save
from Comands.show_notes import Show


class Delete(Comand):

    def __init__(self, description="Delete note."):
        super().__init__()
        self.description = description

    def action(self, notebook=None):
        show = Show()
        save = Save()
        with open('notes.json', 'r') as file:
            data = json.load(file)
        show.action(data)
        del_choice = int(input('Choose which one you would like to DELETE: '))
        var = data['notes'].pop(del_choice-1)
        print(f"deleted note: {var}")
        save.action(data)
        return notebook

