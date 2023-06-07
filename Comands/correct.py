import json
from Comands.comand import Comand
from Comands.save import Save
from Comands.show_notes import Show


class Correct(Comand):
    description = "Correct note."

    def action(self, notebook):
        show = Show()
        save = Save()
        with open('notes.json', 'r') as file:
            data = json.load(file)
        show.action(data)
        el_choice = int(input('Choose which note one you would like to CORRECT: '))
        el = data['notes'][el_choice - 1]
        lst = list(el.keys())
        for i in range(len(lst)):
            print(f'{i+1}. {lst[i]}')
        field = int(input(f'Choose which field would you like to correct: '))
        el[lst[field-1]] = input('Enter changes: ')
        save.action(data)
