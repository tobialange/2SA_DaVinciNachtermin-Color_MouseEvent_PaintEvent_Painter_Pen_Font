import sys

from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow
# All you need is
# https://doc.qt.io/qtforpython/

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())