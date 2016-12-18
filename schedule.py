# DYNAMIC coded by Mr. Tang
# Create your classes here

import sys
from PySide import QtGui, QtCore


class Calendar(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(0, 60, 500, 540)
        self.initUI()

    def initUI(self):
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.connect(self.cal, QtCore.SIGNAL('selectionChanged()'),self.showDate)
        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy/MM/dd"))  # str(date.toPyDate())
        self.label.move(130, 260)
        self.cal.setGeometry(10, 80, 350, 300)
        self.update()

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(date.toString("yyyy/MM/dd"))

