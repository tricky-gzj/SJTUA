#-*- coding:utf-8 -*-

import json
import os
from PySide import QtCore, QtGui

default_settings = {
    "confirm": True,
    "x_action_is_quit": False,
}

settings_path = 'settings.json'



def save_settings(settings, path=settings_path):
    with open(path, 'w') as f:
        buf = json.dumps(settings)
        f.write(buf)


def load_settings(path=settings_path):
    if os.path.exists(path):
        with open(path) as f:
            c = f.read()
            settings = json.loads(c)
    else:
        global default_settings
        settings = default_settings

    return settings


class CustomDlg(QtGui.QDialog):
    """
    Custom dialog template.

    You should override there method:
     - __init__
     - get_inputs
     - popup_and_get_inputs
    """

    def __init__(self, parent, settings):
        super(CustomDlg, self).__init__(parent)

        self.resize(400, 250)

        self._settings = settings
        self.setModal(True)

        # add custom sub-widgets here ...

    def keyPressEvent(self, evt):
        close_win_cmd_w = (evt.key() == QtCore.Qt.Key_W and evt.modifiers() == QtCore.Qt.ControlModifier)
        close_win_esc = (evt.key() == QtCore.Qt.Key_Escape)

        if close_win_cmd_w or close_win_esc:
            self.close()
            return self._settings

    def get_inputs(self):
        # update self._settings from custom sub-widgets ...
        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        dlg = CustomDlg(parent, settings)
        dlg.show()
        dlg.exec_()


class QuitConfirmDlg(CustomDlg):
    def __init__(self, parent, settings):
        super(QuitConfirmDlg, self).__init__(parent, settings)

        self.resize(400, 250)
        self.setWindowTitle(u"关闭窗口")

        self.tips_label = QtGui.QLabel(u"关闭窗口时，您是想：", self)
        self.tips_label.setGeometry(40, 40, 280, 15)

        self.minimize_rbtn = QtGui.QRadioButton(u"最小化到托盘", self)
        self.minimize_rbtn.setGeometry(70, 90, 180, 20)

        self.exit_rbtn = QtGui.QRadioButton(u"退出程序", self)
        self.exit_rbtn.setGeometry(70, 120, 110, 20)

        self.no_confirm_cbox = QtGui.QCheckBox(u"下次别再问我", self)
        self.no_confirm_cbox.setGeometry(40, 180, 150, 20)

        self.minimize_rbtn.setChecked(not self._settings['x_action_is_quit'])
        self.exit_rbtn.setChecked(self._settings['x_action_is_quit'])
        self.no_confirm_cbox.setChecked(not self._settings['confirm'])

    def get_inputs(self):
        self._settings["x_action_is_quit"] = self.exit_rbtn.isChecked()
        self._settings["confirm"] = not self.no_confirm_cbox.isChecked()

        return self._settings

    @staticmethod
    def popup_and_get_inputs(parent, settings):
        dlg = QuitConfirmDlg(parent, settings)
        dlg.show()
        dlg.exec_()

        return dlg.get_inputs()