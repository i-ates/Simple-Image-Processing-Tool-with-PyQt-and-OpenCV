from PyQt5 import QtWidgets


class StateManager(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.inputSource = ''
        self.outputSource = ''

    def importImage(self, inputPath):
        self.inputSource = inputPath

    def imageOperation(self, newImage):
        self.outputSource = newImage
