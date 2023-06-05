from Comands.create_note import CreateNote
from Comands.show_notes import Show
from menu import Menu
from notebook import Notebook
from service import Service
"""
lst = []
create_note = CreateNote()
show = Show()
lst.append(create_note)
lst.append(show)
for i in range(len(lst)):
    print(f"{i+1}. {lst[i]}")
"""

service = Service()
service.start()
#for i in range(len(menu)):
#    print(f"{i + 1}. {menu[i]}")
