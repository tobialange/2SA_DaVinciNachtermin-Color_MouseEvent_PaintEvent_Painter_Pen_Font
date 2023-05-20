from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowTitle("Nachtermin zur 2. Schulaufgabe")