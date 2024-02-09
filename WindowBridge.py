# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial

import sys
import time
from pathlib import Path

from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtQml import QQmlApplicationEngine, QmlElement, qmlRegisterType, QQmlComponent
import threading as th
import time as t

import MainBridge

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class WindowBridge(QObject):
    view_changed = Signal()

    def __init__(self):

        super().__init__()
        self._view = "main"
        self.xd = "first"

        self.start_sequence()

    def xd(self, val=None):
        if val is None:
            return self._xd
        else:
            self._xd = val
            self.view_changed.emit()

    xd = Property(str, fget=xd, fset=xd, notify=view_changed)

    def start_sequence(self):
        th.Thread(target=self.change_view).start()

    #
    def change_view(self):
        # while True:
        t.sleep(1)

        self.xd = "second" if self.xd == "first" else "first"
        self.view1 = MainBridge.MainBridge()
