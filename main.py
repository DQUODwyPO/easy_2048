from PySide6 import QtGui, QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from random import randint

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.fon = QtGui.QPixmap('1.png')
        self.item = QtGui.QPixmap('2_1.png')
        self.label.setPixmap(self.fon)
        self.label2 = QtWidgets.QLabel(self)
        self.init_mas()

    def init_mas(self):
        self.mas = [[0] * 6 for i in range(6)]
        self.mas_change = [[0] * 6 for i in range(6)]
        self.mas_labels = []
        for i in range(6):
            labels = []
            for j in range(6):
                labels.append(QtWidgets.QLabel(self))
            self.mas_labels.append(labels)
        for i in range(6):
            for j in range(6):
                self.mas_labels[i][j].setGeometry(13 + j*14 + j*107,12 + i*14 + i*107, 107, 107)
        print(self.mas_labels)
        x = randint(0,5)
        y = randint(0,5)
        self.mas_labels[x][y].setPixmap(QtGui.QPixmap('2_1.png'))
        self.mas[x][y] = 1

    def move_block(self,x1,y1,x2,y2):
        if self.mas[x1][y1] == 0:
            return False
        if self.mas[x2][y2] == 0 and self.mas[x1][y1] != 0:
            self.mas[x2][y2] = self.mas[x1][y1]
            self.mas_labels[x2][y2].setPixmap(QtGui.QPixmap('2_'
                                                            +str(self.mas[x2][y2])+'.png'))
            self.mas[x1][y1] = 0
            self.mas_labels[x1][y1].clear()
            return True
        if self.mas[x1][y1] == self.mas[x2][y2] and self.mas[x1][y1] != 0 \
                and self.mas_change[x1][y1] == 0 and self.mas_change[x2][y2] == 0 :
            self.mas[x2][y2] = self.mas[x1][y1] + 1
            self.mas_labels[x2][y2].setPixmap(QtGui.QPixmap('2_' + str(self.mas[x2][y2]) + '.png'))
            self.mas_change[x2][y2] = 1
            self.mas[x1][y1] = 0
            self.mas_labels[x1][y1].clear()
        return False

    def clear_(self):
        for i in range(6):
            for j in range(6):
                self.mas_change[i][j] = 0

    def func_move(self, direction):
        change = True
        if direction == 0:
            while change:
                change = False
                for i in range(1, 6):
                    for j in range(6):
                        answ = self.move_block(i,j,i-1,j)
                        if answ:
                            change = True
        if direction == 1:
            while change:
                change = False
                for i in range(6):
                    for j in range(4, -1, -1):
                        answ = self.move_block(i, j, i, j+1)
                        if answ:
                            change = True
        if direction == 2:
            while change:
                change = False
                for i in range(4, -1, -1):
                    for j in range(6):
                        answ = self.move_block(i, j, i + 1, j)
                        if answ:
                            change = True
        if direction == 3:
            while change:
                change = False
                for i in range(6):
                    for j in range(1, 6):
                        answ = self.move_block(i, j, i, j - 1)
                        if answ:
                            change = True
        self.clear_()
        gameend = True
        for i in range(6):
            for j in range(6):
                if self.mas[i][j] == 0:
                       gameend = False
        if gameend:
            self.close()
        else:
            while True:
                x = randint(0, 5)
                y = randint(0, 5)
                if self.mas[x][y] == 0:
                    self.mas_labels[x][y].setPixmap(QtGui.QPixmap('2_1.png'))
                    self.mas[x][y] = 1
                    break

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:

        if event.key() == Qt.Key.Key_Up:
            self.func_move(0)
        if event.key() == Qt.Key.Key_Down:
            self.func_move(2)
        if event.key() == Qt.Key.Key_Left:
            self.func_move(3)
        if event.key() == Qt.Key.Key_Right:
            self.func_move(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(['Easy 2048'])
    w = Window()
    w.setWindowTitle('Easy 2048')
    w.setMaximumHeight(736)
    w.setMaximumWidth(736)
    w.setMinimumSize(736,736)
    w.show()
    app.exec()



