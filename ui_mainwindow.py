# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_afterAcQsLp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QScrollBar)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1407, 840)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        # self.line_9.setLineWidth(50)

        self.verticalLayout_3.addWidget(self.line_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.face_open_button = QPushButton(self.centralwidget)
        self.face_open_button.setObjectName(u"face_open_button")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.face_open_button.sizePolicy().hasHeightForWidth())
        self.face_open_button.setSizePolicy(sizePolicy)
        self.face_open_button.setMinimumSize(QSize(80, 80))
        self.face_open_button.setMaximumSize(QSize(110, 110))
        self.face_open_button.setSizeIncrement(QSize(0, 0))
        self.face_open_button.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setKerning(True)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.face_open_button.setFont(font1)
        self.face_open_button.setStyleSheet(u"")
        self.face_open_button.setIconSize(QSize(50, 50))
        self.face_open_button.setCheckable(False)
        self.face_open_button.setAutoDefault(False)

        self.verticalLayout.addWidget(self.face_open_button)

        self.face_FileList_button = QPushButton(self.centralwidget)
        self.face_FileList_button.setObjectName(u"face_FileList_button")
        sizePolicy.setHeightForWidth(self.face_FileList_button.sizePolicy().hasHeightForWidth())
        self.face_FileList_button.setSizePolicy(sizePolicy)
        self.face_FileList_button.setMinimumSize(QSize(80, 80))
        self.face_FileList_button.setMaximumSize(QSize(110, 110))
        self.face_FileList_button.setSizeIncrement(QSize(0, 0))
        self.face_FileList_button.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.face_FileList_button.setFont(font2)

        self.verticalLayout.addWidget(self.face_FileList_button)

        self.face_DataAug_button = QPushButton(self.centralwidget)
        self.face_DataAug_button.setObjectName(u"face_DataAug_button")
        sizePolicy.setHeightForWidth(self.face_DataAug_button.sizePolicy().hasHeightForWidth())
        self.face_DataAug_button.setSizePolicy(sizePolicy)
        self.face_DataAug_button.setMinimumSize(QSize(80, 80))
        self.face_DataAug_button.setMaximumSize(QSize(110, 110))
        self.face_DataAug_button.setSizeIncrement(QSize(0, 0))
        self.face_DataAug_button.setBaseSize(QSize(0, 0))
        self.face_DataAug_button.setFont(font2)

        self.verticalLayout.addWidget(self.face_DataAug_button)

        self.face_Delete_button = QPushButton(self.centralwidget)
        self.face_Delete_button.setObjectName(u"face_Delete_button")
        sizePolicy.setHeightForWidth(self.face_Delete_button.sizePolicy().hasHeightForWidth())
        self.face_Delete_button.setSizePolicy(sizePolicy)
        self.face_Delete_button.setMinimumSize(QSize(80, 80))
        self.face_Delete_button.setMaximumSize(QSize(110, 110))
        self.face_Delete_button.setSizeIncrement(QSize(0, 0))
        self.face_Delete_button.setBaseSize(QSize(0, 0))
        self.face_Delete_button.setFont(font2)

        self.verticalLayout.addWidget(self.face_Delete_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_8)

        self.t_1_faceimage = QLabel(self.centralwidget)
        self.t_1_faceimage.setObjectName(u"t_1_faceimage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.t_1_faceimage.sizePolicy().hasHeightForWidth())
        self.t_1_faceimage.setSizePolicy(sizePolicy1)
        self.t_1_faceimage.setMinimumSize(QSize(420, 250))
        self.t_1_faceimage.setMaximumSize(QSize(590, 400))
        self.t_1_faceimage.setAlignment(Qt.AlignCenter)
        self.t_1_faceimage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.t_1_faceimage)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        

        self.horizontalLayout_2.addWidget(self.line_3)

        self.t_2_faceimage = QLabel(self.centralwidget)
        self.t_2_faceimage.setObjectName(u"t_2_faceimage")
        sizePolicy1.setHeightForWidth(self.t_2_faceimage.sizePolicy().hasHeightForWidth())
        self.t_2_faceimage.setSizePolicy(sizePolicy1)
        self.t_2_faceimage.setMinimumSize(QSize(420, 250))
        self.t_2_faceimage.setMaximumSize(QSize(590, 400))
        self.t_2_faceimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.t_2_faceimage)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        # self.line_4.setLineWidth(50)
        

        self.horizontalLayout_2.addWidget(self.line_4)

        self.t_3_faceimage = QLabel(self.centralwidget)
        self.t_3_faceimage.setObjectName(u"t_3_faceimage")
        sizePolicy1.setHeightForWidth(self.t_3_faceimage.sizePolicy().hasHeightForWidth())
        self.t_3_faceimage.setSizePolicy(sizePolicy1)
        self.t_3_faceimage.setMinimumSize(QSize(420, 250))
        self.t_3_faceimage.setMaximumSize(QSize(590, 400))
        self.t_3_faceimage.setAlignment(Qt.AlignCenter)
        self.t_3_faceimage.setMargin(20)

        self.horizontalLayout_2.addWidget(self.t_3_faceimage)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.body_open_button = QPushButton(self.centralwidget)
        self.body_open_button.setObjectName(u"body_open_button")
        sizePolicy.setHeightForWidth(self.body_open_button.sizePolicy().hasHeightForWidth())
        self.body_open_button.setSizePolicy(sizePolicy)
        self.body_open_button.setMinimumSize(QSize(80, 80))
        self.body_open_button.setMaximumSize(QSize(110, 110))
        self.body_open_button.setSizeIncrement(QSize(0, 0))
        self.body_open_button.setBaseSize(QSize(0, 0))
        self.body_open_button.setFont(font1)
        self.body_open_button.setStyleSheet(u"border-image:url(\"C/Users/USER/Desktop/pyqt5_design/images/open.png\");")
        self.body_open_button.setIconSize(QSize(50, 50))
        self.body_open_button.setCheckable(False)
        self.body_open_button.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.body_open_button)

        self.body_delete_button = QPushButton(self.centralwidget)
        self.body_delete_button.setObjectName(u"body_delete_button")
        sizePolicy.setHeightForWidth(self.body_delete_button.sizePolicy().hasHeightForWidth())
        self.body_delete_button.setSizePolicy(sizePolicy)
        self.body_delete_button.setMinimumSize(QSize(80, 80))
        self.body_delete_button.setMaximumSize(QSize(110, 110))
        self.body_delete_button.setSizeIncrement(QSize(0, 0))
        self.body_delete_button.setBaseSize(QSize(0, 0))
        self.body_delete_button.setFont(font2)

        self.verticalLayout_2.addWidget(self.body_delete_button)

        self.body_FileList_button = QPushButton(self.centralwidget)
        self.body_FileList_button.setObjectName(u"body_FileList_button")
        sizePolicy.setHeightForWidth(self.body_FileList_button.sizePolicy().hasHeightForWidth())
        self.body_FileList_button.setSizePolicy(sizePolicy)
        self.body_FileList_button.setMinimumSize(QSize(80, 80))
        self.body_FileList_button.setMaximumSize(QSize(110, 110))
        self.body_FileList_button.setSizeIncrement(QSize(0, 0))
        self.body_FileList_button.setBaseSize(QSize(0, 0))
        self.body_FileList_button.setFont(font2)

        self.verticalLayout_2.addWidget(self.body_FileList_button)

        self.body_DataAug_button = QPushButton(self.centralwidget)
        self.body_DataAug_button.setObjectName(u"body_DataAug_button")
        sizePolicy.setHeightForWidth(self.body_DataAug_button.sizePolicy().hasHeightForWidth())
        self.body_DataAug_button.setSizePolicy(sizePolicy)
        self.body_DataAug_button.setMinimumSize(QSize(80, 80))
        self.body_DataAug_button.setMaximumSize(QSize(110, 110))
        self.body_DataAug_button.setSizeIncrement(QSize(0, 0))
        self.body_DataAug_button.setBaseSize(QSize(0, 0))
        self.body_DataAug_button.setFont(font2)

        self.verticalLayout_2.addWidget(self.body_DataAug_button)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_7)

        self.t_1_bodyimage = QLabel(self.centralwidget)
        self.t_1_bodyimage.setObjectName(u"t_1_bodyimage")
        sizePolicy1.setHeightForWidth(self.t_1_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_1_bodyimage.setSizePolicy(sizePolicy1)
        self.t_1_bodyimage.setMinimumSize(QSize(420, 250))
        self.t_1_bodyimage.setMaximumSize(QSize(590, 400))
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
        sizePolicy1.setHeightForWidth(self.t_2_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_2_bodyimage.setSizePolicy(sizePolicy1)
        self.t_2_bodyimage.setMinimumSize(QSize(420, 250))
        self.t_2_bodyimage.setMaximumSize(QSize(590, 400))
        self.t_2_bodyimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.t_2_bodyimage)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        
        self.horizontalLayout_3.addWidget(self.line_6)

        self.t_3_bodyimage = QLabel(self.centralwidget)
        self.t_3_bodyimage.setObjectName(u"t_3_bodyimage")
        sizePolicy1.setHeightForWidth(self.t_3_bodyimage.sizePolicy().hasHeightForWidth())
        self.t_3_bodyimage.setSizePolicy(sizePolicy1)
        self.t_3_bodyimage.setMinimumSize(QSize(420, 250))
        self.t_3_bodyimage.setMaximumSize(QSize(590, 400))
        self.t_3_bodyimage.setAlignment(Qt.AlignCenter)
        self.t_3_bodyimage.setMargin(20)

        self.horizontalLayout_3.addWidget(self.t_3_bodyimage)
        

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.scrollbar = QScrollBar(Qt.Orientation.Horizontal, self)
        self.verticalLayout_3.addWidget(self.scrollbar)
        self.scrollbar.setMaximum(0)
        

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(80, 80))
        self.pushButton.setMaximumSize(QSize(80, 80))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.pushButton.setFont(font3)

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(80, 80))
        self.pushButton_2.setMaximumSize(QSize(80, 80))
        self.pushButton_2.setFont(font2)

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(1040, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy4)
        self.radioButton_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy4.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy4)
        self.radioButton_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy4.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy4)
        self.radioButton_4.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")
        sizePolicy4.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy4)
        self.radioButton_5.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox)
        self.radioButton_6.setObjectName(u"radioButton_6")
        sizePolicy4.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
        self.radioButton_6.setSizePolicy(sizePolicy4)
        self.radioButton_6.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.groupBox)
        self.radioButton_7.setObjectName(u"radioButton_7")
        sizePolicy4.setHeightForWidth(self.radioButton_7.sizePolicy().hasHeightForWidth())
        self.radioButton_7.setSizePolicy(sizePolicy4)
        self.radioButton_7.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.radioButton_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.horizontalLayout_6.addWidget(self.groupBox)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(80, 80))
        self.pushButton_3.setMaximumSize(QSize(80, 80))
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1407, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.face_open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.face_FileList_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.face_DataAug_button.setText(QCoreApplication.translate("MainWindow", u"File List", None))
        self.face_Delete_button.setText(QCoreApplication.translate("MainWindow", u"Data\n"
"Aug", None))
        self.t_1_faceimage.setText("")
        self.t_2_faceimage.setText(QCoreApplication.translate("MainWindow", u"Open the Vedio File", None))
        self.t_3_faceimage.setText("")
        self.body_open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.body_delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.body_FileList_button.setText(QCoreApplication.translate("MainWindow", u"File List", None))
        self.body_DataAug_button.setText(QCoreApplication.translate("MainWindow", u"Data\n"
"Aug", None))
        self.t_1_bodyimage.setText("")
        self.t_2_bodyimage.setText(QCoreApplication.translate("MainWindow", u"Open the Vedio File", None))
        self.t_3_bodyimage.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Prev\n"
"Image", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Annotation", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"-3", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"-2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Next\n"
"Image", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

