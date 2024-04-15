
from PySide6.QtWidgets import QMessageBox

class ErroWindow(QMessageBox):
    def __init__(self) -> None:
        super().__init__()
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle("Error")

    def set_message(self, message: str):
        if isinstance(message, str):
            self.setText(message)

    def file_not_faund(self):
        self.set_message(
            'Critical file not found'
        )
