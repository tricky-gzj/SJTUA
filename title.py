# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\codespace\SJTUA\title.ui'
#
# Created: Sun Dec 04 16:22:29 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1000, 167)
        Frame.setMouseTracking(False)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.btn3 = QtGui.QPushButton(Frame)
        self.btn3.setGeometry(QtCore.QRect(500, 10, 75, 31))
        self.btn3.setObjectName("btn3")
        self.cbx = QtGui.QComboBox(Frame)
        self.cbx.setGeometry(QtCore.QRect(13, 0, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.cbx.setFont(font)
        self.cbx.setObjectName("cbx")
        self.cbx.addItem("")
        self.cbx.addItem("")
        self.btn1 = QtGui.QPushButton(Frame)
        self.btn1.setGeometry(QtCore.QRect(350, 0, 75, 41))
        font = QtGui.QFont()
