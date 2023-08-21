import config
from PySide6.QtCore import (Qt, QEvent, QObject, Signal, Slot)
from PySide6.QtWidgets import QApplication,d
from PySide6.QtUiTools import QUiLoader

import sys

from mainview import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    async_helper = AsyncHelper(main_window, main_window.set_text)

    main_window.show()
    app.exec()
    
    
    ui_file = QFile("mainwindow.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    window.show()