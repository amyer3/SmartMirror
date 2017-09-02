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
        font = QFont("times", 30)

        wthr = QLabel(md.weather(), self)
        wthr.setStyleSheet("color: white")
        wthr.setAlignment(Qt.AlignRight)
        wthr.setStyleSheet("background: white")
        wthr.setFont(font)

        tme = QLabel(md.times(), self)
        tme.setStyleSheet("color: white")
        tme.setAlignment(Qt.AlignLeft)
        tme.setStyleSheet("background: white")
        tme.setFont(font)

        newscall = md.news()
        act = QLabel(newscall[2], self)
        act.setAlignment(Qt.AlignBaseline)
        act.setStyleSheet("color: white")
        act.setStyleSheet("background: white")
        act.setFont(font)

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(tme, 0, 0)
        self.gridLayout.addWidget(act, 1, 0)
        self.gridLayout.addWidget(wthr, 0, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(0, 0)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 0)
        self.setLayout(self.gridLayout)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
