import json

from Comands.create_note import CreateNote
from Comands.show_notes import Show
from menu import Menu
from note import Note
from notebook import Notebook
from service import Service

"""
notebook = Notebook()
print(type(notebook))
print(notebook)
print(dict(notebook))
print(type(notebook))
"""

service = Service()
service.start()

#with open('notes.json', 'w') as file:
 #   json.dump(notebook.push(), file, indent=3)

