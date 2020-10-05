import os
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.routine_graphic import RoutineWidget

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutineWidget()
    ex.show()
    sys.exit(app.exec_())
