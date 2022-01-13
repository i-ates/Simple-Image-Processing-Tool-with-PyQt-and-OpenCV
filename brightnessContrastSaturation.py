import numpy as np
import qimage2ndarray
from PIL import Image, ImageEnhance
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
import sys
from skimage.io import imread
from operations import QImageToCvMat

class brightnessContrastSaturation(QWidget):

    def __init__(self, outputImageLabel, stateManager):
        super().__init__()
        self.outputImageLabel = outputImageLabel
        self.stateManager = stateManager
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        hbox = QHBoxLayout()

        labelBrightness = QLabel('Brightness:', self)
        self.sldBrightness = QSlider(Qt.Vertical, self)
        self.sldBrightness.setObjectName("brightness")
        self.sldBrightness.setFocusPolicy(Qt.NoFocus)
        self.sldBrightness.setValue(50)
        self.sldBrightness.valueChanged.connect(self.changeValue)

        labelContrast = QLabel('Contrast:', self)
        self.sldContrast = QSlider(Qt.Vertical, self)
        self.sldContrast.setObjectName("contrast")
        self.sldContrast.setFocusPolicy(Qt.NoFocus)
        self.sldContrast.setValue(50)
        self.sldContrast.valueChanged.connect(self.changeValue)

        labelSaturation = QLabel('Saturation:', self)
        self.sldSaturation = QSlider(Qt.Vertical, self)
        self.sldSaturation.setObjectName("saturation")
        self.sldSaturation.setFocusPolicy(Qt.NoFocus)
        self.sldSaturation.setValue(50)
        self.sldSaturation.valueChanged.connect(self.changeValue)

        hbox.addWidget(labelBrightness)
        hbox.addWidget(self.sldBrightness)
        hbox.addSpacing(15)

        hbox.addWidget(labelContrast)
        hbox.addWidget(self.sldContrast)
        hbox.addSpacing(15)

        hbox.addWidget(labelSaturation)
        hbox.addWidget(self.sldSaturation)
        hbox.addSpacing(15)

        self.setLayout(hbox)

        self.setWindowTitle('Brightness & Contrast & Saturation')
        self.show()

    def changeValue(self, value):
        channel =1

        if self.sender().objectName() == "brightness":
            channel = 2
        elif self.sender().objectName() == "contrast":
            channel = 0

        if self.stateManager.outputSource != '':
            inputImage = QImageToCvMat(self.stateManager.outputSource)
        else:
            inputImage = imread(self.stateManager.inputSource)
        pilImage = Image.fromarray(np.uint8(inputImage)).convert('RGB')

        if channel == 2:
            enhancer = ImageEnhance.Brightness(pilImage)
        elif channel == 0:
            enhancer = ImageEnhance.Contrast(pilImage)
        else:
            enhancer = ImageEnhance.Color(pilImage)

        if value > 50:
            inputImage = enhancer.enhance(1.1)
        if value < 50:
            inputImage = enhancer.enhance(0.5)

        outputImage = np.array(inputImage.getdata()).reshape(inputImage.size[0], inputImage.size[1], 3)
        outputQImage = qimage2ndarray.array2qimage(outputImage, normalize=True)
        self.outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
        self.stateManager.imageOperation(
            outputQImage)


def main():
    app = QApplication(sys.argv)
    ex = brightnessContrastSaturation()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
