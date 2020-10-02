from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.routine import Routine, Cycle


class RoutineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.routine = Routine()

        routine_label = QLabel("Add Routine")
        routine_label.setAlignment(Qt.AlignCenter)
        save = QPushButton("Save")
        cancel = QPushButton("Cancel")

        title_layout = QHBoxLayout()
        title_layout.addWidget(cancel)
        title_layout.addWidget(routine_label)
        title_layout.addWidget(save)

        self.name = QLineEdit("Routine Name")
        self.name.textChanged.connect(self.update_routine)

        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addWidget(self.name)

        self.setLayout(main_layout)

        self.setFixedSize(400, 600)

    def update_routine(self):
        self.routine.update(self.name.text(), 1, 10, 30)
        print(self.routine.name)
