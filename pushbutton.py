from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Okno programu'
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 250
        self.iconName = 'chest.ico'

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.top, self.left, self.width, self.height)

        #init
        self.UiButtons()
        self.show()


    def UiButtons(self):
        button = QPushButton("Kliknij mnie", self)
        #button.move(50, 50)
        button.setGeometry(QRect(50, 50, 100, 100)) # polozenie x, y, wymiar a, b
        button.setToolTip("to jest podpowiedź") # można doawać takgi <h2> z htmllem
        button.clicked.connect(self.clickme)

    def clickme(self):
        #print("siema")
        sys.exit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = Window()
    sys.exit(App.exec())




