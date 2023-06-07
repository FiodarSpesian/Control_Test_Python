import json
from Comands.comand import Comand


class Show(Comand):
    description = "Show list of notes."

    def action(self, notebook=None):
        with open('notes.json', 'r') as file:
            data = json.load(file)
        for i in range(len(data['notes'])):
            print(f"{i+1}."
                  f"title: {data['notes'][i]['title']}"
                  f"\n  event_day: {data['notes'][i]['event_day']}"
                  f"\n  note_content: {data['notes'][i]['note_content']}"
                  f"\n  creation_day: <{data['notes'][i]['creation_day']}>")
