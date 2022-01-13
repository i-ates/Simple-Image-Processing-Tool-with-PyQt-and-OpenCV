import qimage2ndarray
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
import sys
from skimage.io import imread
from operations import QImageToCvMat


class colorBalance(QWidget):

    def __init__(self, outputImageLabel, stateManager):
        super().__init__()
        self.outputImageLabel = outputImageLabel
        self.stateManager = stateManager
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        hbox = QHBoxLayout()

        labelRed = QLabel('Red:', self)
        self.sldRed = QSlider(Qt.Vertical, self)
        self.sldRed.setObjectName("red")
        self.sldRed.setFocusPolicy(Qt.NoFocus)
        self.sldRed.setValue(50)
        self.sldRed.valueChanged.connect(self.changeValue)

        labelGreen = QLabel('Blue:', self)
        self.sldGreen = QSlider(Qt.Vertical, self)
        self.sldGreen.setObjectName("green")
        self.sldGreen.setFocusPolicy(Qt.NoFocus)
        self.sldGreen.setValue(50)
        self.sldGreen.valueChanged.connect(self.changeValue)

        labelBlue = QLabel('Green:', self)
        self.sldBlue = QSlider(Qt.Vertical, self)
        self.sldBlue.setObjectName("blue")
        self.sldBlue.setFocusPolicy(Qt.NoFocus)
        self.sldBlue.setValue(50)
        self.sldBlue.valueChanged.connect(self.changeValue)

        hbox.addWidget(labelRed)
        hbox.addWidget(self.sldRed)
        hbox.addSpacing(15)

        hbox.addWidget(labelGreen)
        hbox.addWidget(self.sldGreen)
        hbox.addSpacing(15)

        hbox.addWidget(labelBlue)
        hbox.addWidget(self.sldBlue)
        hbox.addSpacing(15)

        self.setLayout(hbox)

        self.setWindowTitle('Color Balance')
        self.show()

    def changeValue(self, value):
        channel = 2

        if self.sender().objectName() == "red":
            channel = 0
        elif self.sender().objectName() == "blue":
            channel = 1

        if self.stateManager.outputSource != '':
            inputImage = QImageToCvMat(self.stateManager.outputSource)
        else:
            inputImage = imread(self.stateManager.inputSource)

        outputImage = inputImage
        if value > 50:
            increaseSize = (255 // 50) * (value - 50)
            for i in range(inputImage.shape[0]):
                for j in range(inputImage.shape[1]):
                    pixel = inputImage[i, j][channel]
                    if pixel + increaseSize >= 255:
                        outputImage[i, j][channel] = 255
                    else:
                        outputImage[i, j][channel] = pixel + increaseSize
        if value < 50:
            decreaseSize = (255 // 50) * (50 - value)
            for i in range(inputImage.shape[0]):
                for j in range(inputImage.shape[1]):
                    pixel = inputImage[i, j][channel]
                    if pixel - decreaseSize <= 0:
                        outputImage[i, j][channel] = 0
                    else:
                        outputImage[i, j][channel] = pixel - decreaseSize

        outputQImage = qimage2ndarray.array2qimage(inputImage, normalize=True)
        self.outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        self.stateManager.imageOperation(
            outputQImage)


def main():
    app = QApplication(sys.argv)
    ex = colorBalance()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
