import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.timer import TimerObject


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = TimerObject()

        widget = QWidget()

        start = QPushButton("Start")
        start.clicked.connect(self.timer.start)

        pause = QPushButton("Pause")
        pause.clicked.connect(self.timer.pause)

        restart = QPushButton("Restart")
        restart.clicked.connect(self.timer.restart)

        button_layout = QHBoxLayout()
        button_layout.addWidget(start)
        button_layout.addWidget(pause)
        button_layout.addWidget(restart)

        layout = QVBoxLayout()
        layout.addWidget(self.timer)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestWidget()
    sys.exit(app.exec_())
