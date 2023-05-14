# 1.
```python
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        ## Изображение
        self.pixmap = QPixmap('orig.jpg')
        # Если картинки нет, то QPixmap будет пустым, 
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
```
# 2.
```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.run)

    def run(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя", 
                                                "Как тебя зовут?")
        if ok_pressed:
            self.button_1.setText(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
```
# 3.
```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QColorDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.run)

    def run(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_1.setStyleSheet(
                "background-color: {}".format(color.name()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
```
# 4.
```python
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(70, 150)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(0, 0, 255))
        qp.drawRect(30, 90, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
```
# 5.
```python
import sys
from math import cos, pi, sin

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов
SIDE_LENGTH = 200
SIDES_COUNT = 5


class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем звезду')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_star(qp)
        qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_star(self, qp):

        # Считаем координаты и переводим их в экранные
        nodes = [(SIDE_LENGTH * cos(i * 2 * pi / SIDES_COUNT),
                  SIDE_LENGTH * sin(i * 2 * pi / SIDES_COUNT))
                 for i in range(SIDES_COUNT)]
        nodes2 = [(int(self.xs(node[0])),
                   int(self.ys(node[1]))) for node in nodes]

        # Рисуем пятиугольник
        for i in range(-1, len(nodes2) - 1):
            qp.drawLine(*nodes2[i], *nodes2[i + 1])

        # Изменяем цвет линии
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)

        # Рисуем звезду
        for i in range(-2, len(nodes2) - 2):
            qp.drawLine(*nodes2[i], *nodes2[i + 2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
```