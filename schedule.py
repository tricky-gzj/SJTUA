#-*- coding:utf-8 -*-
# DYNAMIC coded by Mr. Tang
# Create your classes here

import sys
from PySide import QtGui, QtCore

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

        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(0, 0, 600, 540)
        self.list_view.setSpacing(3)

        self.list_model = AffairListModel(affairList)
        self.list_view.setModel(self.list_model)
        self.list_view.setIconSize(QtCore.QSize(50, 50))

        self.db = AffairDB()


class AffairListModel(QtCore.QAbstractListModel):
    def __init__(self, affairList):
        super(AffairListModel, self).__init__()
        self._items = set()
        for item in affairList:
            self._items.add(item)
        self.items = list(self._items)

    def rowCount(self, parent):
        return len(self.items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        item = self.items[index.row()]
        fullname, icon_path, user_data = item.name, item.getIcon(), item.pid

        if role == QtCore.Qt.DisplayRole:
            return fullname

        elif role == QtCore.Qt.DecorationRole:
            icon = QtGui.QIcon(icon_path)
            return icon

        elif role == QtCore.Qt.BackgroundColorRole:
            colorTable = [0x000000, 0xFFFFE0, 0xDCDCDC, 0xF0FFFF,
                          0xD1EEEE, 0xCDCDC1, 0x00FFFF, 0x00FF7F]
            cc = eval(item.pid) % 8
            color = QtGui.QColor(colorTable[cc])
            return QtGui.QBrush(color)

        return None

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