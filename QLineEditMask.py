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