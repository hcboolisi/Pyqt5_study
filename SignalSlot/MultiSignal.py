from PyQt5.QtCore import QObject, pyqtSignal


class MultiSignal(QObject):
    signal1 = pyqtSignal()

    signal2 = pyqtSignal(int)

    signal3 = pyqtSignal(int, str)

    signal4 = pyqtSignal(list)

    signal5 = pyqtSignal(dict)

    # 定义一个重载版本的信号，也就是槽函数的参数可以是[int,str]或者是[str]
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self):
        super(MultiSignal, self).__init__()
        self.signal1.connect(self.signal1Call)
        self.signal2.connect(self.signal2Call)
        self.signal3.connect(self.signal3Call)
        self.signal4.connect(self.signal4Call)
        self.signal5.connect(self.signal5Call)
        # 连接重载信号的时候，需要在提交和信号连接时同时指定参数类型
        self.signal6[int, str].connect(self.signal6Call)
        self.signal6[str].connect(self.signal6Overload)

        self.signal1.emit()
        self.signal2.emit(50)
        self.signal3.emit(30, '字符串')
        self.signal4.emit([1, 'asd', 3])
        self.signal5.emit({'name': 'bill', 'age': 30})
        # 连接重载信号的时候，需要在提交和信号连接时同时指定参数类型
        self.signal6[int, str].emit(62, '字符串')
        self.signal6[str].emit('字符串')

    def signal1Call(self):
        print('signal1 emit,value:')

    def signal2Call(self, val):
        print('signale2 emit,value:', val)

    def signal3Call(self, val, text):
        print('signal3 emit,value:', val, text)

    def signal4Call(self, val):
        print('signal4 emit,value:', val)

    def signal5Call(self, val):
        print('signal5 emit,value:', val)

    def signal6Call(self, val, text):
        print('signal6 emit,value:', val, text)

    def signal6Overload(self, val):
        print('signal6 Overload emit,value:', val)


if __name__ == '__main__':
    mysignal = MultiSignal()