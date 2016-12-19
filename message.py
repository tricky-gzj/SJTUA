#-*- coding:utf-8 -*-
# DYNAMIC coded by Mr. Ma & Mr. Gong
# Create your classes here
# you may use :
# from PySide import QtCore, QtGui

from PySide import QtCore, QtGui
import sqlite3
import os
import sys


css = '''
div {
    line-height: 27px;
}
.nickname {
    color: #A52A2A;
    font-weight: bolder;
}
.ts {
    color: #7F7F7F;
}
'''

class Message:
    def __init__(self, m):
        dnid, bgntime, endtime, content, pointer = m
        self.dnid = dnid
        self.bgntime = bgntime
        self.endtime = endtime
        self.content = content
        self.pointer = pointer

    def getIcon(self):
        iconid = int(self.dnid) % 4
        return './head/' + str(iconid) + '.png'


class MessageDB:
    def __init__(self):
        conn = sqlite3.connect('test.db')
        self.cu = conn.cursor()
        self.messageList = []
        self.readMessage()

    def readMessage(self):
        self.messageList = []
        self.cu.execute("select dnid, bgntime, endtime, content, pointer from message")
        for row in self.cu:
            m = Message(row)
            self.messageList.append(m)

    # def newMessage(self, message):


    def searchMessage(self,tags):
        self.messageList = []


class MessageList(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(0, 60, 1000, 540)
        self.db = MessageDB()

        self.list_view = QtGui.QListView(self)
        self.list_view.setGeometry(0, 0, 1000, 540)
        self.list_view.setSpacing(3)

        self.list_model = MessageListModel(self.db.messageList)
        self.list_view.setModel(self.list_model)
        self.list_view.setIconSize(QtCore.QSize(50, 50))


class MessageListModel(QtCore.QAbstractListModel):
    def __init__(self, messageList):
        super(MessageListModel, self).__init__()
        self._items = set()
        for item in messageList:
            self._items.add(item)
        self.items = list(self._items)

    def rowCount(self, parent):
        return len(self.items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        item = self.items[index.row()]
        fullname, icon_path, user_data = item.content, item.getIcon(), item.dnid

        if role == QtCore.Qt.DisplayRole:
            return fullname

        elif role == QtCore.Qt.DecorationRole:
            icon = QtGui.QIcon(icon_path)
            return icon

        elif role == QtCore.Qt.BackgroundColorRole:
            colorTable = [0xCDCDC1, 0xFFFFE0, 0xDCDCDC, 0xF0FFFF,
                          0xD1EEEE, 0xCDCDC1, 0x00FFFF, 0x00FF7F]
            cc = item.dnid % 8
            color = QtGui.QColor(colorTable[cc])
            return QtGui.QBrush(color)

        return None


class EmailEditor(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.setGeometry(265, 60, 745, 540)

        self.text_doc = QtGui.QTextDocument()
        self.text_doc.setDefaultStyleSheet(css)

        self.text_edit = QtGui.QTextEdit(self)
        self.text_edit.setGeometry(0, 0, 745, 540)
        self.text_edit.setDocument(self.text_doc)
        self.text_edit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        #        self.text_edit.setReadOnly(True)
        self.log(msg=' ')
        self.log(msg='hello\nworld')
        self.log(msg='hello\nworld')
        self.log(msg=u'中文输入\n法 KDE 桌面环境')
        self.log(msg='hello\nworld')
        self.log(msg='hello\nworld')
        self.log(msg='hello\nworld')
        self.log(msg='hello\nworld')

        self.top_btn = QtGui.QPushButton("top", self)
        self.top_btn.move(150, 280)
        self.top_btn.clicked.connect(self.goto_top_btn_clicked)

        self.buttom_btn = QtGui.QPushButton("bottom", self)
        self.buttom_btn.move(150, 300)
        self.buttom_btn.clicked.connect(self.goto_buttom_btn_clicked)

        # t = self.text_edit.toHtml()

        self.show()

    def goto_top_btn_clicked(self):
        scroll_bar = self.text_edit.verticalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.minimum())

    def goto_buttom_btn_clicked(self):
        scroll_bar = self.text_edit.verticalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.maximum())

    def log(self, nickname='foo', msg=None):
        t = QtCore.QTime()
        now_time = t.currentTime().toString()

        msg = msg.replace(os.linesep, '<br />')
        log = '''<div><span class="nickname">%s</span>&nbsp;&nbsp;<span class="ts">%s</span><p class="msg">%s</p></div>''' % \
              (nickname, now_time, msg)
        self.text_edit.append(log)

        #        t = self.text_doc.toHtml()
        #        with open('log.txt', 'w') as f:
        #            f.write(t.toUtf8())

        #        # buf = t
        #        buf = QtCore.QString('<html><body>你好</body></html>'.decode('utf-8'))
        #        self.text_doc.setHtml(buf)

        #        t = self.text_doc.toHtml()
        #        with open('log2.txt', 'w') as f:
        #            f.write(t.toUtf8())




