
from PySide6.QtWidgets import QApplication

from global_param import ECHO

from functions.loger import Logger

class QApplicationWithLogging(QApplication):
    """
    start QApplication and Logger
    """
    def __init__(self, argv):
        super().__init__(argv)
        self._logger = Logger(echo= ECHO)
        self._logger.start_logger()
