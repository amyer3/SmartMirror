import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MirrorData as md
import time
from threading import Thread
import os
from PyQt5.QtSvg import *


class MainWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        layout = QGridLayout()
        self.setLayout(layout)
        majorText = QFont("arial unicode ms", 47)

        self.wthr = QLabel(" ")
        self.wthr.setStyleSheet("color: white")
        self.wthr.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.wthr.setFont(majorText)

        self.tme = QLabel(" ")
        self.tme.setStyleSheet("color: white")
        self.tme.setAlignment(Qt.AlignLeft)
        self.tme.setFont(majorText)

        newscall = md.news()
        self.act = QLabel(" ")
        self.act.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.act.setStyleSheet("color: white")
        self.act.setFont(majorText)

        self.jspr = QLabel("!")
        self.jspr.setStyleSheet("color: white")
        self.jspr.setAlignment(Qt.AlignCenter)
        self.jspr.setFont(majorText)

        self.pic = QLabel()
        self.pic.setAlignment(Qt.AlignLeft | Qt.AlignCenter)

        # xx.addWidget(name, from row, from col, span rows, span cols)
        # Layout:
        #   0   1   2   3
        # 0 T       P   W
        # 1 J   J   J   J
        # 2 J   J   J   J
        # 3 A   A   A   A

        layout.addWidget(self.tme, 0, 0)
        layout.addWidget(self.wthr, 0, 2, 1, 2)
        layout.addWidget(self.jspr, 1, 0, 2, 4)
        layout.addWidget(self.act, 3, 0, 1, 4)
        layout.addWidget(self.pic, 0, 2, 1, 2)
        layout.setRowStretch(1, 0)

        updateTime = UpdateTime()
        updateTime.start()
        updateTime.refreshT = md.times()

        updateNews = UpdateNews()
        updateNews.start()
        updateNews.refreshN = newscall[0]

        updateWthr = UpdateWeather()
        updateWthr.start()


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
            for i in range(headlines.__len__()):
                if i < headlines.__len__() - 1:
                    ex.act.setText(headlines[i])
                    time.sleep(10)
                else:
                    self.run()


class UpdateWeather(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        # data = (high, lo, cond(url), day)
        upArrow = u"\u25B4"
        dwnArrow = u"\u25BE"
        tup = md.weather()
        ex.wthr.setText("San Francisco, CA" + os.linesep + upArrow + " " + tup[0][0] + " | " + dwnArrow + " " + tup[1][0])
        pixmap = QPixmap()
        pixmap.load(md.svgSelector())
        ex.pic.setPixmap(pixmap.scaled(100, 100))
        time.sleep(14400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec_())
