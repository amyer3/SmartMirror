import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MirrorData as md


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.gridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.showFullScreen()

    def gridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        font = QFont("times", 30)

        # white text = xx.setStyleSheet("color: white")
        # white backgrd = xx.setStyleSheet("background: white")
        wthr = QLabel(md.weather(), self)
        wthr.setStyleSheet("color: white")
        wthr.setAlignment(Qt.AlignRight)
        wthr.setFont(font)

        tme = QLabel(md.times(), self)
        tme.setStyleSheet("color: white")
        tme.setAlignment(Qt.AlignLeft)
        tme.setFont(font)

        newscall = md.news()
        act = QLabel(newscall[2], self)
        act.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        act.setStyleSheet("color: white")
        act.setFont(font)

        jspr = QLabel("Jasper Placeholder", self)
        jspr.setStyleSheet("color: white")
        jspr.setAlignment(Qt.AlignCenter)
        jspr.setFont(font)

        # xx.addWidget(name, from row, from col, span rows, span cols)
        #Layout
        #  0   1   2
        #0 T       W
        #1     J
        #2 A   A   A
        layout.addWidget(tme, 0, 0)
        layout.addWidget(wthr, 0, 2)
        layout.addWidget(jspr, 1, 1)
        layout.addWidget(act, 2, 0, 1, 3)
        layout.setRowStretch(1, 0)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
