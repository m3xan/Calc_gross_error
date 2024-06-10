"""
заглушка
"""
from PySide6.QtWidgets import QMessageBox

from functions import logger

class ErroWindow(QMessageBox):
    """
    заглушка
    """
    def __init__(self) -> None:
        super().__init__()
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Error")

    @logger.info
    def set_message(self, message: str):
        """
        заглушка
        """
        if isinstance(message, str):
            self.setText(message)
        return message
