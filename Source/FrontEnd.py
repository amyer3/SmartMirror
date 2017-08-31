import Source.MirrorData as md
import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        lbl1 = QLabel(md.stocks(), self)
        lbl1.move(10, 10)

        lbl2 = QLabel(md.weather(), self)
        lbl2.move(10, 40)

        lbl3 = QLabel(md.times(), self)
        lbl3.move(10, 70)

        self.setGeometry(30, 100, 300, 100)
        self.setWindowTitle('Absolute')
        self.show()

    def clockTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
