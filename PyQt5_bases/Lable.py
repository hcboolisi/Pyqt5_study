import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QApplication, QWidget

'''
这里的父类是继承自QWidget,如果要继承自QMainWindow,则要设置一下中心窗口central_widget,不然显示不出来相关控件
，设置代码如下：central_widget = QWidget()
              self.setCentralWidget(central_widget)
              central_widget.setLayout(vbox)
详细例子见Label_1
'''


class LabelWidget(QWidget):
    def __init__(self):
        super(LabelWidget, self).__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel(self)  # self 可以有，也可以无
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        label1.setText('<font color = yellow >这是一个文本标签</font>')
        label1.setAlignment(Qt.AlignCenter)
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置标签背景颜色为蓝色，注意W是大写的，也可以使用QPalette.BackGround
                                                    # 不过好像已经被废弃。
        label1.setPalette(palette)

        label2.setText('<a href="#">欢饮使用Python GUI 程序</a>')

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('../图标.jpg'))

        label4.setText("<a href='https://www.baidu.com/'>点击打开百度网站</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")
        label4.setOpenExternalLinks(True)  # 设置是否打开扩展链接

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.LinkHovered)
        label4.linkActivated.connect(self.LinkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('label控件演示')


    def LinkHovered(self):
        print('当鼠标划过label2时，触发该事件')


    def LinkClicked(self):
        print('当鼠标点击label4时，触发该事件')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LabelWidget()
    w.show()
    sys.exit(app.exec_())
