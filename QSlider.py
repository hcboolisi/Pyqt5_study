import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QSlider, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class Slider(QWidget):
    def __init__(self):
        super(Slider, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSlider滑块')

        self.label = QLabel('你好Python,你好PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        self.slider = QSlider(Qt.Horizontal)  # 创建一个滑块实例，设置其为水平放置
        self.slider.setMaximum(48)  # 设置滑块的最大值为48
        self.slider.setMinimum(12)  # 设置滑块的最小值为12
        self.slider.setSingleStep(3)  # 设置滑块的步长值为3
        self.slider.setTickPosition(QSlider.TicksBelow)  # 设置刻度的位置在下方
        self.slider.setTickInterval(6)  # 设置刻度的间隔为6
        self.slider.setValue(20)  # 设置当前值为20

        self.slider_1 = QSlider(Qt.Vertical)
        self.slider_1.setMaximum(60)  # 设置滑块的最大值为60
        self.slider_1.setMinimum(10)  # 设置滑块的最小值为10
        self.slider_1.setSingleStep(5)  # 设置滑块的步长值为5
        self.slider_1.setTickPosition(QSlider.TicksLeft)  # 设置刻度的位置在左边
        self.slider_1.setTickInterval(5)  # 设置刻度的间隔为5
        self.slider_1.setValue(25)  # 设置当前值为25

        self.slider.valueChanged.connect(lambda: self.valuechange(self.slider))
        self.slider_1.valueChanged.connect(self.valuechange_1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.slider)
        vbox.addWidget(self.slider_1)

        self.setLayout(vbox)
        self.resize(300, 700)

    def valuechange(self, sld):
        print('当前的刻度值为： ', sld.value())
        self.label.setFont(QFont('宋体', sld.value()))

    def valuechange_1(self):
        sender = self.sender()
        print('当前的刻度值为： ', sender.value())
        self.label.setFont(QFont('Arial', sender.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Slider()
    w.show()
    sys.exit(app.exec_())