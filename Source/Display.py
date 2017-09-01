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
        font = QFont("times", 50)

        wthr = QLabel(md.weather(), self)
        wthr.setAlignment(Qt.AlignRight)
        wthr.setStyleSheet("color: white")
        #lbl2.setStyleSheet("background: white")
        wthr.setFont(font)

        tme = QLabel(md.times(), self)
        tme.setAlignment(Qt.AlignLeft)
        tme.setStyleSheet("color: white")
        #lbl3.setStyleSheet("background: white")
        tme.setFont(font)

        hbox = QHBoxLayout()
        hbox.addWidget(tme)
        hbox.addWidget(wthr)
        self.setLayout(hbox)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
