
from PySide6.QtGui import QPixmap, QPainter, QRegion, QColor
from PySide6.QtCore import Qt

def createCircleMask(size, x, y):
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

def setCircleImage(image_path, desired_size):
    orig_pixmap = QPixmap(image_path)
    if not orig_pixmap.isNull():
        min_ = min(orig_pixmap.size().width(), orig_pixmap.size().height())
        if min_ == orig_pixmap.size().width():
            c = orig_pixmap.size().height() / orig_pixmap.size().width() * desired_size
            orig_pixmap = orig_pixmap.scaled(desired_size, c , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = 0
            sy = (orig_pixmap.size().height() - orig_pixmap.size().width()) /2
        else:
            c = orig_pixmap.size().width() / orig_pixmap.size().height() * desired_size
            orig_pixmap = orig_pixmap.scaled(c, desired_size , Qt.KeepAspectRatio, Qt.SmoothTransformation)
            sx = (orig_pixmap.size().width() - orig_pixmap.size().height()) /2
            sy = 0

        target_pixmap = QPixmap(desired_size, desired_size)
        target_pixmap.fill(Qt.transparent)

        painter = QPainter(target_pixmap)
        reg  = createCircleMask(desired_size, 0, 0)

        painter.setClipRegion(reg)

        painter.drawPixmap(0, 0, orig_pixmap, sx , sy, desired_size, desired_size)
        painter.end()
        return target_pixmap
    return None
