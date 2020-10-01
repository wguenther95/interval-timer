import os
import sys

from PyQt5.QtWidgets import QApplication

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.routine import Routine

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Routine()
    ex.show()
    sys.exit(app.exec_())
