from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class GridScene(QGraphicsScene):
    """QGraphicsScene overwritten to draw a grid in the background for the notes"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_size = 50
        self.grid_height = 12

        self.setSceneRect(
            0,
            0,          # begin coordinates
            2000,       # width
            self.grid_size * self.grid_height # height
        )

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        left = int(rect.left()) - (int(rect.left()) % self.grid_size)
        top = int(rect.top()) - (int(rect.top()) % self.grid_size)
        bottom = (self.grid_size * (self.grid_height))

        lines = []

        x = left
        while x < rect.right():
            lines.append(QLineF(x, rect.top(), x, bottom))
            x += self.grid_size

        y = top

        while y < bottom + self.grid_size:
            lines.append(QLineF(rect.left(), y, rect.right(), y))
            y += self.grid_size

        painter.setPen(QPen(QColor(200, 200, 200), 0))
        painter.drawLines(lines)