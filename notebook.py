

class Notebook(dict):
    """ Класс Notebook предназначен для сбора в себе заметок (класс Note)"""
    print("It is Notebook.\nYou can (choose something):")

    def __init__(self):
        super().__init__()
        self.notes = {'notes': []}

    def __getitem__(self, key):
        return self.notes[key]

    def __delitem__(self, key):
        del self.notes[key]

    def __setitem__(self, key, value):
        self.notes[key] = value

    def __iter__(self):
        return iter(self.notes)

    def __len__(self):
        return len(self.notes)

    def __str__(self):
        return str(self.notes)

    def push(self):
        return self.notes
