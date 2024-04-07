
from PySide6.QtGui import QPixmap, QPainter, QRegion, QColor
from PySide6.QtCore import Qt

class ImageChanger:

    def __init__(self, image_path) -> None:
        self.image = image_path

    @property
    def image_path(self):
        return self.__image_path
    
    @image_path.setter
    def image(self, image_path):
        self.__image_path = image_path

    def setCircleImage(self, desired_size):
        orig_pixmap = QPixmap(self.__image_path)
        if not orig_pixmap.isNull():
            scaled_pixmap, sx, sy = self.__calculate_senter(
                orig_pixmap,
                desired_size
            )
            target_pixmap = QPixmap(desired_size, desired_size)
            target_pixmap.fill(Qt.transparent)

            painter = QPainter(target_pixmap)
            painter.setClipRegion(
                self.__createCircleMask(desired_size, 0, 0)
            )
            painter.drawPixmap(0, 0, scaled_pixmap, sx , sy, desired_size, desired_size)
            painter.end()
            return target_pixmap
        return None

    @staticmethod
    def __calculate_senter(orig_pixmap: QPixmap, desired_size):
        min_ = min(orig_pixmap.size().width(), orig_pixmap.size().height())
        if min_ == orig_pixmap.size().width():
            _height = orig_pixmap.size().height() / orig_pixmap.size().width() * desired_size
            scaled_pixmap = orig_pixmap.scaled(desired_size, _height , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = 0
            sy = (orig_pixmap.size().height() - orig_pixmap.size().width()) /2
        else:
            width_ = orig_pixmap.size().width() / orig_pixmap.size().height() * desired_size
            scaled_pixmap = orig_pixmap.scaled(width_, desired_size , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = (orig_pixmap.size().width() - orig_pixmap.size().height()) /2
            sy = 0
        return scaled_pixmap, sx, sy

    @staticmethod
    def __createCircleMask(size, x, y):
        mask = QPixmap(size, size)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        # Центрируем круг внутри области
        painter.setBrush(QColor("black"))
        # Рисуем круг в центре своей области
        painter.drawEllipse(x, y, size, size)
        painter.end()
        region = QRegion(mask.mask())
        return region
