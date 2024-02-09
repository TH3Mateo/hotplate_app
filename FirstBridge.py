from PySide6.QtCore import QObject
from Graph import MatplotlibImageProvider


class FirstScreenBridge(QObject):
    def __init__(self):
        super().__init__()
        self.imageProvider = MatplotlibImageProvider()
        figure = self.imageProvider.addFigure("eventStatisticsPlot", figsize=(10, 10))
        self.graph = figure.add_subplot(111)
