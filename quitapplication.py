import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QHBoxLayout, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle('退出按钮')

        self.button = QPushButton('退出', self)  # 加self为全局变量，如果不加self,则不是全局变量
        # self.button.setGeometry(300, 200, 100, 50)
        self.button.clicked.connect(self.onclick_button)  # self.button为全局变量，如果不加self,则不是全局变量

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        center_widget = QWidget()
        center_widget.setLayout(layout)

        self.setCentralWidget(center_widget)

    # 自定义一个按钮单击槽，实现关闭窗口功能
    def onclick_button(self):
        sender = self.sender()
        # print(sender.text() + "按钮被按下")
        message_box = QMessageBox.information(None, '提示', f'{sender.text()}按钮被按下,你确定要退出窗口',
                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if message_box == QMessageBox.Yes:
            app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuitApplication()
    window.show()
    sys.exit(app.exec_())
