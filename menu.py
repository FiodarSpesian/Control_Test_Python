from Comands.create_note import CreateNote
from Comands.exit import Exit
from Comands.show_notes import Show


class Menu(list):
    commands = []

    def __init__(self):
        super().__init__()
        create_note = CreateNote()
        self.commands.append(create_note)
        show = Show()
        self.commands.append(show)
        finish = Exit()
        self.commands.append(finish)

    def __len__(self):
        return len(self.commands)

    def print(self):
        for i in range(len(self.commands)):
            print(f"{i+1}. {self.commands[i]}")

