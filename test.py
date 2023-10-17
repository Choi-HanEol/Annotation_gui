import sys
import cv2
import os, glob
from PySide6.QtWidgets import *
# from PySide6 import uic
# from ui_mainwindow import Ui_MainWindow
from ui_mainwindow_after import Ui_MainWindow
from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# form_class = uic.loadUiType("mainwindow.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI('', '')

    def initUI(self, face_image_paths, body_image_paths):
        self.face_image_paths = face_image_paths
        self.body_image_paths = body_image_paths
        self.current_image_index = 0    #현재 보고있는 이미지의 인덱스, t번째 이미지
        # # 스크롤바 구현
        # self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
        # self.scrollbar.valueChanged.connect(self.changeImage)

        # self.loadImage(self.current_image_index)
        self.line_5.setStyleSheet("background-color: red;")
        #open버튼 클릭 시
        self.face_open_button.clicked.connect(lambda: self.convertToImage('face'))
        self.body_open_button.clicked.connect(lambda: self.convertToImage('body'))
    
        
        # 스크롤바 구현
        self.loadImage(self.current_image_index)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A: #스페이스바도 할 수 있으면 하자. 방향키 왼쪽
            if self.current_image_index > 0:
                self.current_image_index -= 1
                
        elif event.key() == Qt.Key_D: #백스페이스바도 할 수 있으면 하자. 방향키 오른쪽
            if self.current_image_index < len(self.face_image_paths) - 1:
                self.current_image_index += 1
                

    def loadImage(self, index):
        self.body_image_paths = ['./images/image1.jpg', './images/image1.jpg', './images/image3.jpg', './images/image4.jpg' ,'./images/image5.jpg' ,'./images/image6.jpg']
        self.face_image_paths = ['./images/image1.jpg', './images/image1.jpg', './images/image3.jpg', './images/image4.jpg' ,'./images/image5.jpg' ,'./images/image6.jpg']
        if 0 <= index < len(self.face_image_paths): 
            #face
            pixmap_t1 = QPixmap(self.face_image_paths[index-1]) if index != 0 else QPixmap()
            self.t_1_faceimage.setPixmap(pixmap_t1)
            self.t_1_faceimage.setScaledContents(True)
            pixmap_t2 = QPixmap(self.face_image_paths[index])
            self.t_2_faceimage.setPixmap(pixmap_t2)
            self.t_2_faceimage.setScaledContents(True)
            pixmap_t3 = QPixmap(self.face_image_paths[index+1]) if index+1 != len(self.face_image_paths) else QPixmap()
            self.t_3_faceimage.setPixmap(pixmap_t3)
            self.t_3_faceimage.setScaledContents(True)
            #body
            pixmap_t1 = QPixmap(self.body_image_paths[index-1]) if index != 0 else QPixmap()
            self.t_1_bodyimage.setPixmap(pixmap_t1)
            self.t_1_bodyimage.setScaledContents(True)
            pixmap_t2 = QPixmap(self.body_image_paths[index])
            self.t_2_bodyimage.setPixmap(pixmap_t2)
            self.t_2_bodyimage.setScaledContents(True)
            pixmap_t3 = QPixmap(self.body_image_paths[index+1]) if index+1 != len(self.body_image_paths) else QPixmap()
            self.t_3_bodyimage.setPixmap(pixmap_t3)
            self.t_3_bodyimage.setScaledContents(True)
            
    
    def changeImage(self, value):
        self.current_image_index = value
        self.loadImage(self.current_image_index)

if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    face_image_paths = []#["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg", "image6.jpg"]
    body_image_paths = []#["image6.jpg", "image5.jpg", "image4.jpg", "image3.jpg", "image2.jpg", "image1.jpg"]
    #WindowClass의 인스턴스 생성
    # myWindow = WindowClass(face_image_paths, body_image_paths)
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()