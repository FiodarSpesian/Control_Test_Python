import datetime


class Note:
    creation_day = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")

    def __init__(self):
        self.event_day = input("Enter day of event in format dd mm yyyy: ")
        self.name = input("Enter name of note: ")
        self.note_content = input("Enter content of note: ")
        print("Note create successful!")

    def __repr__(self):
        return self.name
        #return f"Date of creation:<{self.creation_day}> {self.name}; {self.note_content}; {self.event_day}"
