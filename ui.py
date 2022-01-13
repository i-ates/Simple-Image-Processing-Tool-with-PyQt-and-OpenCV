from PyQt5 import QtCore, QtGui, QtWidgets
from stateManager import StateManager
from operations import Operations, checkInputPhotoExist, warnMessage
from cropImage import cropImage
from colorBalance import colorBalance
from brightnessContrastSaturation import  brightnessContrastSaturation


class Ui_MainWindow(object):
    def __init__(self):
        self.w = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        stateManager = StateManager()

        MainWindow.resize(1400, 800)
        self.actionOpen_Source = QtWidgets.QAction(MainWindow)
        self.actionOpen_Source.setObjectName(u"actionOpen_Source")
        self.actionSave_Output = QtWidgets.QAction(MainWindow)
        self.actionSave_Output.setObjectName(u"actionSave_Output")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionBlur_Image = QtWidgets.QAction(MainWindow)
        self.actionBlur_Image.setObjectName(u"actionBlur_Image")
        self.actionGray_Image = QtWidgets.QAction(MainWindow)
        self.actionGray_Image.setObjectName(u"actionGray_Image")
        self.actionColor_Balance = QtWidgets.QAction(MainWindow)
        self.actionColor_Balance.setObjectName(u"actionColor_Balance")
        self.actionDeBlur_Image = QtWidgets.QAction(MainWindow)
        self.actionDeBlur_Image.setObjectName(u"actionDeBlur_Image")
        self.actionCrop_Image = QtWidgets.QAction(MainWindow)
        self.actionCrop_Image.setObjectName(u"actionCrop_Image")
        self.actionFlip_Image = QtWidgets.QAction(MainWindow)
        self.actionFlip_Image.setObjectName(u"actionFlip_Image")
        self.actionMirror_Image = QtWidgets.QAction(MainWindow)
        self.actionMirror_Image.setObjectName(u"actionMirror_Image")
        self.actionReverse_Image = QtWidgets.QAction(MainWindow)
        self.actionReverse_Image.setObjectName(u"actionReverse_Image")
        self.actionAdd_Noise = QtWidgets.QAction(MainWindow)
        self.actionAdd_Noise.setObjectName(u"actionAdd_Noise")
        self.actionEdge_Detection = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection.setObjectName(u"actionEdge_Detection")
        self.actionRotate_Image = QtWidgets.QAction(MainWindow)
        self.actionRotate_Image.setObjectName(u"actionRotate_Image")
        self.actionBrightness_Contrast_Saturation = QtWidgets.QAction(MainWindow)
        self.actionBrightness_Contrast_Saturation.setObjectName(u"actionBrightness_Contrast_Saturation")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QtCore.QRect(0, 0, 1350, 775))
        self.background.setPixmap(QtGui.QPixmap(u"Background.png"))
        self.background.setScaledContents(True)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1350, 775))
        self.verticalApp = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalApp.setObjectName(u"verticalApp")
        self.verticalApp.setContentsMargins(0, 0, 0, 0)
        self.horizontalPhotos = QtWidgets.QHBoxLayout()
        self.horizontalPhotos.setObjectName(u"horizontalPhotos")
        self.sourceImage = QtWidgets.QLabel(self.layoutWidget)
        self.sourceImage.setObjectName(u"sourceImage")
        self.sourceImage.setMinimumSize(QtCore.QSize(700, 700))
        self.sourceImage.setMaximumSize(QtCore.QSize(700, 700))
        self.sourceImage.setScaledContents(True)

        self.horizontalPhotos.addWidget(self.sourceImage)

        self.outputImage = QtWidgets.QLabel(self.layoutWidget)
        self.outputImage.setObjectName(u"outputImage")
        self.outputImage.setPixmap(QtGui.QPixmap(u"images/output.png"))
        self.outputImage.setMinimumSize(QtCore.QSize(700, 700))
        self.outputImage.setMaximumSize(QtCore.QSize(700, 700))
        self.outputImage.setScaledContents(True)

        self.horizontalPhotos.addWidget(self.outputImage)

        self.verticalApp.addLayout(self.horizontalPhotos)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 20))
        self.menuImage_Operations = QtWidgets.QMenu(self.menubar)
        self.menuImage_Operations.setObjectName(u"menuImage_Operations")
        self.menuImage_Operations.setEnabled(True)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage_Operations.menuAction())
        self.menuImage_Operations.addAction(self.actionBlur_Image)
        self.menuImage_Operations.addAction(self.actionDeBlur_Image)
        self.menuImage_Operations.addAction(self.actionGray_Image)
        self.menuImage_Operations.addAction(self.actionCrop_Image)
        self.menuImage_Operations.addAction(self.actionFlip_Image)
        self.menuImage_Operations.addAction(self.actionMirror_Image)
        self.menuImage_Operations.addAction(self.actionReverse_Image)
        self.menuImage_Operations.addAction(self.actionColor_Balance)
        self.menuImage_Operations.addAction(self.actionAdd_Noise)
        self.menuImage_Operations.addAction(self.actionEdge_Detection)
        self.menuImage_Operations.addAction(self.actionRotate_Image)
        self.menuImage_Operations.addAction(self.actionBrightness_Contrast_Saturation)
        self.menuFile.addAction(self.actionOpen_Source)
        self.menuFile.addAction(self.actionSave_Output)
        self.menuFile.addAction(self.actionExit)

        self.actionOpen_Source.triggered.connect(lambda:
                                                 Operations.openSource(self.sourceImage,
                                                                       stateManager, self.outputImage))
        self.actionSave_Output.triggered.connect(lambda:
                                                 Operations.saveImageAs(stateManager))
        self.actionGray_Image.triggered.connect(lambda:
                                                Operations.rgbToGrayscale(self.outputImage, stateManager))
        self.actionEdge_Detection.triggered.connect(lambda:
                                                    Operations.Roberts(self.outputImage, stateManager))
        self.actionBlur_Image.triggered.connect(lambda:
                                                Operations.blurImage(self.outputImage, stateManager))
        self.actionFlip_Image.triggered.connect(lambda:
                                                Operations.flipImage(self.outputImage, stateManager))
        self.actionMirror_Image.triggered.connect(lambda:
                                                  Operations.mirrorImage(self.outputImage, stateManager))
        self.actionRotate_Image.triggered.connect(lambda:
                                                  Operations.rotateImage(self.outputImage, stateManager))
        self.actionCrop_Image.triggered.connect(lambda:
                                                self.cropImageWindow(self.outputImage, stateManager))
        self.actionReverse_Image.triggered.connect(lambda:
                                                   Operations.reverseColor(self.outputImage, stateManager))
        self.actionAdd_Noise.triggered.connect(lambda:
                                               Operations.addNoise(self.outputImage, stateManager))
        self.actionColor_Balance.triggered.connect(lambda:
                                                   self.colorBalanceWindow(self.outputImage, stateManager))
        self.actionDeBlur_Image.triggered.connect(lambda:
                                                  Operations.deBlur(self.outputImage, stateManager))
        self.actionBrightness_Contrast_Saturation.triggered.connect(lambda:
                                                                   self.brightnessContrastSaturationWindow(self.outputImage, stateManager))
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Source.setText(QtCore.QCoreApplication.translate("MainWindow", u"Open Source", None))
        self.actionSave_Output.setText(QtCore.QCoreApplication.translate("MainWindow", u"Save Output", None))
        self.actionExit.setText(QtCore.QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionBlur_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Blur Image", None))
        self.actionGray_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Gray Image", None))
        self.actionColor_Balance.setText(QtCore.QCoreApplication.translate("MainWindow", u"Color Balance", None))
        self.actionDeBlur_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"DeBlur Image", None))
        self.actionCrop_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Crop Image", None))
        self.actionFlip_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Flip Image", None))
        self.actionMirror_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Mirror Image", None))
        self.actionReverse_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Reverse Image Color", None))
        self.actionAdd_Noise.setText(QtCore.QCoreApplication.translate("MainWindow", u"Add Noise", None))
        self.actionEdge_Detection.setText(QtCore.QCoreApplication.translate("MainWindow", u"Edge Detection", None))
        self.actionRotate_Image.setText(QtCore.QCoreApplication.translate("MainWindow", u"Rotate Image", None))
        self.actionBrightness_Contrast_Saturation.setText(QtCore.QCoreApplication.translate("MainWindow", u"Brightness/Contrast/Saturation",None))
        self.background.setText("")
        self.sourceImage.setText("")
        self.outputImage.setText("")
        self.menuImage_Operations.setTitle(QtCore.QCoreApplication.translate("MainWindow", u"Image Operations", None))
        self.menuFile.setTitle(QtCore.QCoreApplication.translate("MainWindow", u"File", None))

    # retranslateUi

    def cropImageWindow(self, outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            self.w = cropImage(outputImageLabel, stateManager)
            self.w.show()
        else:
            warnMessage("Please open a image!")


    def colorBalanceWindow(self, outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            self.w = colorBalance(outputImageLabel, stateManager)
            self.w.show()
        else:
            warnMessage("Please open a image!")

    def brightnessContrastSaturationWindow(self, outputImageLabel, stateManager):
        if checkInputPhotoExist(stateManager):
            self.w = brightnessContrastSaturation(outputImageLabel, stateManager)
            self.w.show()
        else:
            warnMessage("Please open a image!")

