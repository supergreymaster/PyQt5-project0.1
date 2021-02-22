import PyQt5
import random
from PIL import Image, ImageDraw
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 240, 211, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 40, 231, 171))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Закрасить"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.do_paint = False

    def draw(self):
        b = 240
        new_image = Image.new("RGB", (200, 200), (b, b, b))
        drawer = ImageDraw.Draw(new_image)
        a = random.randrange(10, 100)
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        drawer.ellipse(((a, a), (200 - a, 200 - a)), (r, g, b))
        new_image.save('ball.png')

        self.pixmap = QPixmap('ball.png')
        self.image = QLabel(self)
        self.image.move(100, 10)
        self.image.resize(200, 200)
        self.image.setPixmap(self.pixmap)
        self.image.show()

        os.remove('ball.png')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())