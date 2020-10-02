from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit,
                             QScrollArea, QComboBox, QSpacerItem, QSizePolicy)
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


class CycleWidget(QWidget):
    def __init__(self, name):
        super().__init__()

        sets_label = QLabel(name)
        self.sets = QComboBox()
        self.sets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        low_time_label = QLabel("Low")
        self.low_time = QLineEdit('10')

        high_time_label = QLabel("High")
        self.high_time = QLineEdit('60')

        top_layout = QHBoxLayout()
        top_layout.addWidget(sets_label)
        top_layout.addWidget(self.sets)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(low_time_label)
        bottom_layout.addWidget(self.low_time)
        bottom_layout.addWidget(high_time_label)
        bottom_layout.addWidget(self.high_time)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        spacer_item = QSpacerItem(0, 50, QSizePolicy.Expanding, QSizePolicy.Fixed)


class CycleScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()
