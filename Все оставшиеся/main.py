import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Управления НЛО")
        self.image = QLabel(self)
        self.x = 0
        self.y = 0
        self.image.move(self.x, self.y)
        self.image.resize(60, 35)
        self.pixmap = QPixmap("nlo.png")
        self.image.setPixmap(self.pixmap)
        self.vx = 10
        self.vy = 10
        self.w = 300 - 60
        self.h = 300 - 35

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.move_nlo(0, (-1) * self.vy)
        elif event.key() == Qt.Key_Down:
            self.move_nlo(0, 1 * self.vy)
        elif event.key() == Qt.Key_Left:
            self.move_nlo((-1) * self.vx, 0)
        elif event.key() == Qt.Key_Right:
            self.move_nlo(self.vx, 0)

    def move_nlo(self, vx, vy):
        x = self.x + vx
        y = self.y + vy
        if x > self.w:
            self.x = 0
        elif x < 0:
            self.x = self.w
        else:
            self.x = x
        if y > self.h:
            self.y = 0
        elif y < 0:
            self.y = self.h
        else:
            self.y = y
        self.image.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
