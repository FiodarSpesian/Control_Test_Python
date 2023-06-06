import datetime


class Note:
    creation_day = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")

    def __init__(self):
        self.name = input("Enter TITLE of note: ")
        self.event_day = input("Enter EVENT DAY in format dd.mm.yyyy: ")
        self.note_content = input("Enter content of note: ")
        print("Note create successful!")

    def __repr__(self):
        return self.name + ";" + self.event_day + ";" + self.note_content + ";" + "<" + self.creation_day + ">"
