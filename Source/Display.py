import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MirrorData as md
import os
import datetime
import pytz


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.tme = QLabel(self.times())
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
        wthr = QLabel(md.weather())
        wthr.setStyleSheet("color: white")
        wthr.setAlignment(Qt.AlignRight)
        wthr.setFont(font)

        # fill Qlabel with a Qobj that has .setTimer()?
        self.tme.setStyleSheet("color: white")
        self.tme.setAlignment(Qt.AlignLeft)
        self.tme.setFont(font)
        self.tme.startTimer(50)

        newscall = md.news()
        act = QLabel(newscall[0])
        act.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        act.setStyleSheet("color: white")
        act.setFont(font)

        jspr = QLabel("Jasper Placeholder")
        jspr.setStyleSheet("color: white")
        jspr.setAlignment(Qt.AlignCenter)
        jspr.setFont(font)

        # xx.addWidget(name, from row, from col, span rows, span cols)
        # Layout:
        #   0   1   2
        # 0 T       W
        # 1     J
        # 2 A   A   A

        layout.addWidget(self.tme, 0, 0)
        layout.addWidget(wthr, 0, 2)
        layout.addWidget(jspr, 1, 1)
        layout.addWidget(act, 2, 0, 1, 3)
        layout.setRowStretch(1, 0)

        self.horizontalGroupBox.setLayout(layout)

    def times(self):
        dtfmt = '%A' + os.linesep + '%B %d, %Y' + os.linesep + '%I:%M:%S %p'
        self.tme.setText(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(dtfmt))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
