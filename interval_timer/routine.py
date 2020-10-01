from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

from enum import Enum


class Type(Enum):
    SINGLE: 0
    COMPLEX: 1


class State(Enum):
    LOW: 0
    HIGH: 1
    REST: 2


class Routine(QWidget):
    def __init__(self):
        super().__init__()

        routine_label = QLabel("Add Routine")
        routine_label.setAlignment(Qt.AlignCenter)
        save = QPushButton("Save")
        cancel = QPushButton("Cancel")

        title_layout = QHBoxLayout()
        title_layout.addWidget(cancel)
        title_layout.addWidget(routine_label)
        title_layout.addWidget(save)

        name = QLineEdit("Routine Name")

        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addWidget(name)

        self.setLayout(main_layout)

        self.setFixedSize(400, 600)
