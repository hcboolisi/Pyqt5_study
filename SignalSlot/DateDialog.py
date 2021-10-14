import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)

        self.setWindowTitle('日期对话框')

        vbox = QVBoxLayout()

        self.datetime = QDateTimeEdit()  # 增加一个日期时间输入框，QDateTimeEdit
        self.datetime.setCalendarPopup(True)  # 设置该日期时间输入框的日历为弹出模式，Popup
        self.datetime.setDateTime(QDateTime.currentDateTime())  # 设置该输入框的时间为当前时间。

        # 利用QDialogButtonBox为该日期时间对话框新增两个按键，OK和Cancel，并设置其布局为水平布局
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)  # 将OK按键的接收信号绑定到自带的接收槽函数上，accept
        buttons.rejected.connect(self.reject)  # 将Cancel按键的取消（拒绝）信号绑定到自带的取消槽函数上，reject

        vbox.addWidget(self.datetime)
        vbox.addWidget(buttons)
        self.setLayout(vbox)

    # 设置一个函数返回当前日期时间输入框里的时间
    def dateTime(self):
        return self.datetime.dateTime()

    # 设置一个静态方法，用来显示该日期时间对话框，并获得在该对话框上选择的时间
    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)  # 实例化一个自己，也就是自己这个 DateDialog日期时间对话框类
        result = dialog.exec()  # 显示自己这个对话框，然后把选择的按键结果（OK或者Cancel）赋给result
        date = dialog.dateTime()  # 调用自己的的dateTime方法，来获得日期输入框里面的日期时间
        # 在对话框点击接受，也就是OK按钮的时候，返回获得的日期，返回获得的时间。如果点击的是Cancel按钮的话，则不返回。
        return date.date(), date.time(), result == QDialog.Accepted

