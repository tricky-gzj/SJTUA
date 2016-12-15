#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from PySide import QtCore, QtGui
from quitdialog import *
from magic import *

DYNAMIC, SCHEDULE, MESSAGE, MEMBER = range(4)
winState = DYNAMIC
assName = "SJTU_CC"


class mainWindow(QtGui.QMainWindow):
    def __init__(self, state):
        super(mainWindow, self).__init__()
        self.state = state
        self.settings = load_settings(settings_path)

        self.w = 1000
        self.h = 600
        self.setFixedSize(QtCore.QSize(self.w, self.h))

        self.setGeometry(0, 0, self.w, self.h)
        self.center()
        self.setWindowTitle('SJTUA')
        self.logo_icon = QtGui.QIcon("logo_SJTUA.png")
        self.setWindowIcon(self.logo_icon)

        self.sys_tray_icon = QtGui.QSystemTrayIcon(parent=self)
        self.sys_tray_icon.setIcon(self.logo_icon)
        self.sys_tray_icon.activated.connect(self.on_sys_tray_icon_clicked)
        self.sys_tray_icon.messageClicked.connect(self.on_sys_tray_icon_msg_clicked)
        self.sys_tray_icon.show()

        TitleRect=0,0,self.w,50
        self.TitleBoard = TitleBoard(self,TitleRect,assName,winState)
        self.statusbar = self.statusBar()
        self.connect(self.TitleBoard, QtCore.SIGNAL("messageToStatusbar(QString)"),
                     self.statusbar, QtCore.SLOT("showMessage(QString)"))

        self.demo = MemberLocate(self)


    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
        (screen.height() - size.height()) / 2)

    def show_and_raise(self):
        self.show()
        self.raise_()

    @staticmethod
    def confirm_quit(main_win, close_evt=None):
        if main_win.settings["confirm"]:
            QuitConfirmDlg.popup_and_get_inputs(main_win, main_win.settings)
            save_settings(main_win.settings)

        if main_win.settings['x_action_is_quit']:
            if close_evt:
                close_evt.accept()

            return True
        else:
            if close_evt:
                close_evt.ignore()

            main_win.hide()

            return False

    def closeEvent(self, evt):
        self.confirm_quit(self, evt)

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()

    def on_sys_tray_icon_clicked(self, activation_reason):
        assert activation_reason in (
            QtGui.QSystemTrayIcon.Trigger,
            QtGui.QSystemTrayIcon.DoubleClick,
            QtGui.QSystemTrayIcon.MiddleClick)

        self.show_and_raise()

    def on_sys_tray_icon_msg_clicked(self, *args, **kwargs):
        print 'msg clicked'

    def sys_tray_icon_show_msg(self, title, msg,
                               icon=QtGui.QSystemTrayIcon.MessageIcon(),
                               msecs=10000):
        if self.sys_tray_icon.supportsMessages():
            self.sys_tray_icon.showMessage(title, msg, icon, msecs)


class TitleBoard(QtGui.QFrame):
    def __init__(self, parent, rect, assName, state):
        QtGui.QFrame.__init__(self, parent)
        self.assName = assName
        self.state= state
        self.x,self.y,self.w,self.h = rect
        self.resize(self.w,self.h)
        self.rect = QtCore.QRect(self.x,self.y,self.w,self.h)
        self.setFrameRect(self.rect)
        self.setWidgt()

        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.update()

    def setWidgt(self):
        w=self.w
        h=self.h

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.cbx = QtGui.QComboBox(self)
        self.cbx.addItem(assName)
        self.cbx.addItem(u"注销")
        self.cbx.setFont(font)
        self.cbx.currentIndexChanged.connect(self._cbx_currentIndexChanged)
        self.cbx.setGeometry(10, 5, 130, 40)

        font.setFamily("Song Typeface")
        font.setPointSize(18)
        self.btn1 = QtGui.QPushButton(u"动态", self)
        self.btn1.setFlat(True)
        self.btn1.clicked.connect(self._btn1_cb)
        self.btn1.setGeometry(345, 10, 75, 40)
        self.btn1.setFont(font)
        self.btn2 = QtGui.QPushButton(u"日程", self)
        self.btn2.setFlat(True)
        self.btn2.clicked.connect(self._btn2_cb)
        self.btn2.setGeometry(425, 10, 75, 40)
        self.btn2.setFont(font)
        self.btn3 = QtGui.QPushButton(u"沟通", self)
        self.btn3.setFlat(True)
        self.btn3.clicked.connect(self._btn3_cb)
        self.btn3.setGeometry(505, 10, 75, 40)
        self.btn3.setFont(font)
        self.btn4 = QtGui.QPushButton(u"成员", self)
        self.btn4.setFlat(True)
        self.btn4.clicked.connect(self._btn4_cb)
        self.btn4.setGeometry(585, 10, 75, 40)
        self.btn4.setFont(font)

        self.tbtn = QtGui.QToolButton(self)
        icon = QtGui.QIcon("plus.png")
        self.tbtn.setIcon(icon)
        self.tbtn.setIconSize(QtCore.QSize(24, 24))
        self.tbtn.clicked.connect(self._tbtn_cb)
        self.tbtn.move(950, 15)


    def emitStatus(self,text):
        self.emit(QtCore.SIGNAL("messageToStatusbar(QString)"),text)

    def _cbx_currentIndexChanged(self):
        #sys.exit(app.exec_())
        pass

    def _btn1_cb(self):
        self.emitStatus("clicked1")
        self.update()

    def _btn2_cb(self):
        self.emitStatus("clicked2")
        self.update()

    def _btn3_cb(self):
        self.emitStatus("clicked3")
        self.update()

    def _btn4_cb(self):
        self.emitStatus("clicked4")
        self.update()

    def _tbtn_cb(self):
        self.emitStatus("clicked +")
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        rect = self.contentsRect()
        painter.fillRect(rect, 'white')


    def keyPressEvent(self, event):
        if not self.isStarted or self.curPiece.shape() == Tetrominoes.NoShape:
            QtGui.QWidget.keyPressEvent(self, event)
            return

        key = event.key()
        if key == QtCore.Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return
        elif key == QtCore.Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
        elif key == QtCore.Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
        elif key == QtCore.Qt.Key_Down:
            self.tryMove(self.curPiece.rotatedRight(), self.curX, self.curY)
        elif key == QtCore.Qt.Key_Up:
            self.tryMove(self.curPiece.rotatedLeft(), self.curX, self.curY)
        elif key == QtCore.Qt.Key_Space:
            self.dropDown()
        elif key == QtCore.Qt.Key_D:
            self.oneLineDown()
        else:
            QtGui.QWidget.keyPressEvent(self, event)


    def drawSquare(self, painter, x, y, shape):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QtGui.QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.light())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.dark())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


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

    def _lineedit_textChanged(self, text):
        print "text changed:", text

        self.magic_box.filter_list_by_keyword(text)
        self.list_view.update()

    def _lineedit_returnPressed(self):
        text = self.lineedit.text()

        print "return press:", text
        print "magics:", self.magic_box.magics


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    main = mainWindow(state="Member")

    main.show_and_raise()
    sys.exit(app.exec_())

