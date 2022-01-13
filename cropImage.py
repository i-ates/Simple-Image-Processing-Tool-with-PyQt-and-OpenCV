from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QRubberBand, QLabel
from PyQt5.QtCore import QRect


class cropImage(QLabel):
    def __init__(self, outputImageLabel, stateManager, parentQWidget=None):
        super(cropImage, self).__init__(parentQWidget)
        self.initUI(stateManager)
        self.stateManager = stateManager
        self.outputImageLabel = outputImageLabel

    def initUI(self, stateManager):
        if stateManager.outputSource != '':
            inputImage = QtGui.QPixmap(stateManager.outputSource)
        else:
            inputImage = QtGui.QPixmap(stateManager.inputSource)
        self.setWindowTitle("Crop Image")
        self.setPixmap(inputImage)

    def mousePressEvent(self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent(self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent(self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        cropQPixmap = self.pixmap().copy(currentQRect)
        self.outputImageLabel.setPixmap(QtGui.QPixmap(cropQPixmap))
        self.stateManager.imageOperation(
            cropQPixmap.toImage())
