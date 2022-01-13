import imutils
import numpy as np
from PyQt5.QtWidgets import QMessageBox
from skimage.io import imread
from skimage import filters
from PyQt5 import  QtGui, QtWidgets
import qimage2ndarray
import cv2 as opencv
from skimage.util import random_noise

def QImageToCvMat(incomingImage):
    incomingImage.save('temp.png', 'png')
    mat = opencv.imread('temp.png')
    mat = mat[:, :, ::-1]

    return mat

def warnMessage(message):
    msg = QMessageBox()
    msg.setWindowTitle("WARNING!")
    msg.setText(message)
    msg.exec_()

def checkInputPhotoExist(stateManager):
    if stateManager.inputSource == '':
        return False
    else:
        return True
def checkOutputPhotoExist(stateManager):
    if stateManager.outputSource != '':
        return True
    else:
        return False

class Operations():

    def openSource(imageLabel, stateManager, outputImageLabel):
        dialogMenu = QtWidgets.QDialog()
        sourcePath, _ = QtWidgets.QFileDialog.getOpenFileName(dialogMenu,
                                                              "Open Image", "", "Image (*.jpg *.png)")
        if sourcePath != '':
            imageLabel.setPixmap(QtGui.QPixmap(sourcePath))
            stateManager.importImage(sourcePath)
            stateManager.outputSource = ''
            outputImageLabel.setPixmap(QtGui.QPixmap())

    def saveImageAs(stateManager):
        if checkOutputPhotoExist(stateManager):

            dialogMenu = QtWidgets.QDialog()
            Image = stateManager.outputSource
            fileName = QtWidgets.QFileDialog.getSaveFileName(dialogMenu, "Save File",
                                                             "",
                                                             "Images (*.png *.jpg)")
            Image.save(fileName[0])
        else:
            warnMessage("Output Image can not be null!!")

    def Roberts(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)
            grayImage = opencv.cvtColor(inputImage, opencv.COLOR_BGR2GRAY)
            edgeRoberts = filters.roberts(grayImage)
            outputQImage = qimage2ndarray.array2qimage(
                edgeRoberts, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")
    def rgbToGrayscale(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)

            outputData = opencv.cvtColor(inputImage, opencv.COLOR_BGR2GRAY)
            outputQImage = qimage2ndarray.gray2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")

    def blurImage(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)

            outputData = opencv.blur(inputImage, (5, 5))
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")

    def flipImage(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)

            outputData = opencv.flip(inputImage, 0)
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")


    def mirrorImage(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)

            outputData = opencv.flip(inputImage, 1)
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")


    def rotateImage(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)
            outputData = imutils.rotate(inputImage, 90)
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")

    def reverseColor(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)
            outputData = opencv.bitwise_not(inputImage)
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")

    def addNoise(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)

            outputData = random_noise(inputImage, mode='s&p', amount=0.1)
            outputData = np.array(255 * outputData, dtype='uint8')
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")

    def deBlur(outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            if stateManager.outputSource != '':
                inputImage = QImageToCvMat(stateManager.outputSource)
            else:
                inputImage = imread(stateManager.inputSource)

            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            outputData = opencv.filter2D(src=inputImage, ddepth=-1, kernel=kernel)
            outputQImage = qimage2ndarray.array2qimage(outputData, normalize=True)
            outputImageLabel.setPixmap(QtGui.QPixmap(outputQImage))
            stateManager.imageOperation(
                outputQImage)
        else:
            warnMessage("Please open a image!")
