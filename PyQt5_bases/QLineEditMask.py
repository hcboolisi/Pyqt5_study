"""
0：必须输入数字（0—9），不允许使用加号+和减号－。
9：可选择输入数字或空格，不允许使用加号和减号。
#：可选择输入数字或空格，允许使用加号和减号，空白会转换为空格。
L：必须输入字母（A—Z）。
?：可选择输入字母（A—Z）。
A：必须输入字母或数字。
a：可选择输入字母或数字。
&：必须输入任一字符或空格。
C：可选择输入任一字符或空格。
<：使其后所有字符转换为小写。
>：使其后所有字符转换为大写。
!：使输入掩码从右到左显示。
\(反斜杠)：使其后的字符显示为原义字符。
密码：文本框中输入的任何字符都按字面字符保存，但显示为星号*。
"""

import sys
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class LineEditMask(QWidget):
    def __init__(self):
        super(LineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        form_layout = QFormLayout()

        ip_line_edit = QLineEdit()
        mac_line_edit = QLineEdit()
        data_line_edit = QLineEdit()
        license_line_edit = QLineEdit()

        ip_line_edit.setInputMask('000.000.000.000;_')
        mac_line_edit.setInputMask('HH-HH-HH-HH-HH-HH;*')
        data_line_edit.setInputMask('0000-00-00;_')
        license_line_edit.setInputMask('>AAAA-AAAA-AAAA-AAAA-AAAA')

        form_layout.addRow('IP输入：', ip_line_edit)
        form_layout.addRow('mac输入：', mac_line_edit)
        form_layout.addRow('日期输入: ', data_line_edit)
        form_layout.addRow('序列号输入：', license_line_edit)

        self.setLayout(form_layout)
        self.setWindowTitle('使用掩码控制QLineEdit输入')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LineEditMask()
    w.show()
    sys.exit(app.exec_())