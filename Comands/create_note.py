from Comands.comand import Comand
from note import Note


class CreateNote(Comand):
    description = "Create note."

    note = None

    def action(self):
        self.note = Note()

