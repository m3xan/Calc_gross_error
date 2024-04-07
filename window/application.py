
from PySide6.QtWidgets import QApplication

from functions.loger import Logger

class QApplicationWithLogging(QApplication):
    """
    start QApplication and Logger
    """
    def __init__(self, argv):
        super().__init__(argv)
        self._logger = Logger()
        self._logger.start_logger()
