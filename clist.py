# -*- coding:utf-8 -*-

import re
import sys
import glob
import os
from PySide import QtCore, QtGui

memberList = []

class Item:
    def __init__(self, member):
        self.pid = member.pid
        self.fullname = member.name
        self.icon_path = member.getIcon()
        self.pid = member.pid

    def __repr__(self):
        return "<Item %s>" % self.fullname


class ItemBox(object):
    def __init__(self):
        self._items = set()

        for i in memberList:
            item = Item(i)
            self._items.add(item)

        self._cache = list(self._items)

    @property
    def items_count(self):
        return len(self._items)

    @property
    def all_items(self):
        return self._items

    @property
    def items(self):
        return self._cache

    def filter_list_by_keyword(self, keyword):
        self._cache = [i
                       for i in self._items
                       if i.fullname.find(keyword) != -1 or \
                       re.match(keyword, i.fullname, re.I)]


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, item_box):
        super(ListModel, self).__init__()
        self.item_box = item_box

    def rowCount(self, parent):
        return len(self.item_box.items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        item = self.item_box.items[index.row()]
        fullname, icon_path, user_data = item.fullname, item.icon_path, item.pid

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



datas_ = (
            (u'张三', '10001'),
            ('C#\n----\n456', '10002'),
            ('Lisp\n123', '10003'),
            ('Objective-C', '10004'),
            ('Perl', '10005'),
            ('Ruby', '10006'),
        )






