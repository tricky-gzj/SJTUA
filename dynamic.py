#-*- coding:utf-8 -*-
# DYNAMIC coded by Mr. Gong
# Create your classes here
# you may use :
# from PySide import QtCore, QtGui

from clist import *

dynamicList = []

class Dynamic:
    def __init__(self, pid = 0, name = "lazy"):
        self.pid = pid
        self.name = name

    def getIcon(self):
        iconid = int(self.pid) % 4
        return './head/' + str(iconid) + '.png'

class DynamicDB:
    def __init__(self):
        self.db = "members.db"
        self.memberList = []
        self.readDynamic()

    def readDynamic(self):
        self.memberList = []
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
            member = Dynamic(pid, name)
            memberList.append(member)

    def searchDynamic(self,tags):
        self.memberList = []

class DynamicList(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(0, 60, 100, 540)

        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.setGeometry(10, 5, 450, 30)

        self.lineedit.returnPressed.connect(self._lineedit_returnPressed)
        self.lineedit.textChanged.connect(self._lineedit_textChanged)

        self.item_box = ItemBox()
        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(10, 75, 680, 460)
        self.list_view.setSpacing(3)

        self.list_model = ListModel(self.item_box)
        self.list_view.setModel(self.list_model)
        self.list_view.setIconSize(QtCore.QSize(50, 50))

        self.db = DynamicDB()

    def _lineedit_textChanged(self, text):
        print "text changed:", text

        self.item_box.filter_list_by_keyword(text)
        self.list_view.update()

    def _lineedit_returnPressed(self):
        text = self.lineedit.text()

        print "return press:", text
        print "items:", self.item_box.items

def dynamicdata():
    for i in datas_:
        name, pid = i[0], i[1]
        member = Dynamic(pid, name)
        memberList.append(member)