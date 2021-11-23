import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication

SIZE_SCREEN = [random.randrange(100, 1000), random.randrange(100, 1000)]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUI("UI.ui", self)
        self.p = True
        self.pushButton.clicked.connect(self.update())

    def paintEvent(self):
        if self.p:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()
        self.p = False

    def draw(self):
        r = random.randrange(20, 50)
        self.qp.drawEllipse(self.x - r // 2, self.y - r // 2, r, r)
        self.qp.setPen(QColor(255, 255, 0))
        self.p = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
