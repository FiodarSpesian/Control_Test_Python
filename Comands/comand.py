from Service.notebook import Notebook


class Comand:
    description = ""
    notebook = Notebook()

    def __repr__(self):
        return self.description

    def action(self, notebook):
        self.notebook = notebook






