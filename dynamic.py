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
        self.db = "dynamics.db"
        self.dynamicList = []
        self.readDynamic()

    def readDynamic(self):
        self.dynamicList = []
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
            dynamic = Dynamic(pid, name)
            dynamicList.append(dynamic)

    def searchDynamic(self,tags):
        self.dynamicList = []

class DynamicList(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(0, 60, 1000, 540)

        self.item_box = ItemBox()
        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(0, 0, 1000, 540)
        self.list_view.setSpacing(3)

        self.list_model = ListModel(self.item_box)
        self.list_view.setModel(self.list_model)
        self.list_view.setIconSize(QtCore.QSize(50, 50))

        self.db = DynamicDB()


def dynamicdata():
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
        dynamic = Dynamic(pid, name)
        dynamicList.append(dynamic)