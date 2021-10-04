from PyQt5.QtCore import QObject, pyqtSignal


class MySignal(QObject):
    sendms = pyqtSignal(object)  # 括号内的参数表示信号发送的参数的类型，object表示发送的参数是一个对象。
    sendms1 = pyqtSignal(str, int, int)  # 发送多个参数的信号

    def run(self):
        self.sendms.emit('Hello World')

    def run1(self):
        self.sendms1.emit('Hello PyQt5', 21, 22)


class MySlot(QObject):
    def get(self, ms):
        print('接收到的信息是：' + ms)

    def get1(self, ms, a, b):
        print('接收到的信息是：' + ms)
        print('接收到的数字是：', a, '和', b)


if __name__ == '__main__':
    mysig = MySignal()
    myslot = MySlot()

    mysig.sendms.connect(myslot.get)  # 连接信号
    mysig.run()

    mysig.sendms.disconnect(myslot.get)  # 解除信号连接
    mysig.run()

    mysig.sendms1.connect(myslot.get1)
    mysig.run1()