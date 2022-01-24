import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("隐形窗口")
    win.resize(400, 300)
    button = QPushButton("我的按钮", win)
    win.setWindowOpacity(0.8)  # 数值在0.0到1.0之间，越小越透明
    win.show()
    sys.exit(app.exec_())