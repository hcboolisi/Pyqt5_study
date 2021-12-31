import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication


class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        self.setWindowTitle('QSS设置标签和按钮背景图片')
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet("QLabel{border-image: url(../image_1/3.jpg);}")
        # label1.setFixedHeight(300)
        # label1.setFixedWidth(400)
        label1.setFixedSize(400, 300)

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(48, 48)
        btn1.setMinimumSize(48, 48)

        style = '''
                #btn1{
                    border-radius:4px;  
                    background-image:url(../image/按钮图标1.jpg);
                }
                
                #btn1:pressed{
                    background-image:url(../image/按钮图标2.jpg);
                }
        
        '''
        btn1.setStyleSheet(style)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(btn1)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LabelButtonBackground()
    w.show()
    sys.exit(app.exec_())