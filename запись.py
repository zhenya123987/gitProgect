import sys
import random

from PyQt5.QtGui import QPainter, QColor

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.button_1 = QPushButton(self)
        self.button_1.move(10, 10)
        self.button_1.clicked.connect(self.start)

    def start(self):
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self. qp.begin(self)
        self.draw_circle()
        self.qp.end()

    def draw_circle(self):
        x, y, r = random.randint(1, 500), random.randint(1, 500), random.randint(10, 200)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())  # 3 commit 4 5 6
