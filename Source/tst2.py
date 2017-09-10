import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MirrorData as md
import time
from threading import Thread
import os


class MainWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        layout = QGridLayout()
        self.setLayout(layout)
        majorText = QFont("times", 50)

        # white text = xx.setStyleSheet("color: white")
        # white backgrd = xx.setStyleSheet("background: white")
        pixmap = QPixmap()
        pixmap.load("icons/overcast.svg")

        self.wthr = QLabel(" ")
        self.wthr.setStyleSheet("color: white")
        self.wthr.setAlignment(Qt.AlignRight | Qt.AlignCenter)
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

        self.forecst = QLabel(" ")
        self.forecst.setStyleSheet("color: white")
        self.forecst.setFont(majorText)
        self.forecst.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.pic = QLabel()
        self.pic.setPixmap(pixmap.scaled(150, 150))
        self.pic.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        # xx.addWidget(name, from row, from col, span rows, span cols)
        # Layout:
        #   0   1   2   3
        # 0 T       P   W
        # 1 J   J   J   J
        # 2 J   J   J   J
        # 3 A   A   A   A

        layout.addWidget(self.tme, 0, 0)
        layout.addWidget(self.wthr, 0, 3)
        layout.addWidget(self.jspr, 1, 0, 2, 4)
        layout.addWidget(self.act, 3, 0, 1, 4)
        layout.addWidget(self.pic, 0, 2)
        layout.setRowStretch(1, 0)

        updateTime = UpdateTime()
        updateTime.start()
        updateTime.refreshT = md.times()

        updateNews = UpdateNews()
        updateNews.start()
        updateNews.refreshN = newscall[0]

        updateFcst = UpdateForecast()
        updateFcst.start()


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


class UpdateForecast(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        # data = (high, lo, cond(url), day)
        arr = md.strFormatter()
        tup = md.weather()
        ex.wthr.setText("San Francisco, CA" + os.linesep + tup[0][0]+" | "+tup[1][0])
        ex.forecst.setText(arr[0]+os.linesep+arr[1]+os.linesep+arr[2]+os.linesep+arr[3])
        time.sleep(14400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec_())
