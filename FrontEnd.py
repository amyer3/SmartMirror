import MirrorData as Md
import PyQt5 as P5
import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 500)
    w.move(300, 300)
    w.setWindowTitle('Sample Window for Mirror')
    w.show()

    sys.exit(app.exec_())
