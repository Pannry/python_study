import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QHBoxLayout, QListView, \
                            QPlainTextEdit, QListWidget, QFormLayout, QWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.janela = Janela()
        self.setCentralWidget(self.janela)

        self.show()

class Janela(QWidget):
    def __init__(self):
        super(Janela, self).__init__()

        self.layout = QFormLayout()
        # self.groupBox = QGroupBox("Receitas:")
        self.layoutInput = QHBoxLayout()

        self.listView = QListView(self)
        self.textEdit = QPlainTextEdit(self)

        self.layoutInput.addWidget(self.listView)
        self.layoutInput.addWidget(self.textEdit)

        self.layout.addRow(self.layoutInput)
        self.setLayout(self.layout)

        # self.groupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())