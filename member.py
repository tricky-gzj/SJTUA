#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys
import glob
import os
from PySide import QtCore, QtGui



datas_ = (
    (u'张三', '10001'),
    ('C#\n----\n456', '10002'),
    ('Lisp\n123', '10003'),
    ('Objective-C', '10004'),
    ('Perl', '10005'),
    ('Ruby', '10006'),
)


MemberList=[]

class Member:
    def __init__(self, pid = 0, name = "lazy"):
        self.pid = pid
        self.name = name

    def getIcon(self):
        iconid = int(self.pid) % 4
        return './head/' + str(iconid) + '.png'


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
            #icon.(QtCore.QSize(32, 32))
            return icon

        elif role == QtCore.Qt.BackgroundColorRole:
            colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                          0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
            cc = eval(magic.pid) % 8

            color = QtGui.QColor(colorTable[cc])
            return QtGui.QBrush(color)

        return None


for i in datas_:
    name, pid = i[0], i[1]
    member = Member(pid, name)
    MemberList.append(member)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    demo = Demo()
    demo.show_and_raise()

    sys.exit(app.exec_())


