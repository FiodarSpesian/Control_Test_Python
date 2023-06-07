from Comands.comand import Comand
from Comands.save import Save
from Service.note import Note


class CreateNote(Comand):

    def __init__(self, description="Create note."):
        super().__init__()
        self.description = description
        self.note = None

    def action(self, notebook):
        save = Save()
        self.note = Note()
        notebook['notes'].append(self.note.add_note())
        save.action(notebook)
