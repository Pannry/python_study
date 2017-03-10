import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QGroupBox, QDialog, \
                            QVBoxLayout, QListView, QPlainTextEdit, QAction


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

        self.statusBar().showMessage('')

        self.createHorizontalLayout()
        self.createMenu()

        # TODO Corrigir o layout do programa, para aparecer as duas janelas
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.groupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.groupBox = QGroupBox("Receitas:")
        layout = QHBoxLayout()

        listView = QListView(self)
        layout.addWidget(listView)

        textEdit = QPlainTextEdit(self)
        layout.addWidget(textEdit)

        self.groupBox.setLayout(layout)

    def createMenu(self):

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Menu')
        # aboutMenu = mainMenu.addMenu('Sobre')

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Sair do Programa')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())