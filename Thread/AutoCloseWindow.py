import sys

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=120><b>Hello World,窗口再5秒后自动关闭</b></font>')
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000, app.quit)
    sys.exit(app.exec_())