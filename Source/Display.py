# import Source.DataUpdater as du
# import Source.DataUpdater as du
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Source.MirrorData as md


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        font = QFont("times", 50)

        lbl1 = QLabel(md.stocks(), self)
        lbl1.move(10, 10)
        lbl1.setStyleSheet("color: white")
        lbl1.setFont(font)

        lbl2 = QLabel(md.weather(), self)
        lbl2.move(10, 50)
        lbl2.setStyleSheet("color: white")
        lbl2.setFont(font)

        lbl3 = QLabel(md.times(), self)
        lbl3.move(10, 90)
        lbl3.setStyleSheet("color: white")
        lbl3.setFont(font)

        tmln = QLabel(md.forecast(), self)
        tmln.move(10, 130)
        tmln.setStyleSheet("color: white")
        tmln.setFont(font)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
