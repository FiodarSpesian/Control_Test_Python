import datetime


class Note(dict):
    creation_day = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")

    def __init__(self):
        super().__init__()
        self.name = input("Enter TITLE of note: ")
        self.event_day = input("Enter EVENT DAY in format dd.mm.yyyy: ")
        self.note_content = input("Enter content of note: ")
        print("Note create successful!")

    def __str__(self):
        return str(self.note)

    def add_note(self):
        dct = {'title': self.name, "event_day": self.event_day,
                     'note_content': self.note_content, 'creation_day': self.creation_day}
        return dct
