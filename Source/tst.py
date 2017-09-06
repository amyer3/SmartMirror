import sys
from threading import Thread
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MirrorData as md
import os
import datetime
import pytz
import time


class Update(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(1)
            wa.label.setText(md.times())


class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        self.label = QLabel(" ")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        Update1 = Update()
        Update1.start()
        Update1.refresh1 = md.times()

        self.label.setText(Update1.refresh1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wa = MyWindow()
    wa.show()
    sys.exit(app.exec_())
