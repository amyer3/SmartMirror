import Source.MirrorData as md
#import Source.DataUpdater as du
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        lbl1 = QLabel(md.stocks(), self)
        lbl1.move(10, 10)
        lbl1.setStyleSheet("color: white")

        lbl2 = QLabel(md.weather(), self)
        lbl2.move(10, 40)
        lbl2.setStyleSheet("color: white")

        lbl3 = QLabel(md.times(), self)
        lbl3.move(10, 70)
        lbl3.setStyleSheet("color: white")

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
