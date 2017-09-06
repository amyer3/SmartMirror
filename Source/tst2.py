import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MirrorData as md
import time
from threading import Thread


class MainWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        layout = QGridLayout()
        self.setLayout(layout)
        font = QFont("times", 30)

        # white text = xx.setStyleSheet("color: white")
        # white backgrd = xx.setStyleSheet("background: white")
        self.wthr = QLabel("graph here")
        self.wthr.setStyleSheet("color: white")
        self.wthr.setAlignment(Qt.AlignRight)
        self.wthr.setFont(font)

        # fill Qlabel with a Qobj that has .setTimer()?

        self.tme = QLabel(" ")
        self.tme.setStyleSheet("color: white")
        self.tme.setAlignment(Qt.AlignLeft)
        self.tme.setFont(font)

        newscall = md.news()
        self.act = QLabel(" ")
        self.act.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.act.setStyleSheet("color: white")
        self.act.setFont(font)

        self.jspr = QLabel("Jasper Placeholder")
        self.jspr.setStyleSheet("color: white")
        self.jspr.setAlignment(Qt.AlignCenter)
        self.jspr.setFont(font)

        # xx.addWidget(name, from row, from col, span rows, span cols)
        # Layout:
        #   0   1   2
        # 0 T       W
        # 1     J
        # 2 A   A   A

        layout.addWidget(self.tme, 0, 0)
        layout.addWidget(self.wthr, 0, 2)
        layout.addWidget(self.jspr, 1, 1)
        layout.addWidget(self.act, 2, 0, 1, 3)
        layout.setRowStretch(1, 0)

        updateTime = UpdateTime()
        updateTime.start()
        updateTime.refreshT = md.times()

        updateNews = UpdateNews()
        updateNews.start()
        updateNews.refreshN = newscall[0]

        self.tme.setText(updateTime.refreshT)


class UpdateTime(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(1)
            ex.tme.setText(md.times())


class UpdateNews(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            headlines = md.news()
            for i in range(headlines.__len__()):  # TypeError: 'int' object is not iterable
                if i > headlines.__len__() - 1:
                    ex.act.setText(headlines[i])
                    time.sleep(10)
                else:
                    self.run()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec_())
