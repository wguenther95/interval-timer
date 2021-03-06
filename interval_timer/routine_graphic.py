from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit,
                             QScrollArea, QComboBox, QSpacerItem, QSizePolicy, QStyleOption,
                             QStyle)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from interval_timer.routine import Routine, Cycle
from style.style import css


class RoutineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.routine = Routine()

        routine_label = QLabel("Add Routine")
        routine_label.setAlignment(Qt.AlignCenter)
        save = QPushButton("Save")
        cancel = QPushButton("Cancel")
        add_cycle = QPushButton("Add Cycle")
        add_cycle.clicked.connect(self.add_cycle)
        remove_cycle = QPushButton("Remove Cycle")
        remove_cycle.clicked.connect(self.remove_cycle)

        title_layout = QHBoxLayout()
        title_layout.addWidget(cancel)
        title_layout.addWidget(routine_label)
        title_layout.addWidget(save)

        self.name = QLineEdit("Routine Name")
        self.name.setFixedHeight(25)
        self.name.textChanged.connect(self.update_routine)

        self.cycle_scroll_area = CycleScrollArea()

        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addWidget(self.name)
        main_layout.addWidget(self.cycle_scroll_area)
        main_layout.addWidget(add_cycle)
        main_layout.addWidget(remove_cycle)

        self.setLayout(main_layout)

        self.setFixedSize(400, 600)

    def update_routine(self):
        self.routine.update(self.name.text(), 1, 10, 30)

    def add_cycle(self):
        new_cycle = Cycle()
        self.routine.cycles.append(new_cycle)
        self.cycle_scroll_area.add_cycle()

    def remove_cycle(self):
        if not self.cycle_scroll_area.layout.itemAt((self.cycle_scroll_area.layout.count()) - 1) == None:
            # Delete the CycleWidget from the GUI.
            item = self.cycle_scroll_area.layout.itemAt((self.cycle_scroll_area.layout.count()) - 1).widget()
            item.setParent(None)

            # Delete the corresponding cycle object from the routine.
            del self.routine.cycles[-1]
            print(self.routine.cycles)


class CycleWidget(QWidget):
    def __init__(self, name):
        super().__init__()

        self.cycle = Cycle()

        label = QLabel(name)
        self.sets = QComboBox()
        self.sets.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        sets_label = QLabel("Sets")

        low_time_label = QLabel("Low")
        self.low_time = QLineEdit('10')

        high_time_label = QLabel("High")
        self.high_time = QLineEdit('60')

        top_layout = QHBoxLayout()
        top_layout.addWidget(label)
        top_layout.addStretch(2)
        top_layout.addWidget(self.sets)
        top_layout.addWidget(sets_label)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(low_time_label)
        bottom_layout.addWidget(self.low_time)
        bottom_layout.addWidget(high_time_label)
        bottom_layout.addWidget(self.high_time)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
        self.setFixedHeight(100)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setStyleSheet(css)

    def update_cycle(self):
        self.cycle.update(self.sets.text(), self.low_time.text(), self.high_time.text())

    # In order to set stylesheets on custom widgets, the paintEvent must be overwritten as follows.
    def paintEvent(self, e):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter()
        p.begin(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)


class CycleScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.layout = QVBoxLayout()

        cycle = CycleWidget("Interval Cycle 1")

        self.layout.addWidget(cycle)
        self.layout.setAlignment(Qt.AlignTop)

        widget.setLayout(self.layout)
        widget.setMaximumWidth(self.width())

        self.setWidget(widget)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def add_cycle(self):
        name = 'Interval Cycle ' + str(self.layout.count() + 1)
        cycle = CycleWidget(name)
        self.layout.addWidget(cycle)
