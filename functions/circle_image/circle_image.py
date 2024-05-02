
from typing import overload

from PySide6.QtGui import QPixmap, QPainter, QRegion, QColor
from PySide6.QtCore import Qt

from functions.circle_image.image import Image

class ImageChanger:
    __image_path = None

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, image_path: str) -> None: ...
    @overload
    def __init__(self, image_path: Image) -> None: ...
    @overload
    def set_image(self, image_path: str) -> bool: ...
    @overload
    def set_image(self, image_path: Image) -> bool: ...

    def __init__(self, image_path = None) -> None:
        if image_path is not  None:
            self.set_image(image_path)

    def get_image_path(self):
        return self.__image_path

    def set_image(self, image_path):
        if isinstance(image_path, str):
            image = Image()
            if image.set_image_path(image_path):
                self.__image_path = image_path
                return True
        if isinstance(image_path, Image):
            if (image := image_path.get_image_path()) is not None:
                self.__image_path = image
                return True
        return False

    def circle_image(self, desired_size: float | int):
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
                self.__createcirclemask(desired_size, 0, 0)
            )
            painter.drawPixmap(0, 0, scaled_pixmap, sx , sy, desired_size, desired_size)
            painter.end()
            return target_pixmap
        return None

    @staticmethod
    def __calculate_senter(orig_pixmap: QPixmap, desired_size: float | int):
        min_ = min(orig_pixmap.size().width(), orig_pixmap.size().height())
        if min_ == orig_pixmap.size().width():
            _height = orig_pixmap.size().height() / orig_pixmap.size().width() * desired_size
            scaled_pixmap = orig_pixmap.scaled(desired_size, _height , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = 0
            sy = (scaled_pixmap.size().height() - scaled_pixmap.size().width()) /2
        else:
            width_ = orig_pixmap.size().width() / orig_pixmap.size().height() * desired_size
            scaled_pixmap = orig_pixmap.scaled(width_, desired_size , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = (scaled_pixmap.size().width() - scaled_pixmap.size().height()) /2
            sy = 0
        return scaled_pixmap, sx, sy

    @staticmethod
    def __createcirclemask(size: int, x: int, y: int) -> QRegion:
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
