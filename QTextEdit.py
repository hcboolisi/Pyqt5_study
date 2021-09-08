'''
 font.setFamily('微软雅黑')  #字体
font.setBold(True)  #加粗
font.setItalic(True)    #斜体
font.setStrikeOut(True)  #删除线
font.setUnderline(True)   #下划线
font.setPointSize(23)   #字体大小
font.setWeight(25)   #可能是字体的粗细
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QApplication


class TextEdit(QWidget):
    def __init__(self):
        super(TextEdit, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('多行文本框')

        vbox_layout = QVBoxLayout()

        self.textedit = QTextEdit()
        self.btntext = QPushButton('显示文本')
        self.btnHTML = QPushButton('显示HTML')

        vbox_layout.addWidget(self.textedit)
        vbox_layout.addWidget(self.btntext)
        vbox_layout.addWidget(self.btnHTML)

        self.setLayout(vbox_layout)

        self.btntext.clicked.connect(self.onclickbtntext)
        self.btnHTML.clicked.connect(self.onclickbtnHTML)

        # 两种设置不可编辑的方法
        # self.textedit.setFocusPolicy(Qt.NoFocus)
        self.textedit.setReadOnly(True)
        self.resize(400, 300)


    def onclickbtntext(self):
        # QFont,第一个参数是字体，第二个是字体大小，
        # 第三个是字体宽度（粗细），第四个是设置斜体
        self.textedit.setFont(QFont('宋体', 16, 100, True))
        self.textedit.setPlainText('Hello Word ! 你好世界！')

    def onclickbtnHTML(self):
        self.textedit.setFont(QFont())
        self.textedit.setHtml('<font color="blue" size="8">Hello World!</font>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TextEdit()
    w.show()
    sys.exit(app.exec_())

