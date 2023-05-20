import math

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPaintEvent, QPainter, QColor, QBrush, QMoveEvent, QPen, QPixmap, QFont, QResizeEvent
from PyQt6.QtWidgets import QWidget


class DaVinci(QWidget):
    def __init__(self, parent=None):
        super(DaVinci, self).__init__(parent)

        self.__w = 800
        self.__h = 500

    def calc_radius(self):
        min = self.__h

        if min > self.__w:
            min = self.__w

        self.__radius = int(min / 2) - 2 * 25

    def sizeHint(self) -> QSize:
        return QSize(self.__w, self.__h)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super(DaVinci, self).resizeEvent(a0)

        self.__w = a0.size().width()
        self.__h = a0.size().height()

        self.calc_radius()

    def moveEvent(self, a0: QMoveEvent) -> None:
        super(DaVinci, self).moveEvent(a0)

        #if a0.type().name == Qt.MouseButton.RightButton:
        self.update()

    def paintEvent(self, a0: QPaintEvent) -> None:
        super(DaVinci, self).paintEvent(a0)

        painter = QPainter(self)

        pen = QPen()
        pen.setColor(QColor("lightslategray"))
        pen.setWidth(10)
        painter.setPen(pen)

        font = QFont("OldEnglish", 24)
        painter.setFont(font)

        painter.fillRect(0, 0, self.width(), self.height(), QColor("lightgoldenrodyellow"))

        painter.drawEllipse(int(self.__w / 2) - self.__radius, int(self.__h / 2) - self.__radius, 2 * self.__radius, 2 * self.__radius)

        length = int(2 * self.__radius / 2 ** 0.5)
        x = int(self.__w / 2) - int(self.__radius / 2 ** 0.5)
        y = int(self.__h / 2) - int(self.__radius / 2 ** 0.5)
        painter.drawRect(x, y, length, length)

        pixmap_mensch = QPixmap("strichmensch.jpg").scaledToWidth(length)
        painter.drawPixmap(x, y, pixmap_mensch)

        text = "Vitruvianischer Mensch"
        bounding_rect = painter.boundingRect(0, 0, self.width(), self.height(), 0, text)
        painter.drawText(self.__w - bounding_rect.width(), bounding_rect.height(), text)
        offset = bounding_rect.height()

        font = QFont("OldEnglish", 12)
        painter.setFont(font)

        text = "Leonardo da Vinci"
        bounding_rect = painter.boundingRect(0, 0, self.width(), self.height(), 0, text)
        painter.drawText(self.__w - bounding_rect.width(), offset + bounding_rect.height(), text)
