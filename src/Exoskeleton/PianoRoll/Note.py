from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Note(QGraphicsRectItem):
    GRID_SIZE = 50
    MIN_WIDTH = GRID_SIZE
    RESIZE_MARGIN = 10

    def __init__(self):
        super().__init__(0, 0, 100, self.GRID_SIZE)

        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)

        self.setBrush(QBrush(QColor("red")))
        self.resizing = False


    def hoverMoveEvent(self, event):

        if abs(event.pos().x() - self.rect().width()) < self.RESIZE_MARGIN:
            self.setCursor(Qt.CursorShape.SplitHCursor)
        else:
            self.unsetCursor()


    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.RightButton:
            self.scene().removeItem(self)
            del self
            return

        # Check if the mouse is near the right edge
        if abs(event.pos().x() - self.rect().width()) < self.RESIZE_MARGIN:
            self.resizing = True
            event.accept()
            return

        super().mousePressEvent(event)


    def mouseMoveEvent(self, event):

        if self.resizing:
            width = event.pos().x()

            # Snap width to grid
            width = round(width / self.GRID_SIZE) * self.GRID_SIZE

            # Enforce minimum width
            width = max(self.MIN_WIDTH, width)

            self.setRect(
                0,
                0,
                width,
                self.GRID_SIZE
            )

            event.accept()
            return

        super().mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        self.resizing = False
        super().mouseReleaseEvent(event)


    def itemChange(self, change, value):

        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            x = round(value.x() / self.GRID_SIZE) * self.GRID_SIZE
            y = round(value.y() / self.GRID_SIZE) * self.GRID_SIZE

            # Prevent going beyond left boundary
            x = max(0, x)

            # Prevent going beyond top/bottom boundaries
            #TODO: check actual grid parameters isntead of hardcoded oens
            max_y = self.GRID_SIZE * 12 - self.rect().height()
            y = max(0, min(y, max_y))

            return QPointF(x, y)

        return super().itemChange(change, value)
