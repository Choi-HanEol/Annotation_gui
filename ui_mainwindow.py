# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maxsizedown_mainwindowdTPHJh.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget, QScrollBar)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1407, 840)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.actionOpenVedioFile = QAction(MainWindow)
        self.actionOpenVedioFile.setObjectName(u"actionOpenVedioFile")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpenImageFolder = QAction(MainWindow)
        self.actionOpenImageFolder.setObjectName(u"actionOpenImageFolder")
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionSave_As_2 = QAction(MainWindow)
        self.actionSave_As_2.setObjectName(u"actionSave_As_2")
        self.actionOpenNpyFile = QAction(MainWindow)
        self.actionOpenNpyFile.setObjectName(u"actionOpenNpyFile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_8)

        self.t_1_faceimage = QLabel(self.centralwidget)
        self.t_1_faceimage.setObjectName(u"t_1_faceimage")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_1_faceimage.sizePolicy().hasHeightForWidth())
        self.t_1_faceimage.setSizePolicy(sizePolicy)
        self.t_1_faceimage.setMinimumSize(QSize(224, 166))
        self.t_1_faceimage.setMaximumSize(QSize(400, 250))
        self.t_1_faceimage.setAlignment(Qt.AlignCenter)
        self.t_1_faceimage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.t_1_faceimage)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_10)

        self.t_2_faceimage = QLabel(self.centralwidget)
        self.t_2_faceimage.setObjectName(u"t_2_faceimage")
        sizePolicy.setHeightForWidth(self.t_2_faceimage.sizePolicy().hasHeightForWidth())
        self.t_2_faceimage.setSizePolicy(sizePolicy)
        self.t_2_faceimage.setMinimumSize(QSize(224, 166))
        self.t_2_faceimage.setMaximumSize(QSize(400, 250))
        self.t_2_faceimage.setAlignment(Qt.AlignCenter)
        self.t_2_faceimage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.t_2_faceimage)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.t_3_faceimage = QLabel(self.centralwidget)
        self.t_3_faceimage.setObjectName(u"t_3_faceimage")
        sizePolicy.setHeightForWidth(self.t_3_faceimage.sizePolicy().hasHeightForWidth())
        self.t_3_faceimage.setSizePolicy(sizePolicy)
        self.t_3_faceimage.setMinimumSize(QSize(420, 322))
        self.t_3_faceimage.setMaximumSize(QSize(590, 400))
        self.t_3_faceimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.t_3_faceimage)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_11)

        self.t_4_faceimage = QLabel(self.centralwidget)
        self.t_4_faceimage.setObjectName(u"t_4_faceimage")
        sizePolicy.setHeightForWidth(self.t_4_faceimage.sizePolicy().hasHeightForWidth())
        self.t_4_faceimage.setSizePolicy(sizePolicy)
        self.t_4_faceimage.setMinimumSize(QSize(224, 166))
        self.t_4_faceimage.setMaximumSize(QSize(400, 250))
        self.t_4_faceimage.setAlignment(Qt.AlignCenter)
        self.t_4_faceimage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.t_4_faceimage)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.t_5_faceimage = QLabel(self.centralwidget)
        self.t_5_faceimage.setObjectName(u"t_5_faceimage")
        sizePolicy.setHeightForWidth(self.t_5_faceimage.sizePolicy().hasHeightForWidth())
        self.t_5_faceimage.setSizePolicy(sizePolicy)
        self.t_5_faceimage.setMinimumSize(QSize(224, 166))
        self.t_5_faceimage.setMaximumSize(QSize(400, 250))
        self.t_5_faceimage.setAlignment(Qt.AlignCenter)
        self.t_5_faceimage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.t_5_faceimage)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_7)

        self.t_1_bodyimage = QLabel(self.centralwidget)
        self.t_1_bodyimage.setObjectName(u"t_1_bodyimage")
        sizePolicy.setHeightForWidth(self.t_1_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_1_bodyimage.setSizePolicy(sizePolicy)
        self.t_1_bodyimage.setMinimumSize(QSize(224, 166))
        self.t_1_bodyimage.setMaximumSize(QSize(400, 250))
        self.t_1_bodyimage.setAlignment(Qt.AlignCenter)
        self.t_1_bodyimage.setMargin(20)

        self.horizontalLayout_3.addWidget(self.t_1_bodyimage)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.t_2_bodyimage = QLabel(self.centralwidget)
        self.t_2_bodyimage.setObjectName(u"t_2_bodyimage")
        sizePolicy.setHeightForWidth(self.t_2_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_2_bodyimage.setSizePolicy(sizePolicy)
        self.t_2_bodyimage.setMinimumSize(QSize(224, 166))
        self.t_2_bodyimage.setMaximumSize(QSize(400, 250))
        self.t_2_bodyimage.setAlignment(Qt.AlignCenter)
        self.t_2_bodyimage.setMargin(20)

        self.horizontalLayout_3.addWidget(self.t_2_bodyimage)

        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_12)

        self.t_3_bodyimage = QLabel(self.centralwidget)
        self.t_3_bodyimage.setObjectName(u"t_3_bodyimage")
        sizePolicy.setHeightForWidth(self.t_3_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_3_bodyimage.setSizePolicy(sizePolicy)
        self.t_3_bodyimage.setMinimumSize(QSize(420, 322))
        self.t_3_bodyimage.setMaximumSize(QSize(590, 400))
        self.t_3_bodyimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.t_3_bodyimage)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.t_4_bodyimage = QLabel(self.centralwidget)
        self.t_4_bodyimage.setObjectName(u"t_4_bodyimage")
        sizePolicy.setHeightForWidth(self.t_4_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_4_bodyimage.setSizePolicy(sizePolicy)
        self.t_4_bodyimage.setMinimumSize(QSize(224, 166))
        self.t_4_bodyimage.setMaximumSize(QSize(400, 250))
        self.t_4_bodyimage.setAlignment(Qt.AlignCenter)
        self.t_4_bodyimage.setMargin(20)

        self.horizontalLayout_3.addWidget(self.t_4_bodyimage)

        self.line_13 = QFrame(self.centralwidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_13)

        self.t_5_bodyimage = QLabel(self.centralwidget)
        self.t_5_bodyimage.setObjectName(u"t_5_bodyimage")
        sizePolicy.setHeightForWidth(self.t_5_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_5_bodyimage.setSizePolicy(sizePolicy)
        self.t_5_bodyimage.setMinimumSize(QSize(224, 166))
        self.t_5_bodyimage.setMaximumSize(QSize(400, 250))
        self.t_5_bodyimage.setAlignment(Qt.AlignCenter)
        self.t_5_bodyimage.setMargin(20)

        self.horizontalLayout_3.addWidget(self.t_5_bodyimage)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.scrollbar = QScrollBar(Qt.Orientation.Horizontal, self)
        self.verticalLayout.addWidget(self.scrollbar)
        self.scrollbar.setMaximum(0)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy1)
        self.exportButton.setMinimumSize(QSize(80, 80))
        self.exportButton.setMaximumSize(QSize(80, 80))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.exportButton.setFont(font1)

        self.horizontalLayout_6.addWidget(self.exportButton)

        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setObjectName(u"prevButton")
        sizePolicy1.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
        self.prevButton.setSizePolicy(sizePolicy1)
        self.prevButton.setMinimumSize(QSize(80, 80))
        self.prevButton.setMaximumSize(QSize(80, 80))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.prevButton.setFont(font2)

        self.horizontalLayout_6.addWidget(self.prevButton)

        self.AnnotationBox = QGroupBox(self.centralwidget)
        self.AnnotationBox.setObjectName(u"AnnotationBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AnnotationBox.sizePolicy().hasHeightForWidth())
        self.AnnotationBox.setSizePolicy(sizePolicy2)
        self.AnnotationBox.setMinimumSize(QSize(600, 0))
        self.AnnotationBox.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.AnnotationBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_8 = QRadioButton(self.AnnotationBox)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.horizontalLayout.addWidget(self.radioButton_8)

        self.radioButton = QRadioButton(self.AnnotationBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.AnnotationBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy3)
        self.radioButton_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.AnnotationBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy3.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy3)
        self.radioButton_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.AnnotationBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy3.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy3)
        self.radioButton_4.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.AnnotationBox)
        self.radioButton_5.setObjectName(u"radioButton_5")
        sizePolicy3.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy3)
        self.radioButton_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.AnnotationBox)
        self.radioButton_6.setObjectName(u"radioButton_6")
        sizePolicy3.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
        self.radioButton_6.setSizePolicy(sizePolicy3)
        self.radioButton_6.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.AnnotationBox)
        self.radioButton_7.setObjectName(u"radioButton_7")
        sizePolicy3.setHeightForWidth(self.radioButton_7.sizePolicy().hasHeightForWidth())
        self.radioButton_7.setSizePolicy(sizePolicy3)
        self.radioButton_7.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.horizontalLayout_6.addWidget(self.AnnotationBox)

        self.AugmentBox = QGroupBox(self.centralwidget)
        self.AugmentBox.setObjectName(u"AugmentBox")
        self.AugmentBox.setMinimumSize(QSize(300, 0))
        self.AugmentBox.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_8 = QHBoxLayout(self.AugmentBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_5 = QCheckBox(self.AugmentBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_7.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.AugmentBox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.horizontalLayout_7.addWidget(self.checkBox_6)

        self.checkBox_4 = QCheckBox(self.AugmentBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_7.addWidget(self.checkBox_4)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_6.addWidget(self.AugmentBox)

        self.prevButton_2 = QPushButton(self.centralwidget)
        self.prevButton_2.setObjectName(u"prevButton_2")
        sizePolicy1.setHeightForWidth(self.prevButton_2.sizePolicy().hasHeightForWidth())
        self.prevButton_2.setSizePolicy(sizePolicy1)
        self.prevButton_2.setMinimumSize(QSize(80, 80))
        self.prevButton_2.setMaximumSize(QSize(130, 80))
        self.prevButton_2.setFont(font2)

        self.horizontalLayout_6.addWidget(self.prevButton_2)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        sizePolicy1.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy1)
        self.nextButton.setMinimumSize(QSize(80, 80))
        self.nextButton.setMaximumSize(QSize(80, 80))
        self.nextButton.setFont(font2)

        self.horizontalLayout_6.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1407, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menusave = QMenu(self.menubar)
        self.menusave.setObjectName(u"menusave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menusave.menuAction())
        self.menuFile.addAction(self.actionOpenVedioFile)
        self.menuFile.addAction(self.actionOpenImageFolder)
        self.menuFile.addAction(self.actionOpenNpyFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionSave_As_2)
        self.menusave.addAction(self.actionSearch)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpenVedioFile.setText(QCoreApplication.translate("MainWindow", u"Open Vedio File", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpenImageFolder.setText(QCoreApplication.translate("MainWindow", u"Open Image Folder", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search (Ctrl + F)", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save (Ctrl + S)", None))
        self.actionSave_As_2.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionOpenNpyFile.setText(QCoreApplication.translate("MainWindow", u"Open npy File (Ctrl + O)", None))
        self.t_1_faceimage.setText("")
        self.t_2_faceimage.setText("")
        self.t_3_faceimage.setText(QCoreApplication.translate("MainWindow", u"Open the Vedio File", None))
        self.t_4_faceimage.setText("")
        self.t_5_faceimage.setText("")
        self.t_1_bodyimage.setText("")
        self.t_2_bodyimage.setText("")
        self.t_3_bodyimage.setText(QCoreApplication.translate("MainWindow", u"Open the Vedio File", None))
        self.t_4_bodyimage.setText("")
        self.t_5_bodyimage.setText("")
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Prev\n"
"Image", None))
        self.AnnotationBox.setTitle(QCoreApplication.translate("MainWindow", u"Annotation", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"-3", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"-2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.AugmentBox.setTitle(QCoreApplication.translate("MainWindow", u"Augmentation", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Flip", None))
        self.prevButton_2.setText(QCoreApplication.translate("MainWindow", u"Run\n"
"Augmentation", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next\n"
"Image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menusave.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

