from datetime import datetime

class Note:
    def __init__(self):
        now = datetime.now()
        self.title = input("Entre com o titulo: ")
        self.note = input("Digite a anotação: ")
        self.date = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

class Notebook:

    notes = []

    def addNote(self):
        a = Note()
        self.notes.append(a)

    def showNotes(self):
        for n in self.notes:
            print(n.title)

    def findNote(self, str):
        for n in self.notes:
            if n.title == str:
                print(n.title+", "+n.date)
                print(n.note)

    # def deleteNote(self, str):
    #     for n in self.notes:
    #         if n.title == str:
    #             self.notes.remove()

class Menu:
    def __init__(self):
        self.showMenu()

    def showMenu(self):
        print("\tOpções:"
              "\n\t1 - Criar nota!"
              "\n\t2 - Ver os titulos das notas"
              "\n\t3 - Ver nota especifica")

