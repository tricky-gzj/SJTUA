# -*- coding:utf-8 -*-

import re
import sys
import glob
import os
from PySide import QtCore, QtGui

MemberList=[]

class Member:
    def __init__(self, pid = 0, name = "lazy"):
        self.pid = pid
        self.name = name

    def getIcon(self):
        iconid = int(self.pid) % 4
        return './head/' + str(iconid) + '.png'


class MemberDB:
    def __init__(self):
        self.db = "members.db"
        self.memberList = []
        self.readMember()

    def readMember(self):
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
            member = Member(pid, name)
            MemberList.append(member)

    def searchMember(self,tags):
        self.memberList = []



class Magic:
    def __init__(self, member):
        self.pid = member.pid
        self.fullname = member.name
        self.icon_path = member.getIcon()
        self.pid = member.pid

    def __repr__(self):
        return "<Magic %s>" % self.fullname


class MagicBox(object):
    def __init__(self):
        self._magics = set()

        for i in MemberList:
            magic = Magic(i)
            self._magics.add(magic)

        self._cache = list(self._magics)

    @property
    def magics_count(self):
        return len(self._magics)

    @property
    def all_magics(self):
        return self._magics

    @property
    def magics(self):
        return self._cache

    def filter_list_by_keyword(self, keyword):
        self._cache = [i
                       for i in self._magics
                       if i.fullname.find(keyword) != -1 or \
                       re.match(keyword, i.fullname, re.I)]


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, magic_box):
        super(ListModel, self).__init__()
        self.magic_box = magic_box

    def rowCount(self, parent):
        return len(self.magic_box.magics)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        magic = self.magic_box.magics[index.row()]
        fullname, icon_path, user_data = magic.fullname, magic.icon_path, magic.pid

        if role == QtCore.Qt.DisplayRole:
            return fullname

        elif role == QtCore.Qt.DecorationRole:
            icon = QtGui.QIcon(icon_path)
            return icon

        elif role == QtCore.Qt.BackgroundColorRole:
            colorTable = [0x000000, 0xFFFFE0, 0xDCDCDC, 0xF0FFFF,
                          0xD1EEEE, 0xCDCDC1, 0x00FFFF, 0x00FF7F]
            cc = eval(magic.pid) % 8
            color = QtGui.QColor(colorTable[cc])
            return QtGui.QBrush(color)

        return None

class MemberLocate(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(0, 60, 700, 540)

        self.lineedit = QtGui.QLineEdit(self)
        self.lineedit.setGeometry(10, 5, 450, 30)

        self.lineedit.returnPressed.connect(self._lineedit_returnPressed)
        self.lineedit.textChanged.connect(self._lineedit_textChanged)

        self.magic_box = MagicBox()
        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(10, 75, 680, 460)

        self.list_model = ListModel(self.magic_box)
        self.list_view.setModel(self.list_model)
        self.list_view.setIconSize(QtCore.QSize(50, 50))

        self.db = MemberDB()

    def _lineedit_textChanged(self, text):
        print "text changed:", text

        self.magic_box.filter_list_by_keyword(text)
        self.list_view.update()

    def _lineedit_returnPressed(self):
        text = self.lineedit.text()

        print "return press:", text
        print "magics:", self.magic_box.magics

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
    member = Member(pid, name)
    MemberList.append(member)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())


