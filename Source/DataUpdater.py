import MirrorData as md
from PyQt5.QtCore import *


class Timer:
    def __init__(self, time):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(time)
        self.timer.start()
        self.timer.connect(md.times())
