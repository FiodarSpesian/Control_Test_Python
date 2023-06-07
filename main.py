from Service.service import Service

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

