from Comands.comand import Comand
from note import Note


class CreateNote(Comand):

    def __init__(self, description="Create note."):
        super().__init__()
        self.description = description
        self.note = None

    def action(self):
        self.note = Note()
        return self.note
