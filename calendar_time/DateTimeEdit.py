import sys

from PyQt5.QtCore import QDateTime, QDate, QTime
from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit, QVBoxLayout


class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置不同风格的日期和时间')
        self.resize(300, 90)

        datetimeedit1 = QDateTimeEdit()
        datetimeedit2 = QDateTimeEdit(QDateTime.currentDateTime())
        datetimeedit2.setCalendarPopup(True)

        dateedit = QDateTimeEdit(QDate.currentDate())
        timeedit = QDateTimeEdit(QTime.currentTime())

        datetimeedit1.setDisplayFormat('yyyy-MM--dd HH:mm:ss')
        datetimeedit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')
        dateedit.setDisplayFormat('yyyy.MM.dd')
        timeedit.setDisplayFormat('HH:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(datetimeedit1)
        vbox.addWidget(datetimeedit2)
        vbox.addWidget(dateedit)
        vbox.addWidget(timeedit)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DateTimeEdit()
    w.show()
    sys.exit(app.exec_())