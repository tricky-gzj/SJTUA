#-*- coding:utf-8 -*-
# DYNAMIC coded by Mr. Tang
# Create your classes here

import sys
from PySide import QtGui, QtCore
from clist import *
affairList = []

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


class Affair:
    def __init__(self, pid = 0, name = "lazy"):
        self.pid = pid
        self.name = name

    def getIcon(self):
        iconid = int(self.pid) % 4
        return './head/' + str(iconid) + '.png'

class AffairDB:
    def __init__(self):
        self.db = "affairs.db"
        self.affairList = []
        self.readAffair()

    def readAffair(self):
        self.affairList = []
        datas_ = (
            (u'张三', '10001'),
            ('C#\n----\n456', '10002'),
            ('Lisp\n123', '10003'),
            ('Objective-C', '10004'),
            ('Perl', '10005'),
            ('Ruby', '10006'),
        )

        for i in datas_:
            name, pid = i[0], i[1]
            affair = Affair(pid, name)
            affairList.append(affair)

    def searchAffair(self,tags):
        self.affairList = []

class AffairList(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(400, 60, 600, 540)

        self.item_box = ItemBox()
        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(0, 0, 600, 540)
        self.list_view.setSpacing(3)

        self.list_model = ListModel(self.item_box)
        self.list_view.setModel(self.list_model)
        self.list_view.setIconSize(QtCore.QSize(50, 50))

        self.db = AffairDB()


def affairdata():
    datas_ = (
        (u'张三', '10001'),
        ('C#\n----\n456', '10002'),
        ('Lisp\n123', '10003'),
        ('Objective-C', '10004'),
        ('Perl', '10005'),
        ('Ruby', '10006'),
    )
    for i in datas_:
        name, pid = i[0], i[1]
        affair = Affair(pid, name)
        affairList.append(affair)