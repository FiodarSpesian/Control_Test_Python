from Comands.create_note import CreateNote
from Comands.exit import Exit
from Comands.save import Save
from Comands.show_notes import Show
from notebook import Notebook


class Menu(list):
    commands = []

    def __init__(self):
        super().__init__()
        create_note = CreateNote()
        self.commands.append(create_note)
        show = Show()
        self.commands.append(show)
        save = Save()
        self.commands.append(save)
        finish = Exit()
        self.commands.append(finish)

    def __len__(self):
        return len(self.commands)

    def __iter__(self):
        for i in range(len(self.commands)):
            var = self.commands[i].description

    def __repr__(self):
        return self.commands

    def functions(self):
        for i in range(len(self.commands)):
            print(f"{i+1}. {self.commands[i]}")

    def usr_val(self, chose, notebook):
        return self.commands[chose].action(notebook)
