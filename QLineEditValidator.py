import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class LineEditValitator(QWidget):
    def __init__(self):
        super(LineEditValitator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LineEdit文本输入校验器（validator）')
        form_layout = QFormLayout()

        int_line_edit = QLineEdit()
        double_line_edit = QLineEdit()
        regexp_line_edit = QLineEdit()

        form_layout.addRow('<font color=#FF0000 size=4>整数校验输入</font>', int_line_edit)
        form_layout.addRow('浮点数校验输入', double_line_edit)
        form_layout.addRow('字母和数字校验输入', regexp_line_edit)

        int_line_edit.setPlaceholderText('请输入整数')
        double_line_edit.setPlaceholderText('请输入浮点数，保留两位小数')
        regexp_line_edit.setPlaceholderText('请输入字母和数字')

        # 创建整数检验器 范围[-999999999, 999999999]
        intvalidator = QIntValidator()
        intvalidator.setRange(-999999999, 999999999)

        # 创建浮点数校验器 范围【-999，999】，保留2位小数
        doublevalidator = QDoubleValidator()
        doublevalidator.setRange(-999, 999)
        doublevalidator.setDecimals(2)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)

        # 创建字母和数字校验器 利用正则表达式
        regexpvalidator = QRegExpValidator()
        reg = QRegExp('[a-zA-Z0-9]+$')
        regexpvalidator.setRegExp(reg)

        int_line_edit.setValidator(intvalidator)
        double_line_edit.setValidator(doublevalidator)
        regexp_line_edit.setValidator(regexpvalidator)

        self.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LineEditValitator()
    w.show()
    sys.exit(app.exec_())