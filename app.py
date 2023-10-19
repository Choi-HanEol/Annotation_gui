import sys
import cv2
import os, glob
import numpy as np
import pandas as pd
from PySide6.QtWidgets import *
# from PySide6 import uic
# from ui_mainwindow import Ui_MainWindow
from ui_maxsizedown_mainwindow import Ui_MainWindow
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
        file_list = ['face', 'body']
        self.face_image_paths = face_image_paths
        self.body_image_paths = body_image_paths
        self.current_image_index = -1    #현재 보고있는 이미지의 인덱스, t번째 이미지
        self.annotateList = 0   #anntate리스트 초기화
        # 그룹 재정의
        self.group = QButtonGroup()
        # self.group.setExclusive(False) 
        # self.radioButton = QRadioButton()
        self.group.addButton(self.radioButton)
        # self.radioButton_2 = QRadioButton()
        self.group.addButton(self.radioButton_2)
        # self.radioButton_3 = QRadioButton()
        self.group.addButton(self.radioButton_3)
        # self.radioButton = QRadioButton()
        self.group.addButton(self.radioButton_4)
        # self.radioButton = QRadioButton()
        self.group.addButton(self.radioButton_5)
        # self.radioButton = QRadioButton()
        self.group.addButton(self.radioButton_6)
        # self.radioButton = QRadioButton()
        self.group.addButton(self.radioButton_7)

        # # 스크롤바 구현
        # self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
        # self.scrollbar.valueChanged.connect(self.changeImage)
        self.line_3.setStyleSheet("background-color: red;")
        self.line_11.setStyleSheet("background-color: red;")
        self.line_6.setStyleSheet("background-color: red;")
        self.line_12.setStyleSheet("background-color: red;")
        
        # self.loadImage(self.current_image_index)
        #open버튼 클릭 시
        # self.face_open_button.clicked.connect(lambda: self.convertToImage('face'))
        # self.body_open_button.clicked.connect(lambda: self.convertToImage('body'))
        self.actionOpenVedioFile.triggered.connect(lambda: self.convertToImage(file_list))
        self.actionSearch.triggered.connect(self.show_search_dialog)
        
        # Data Annotation
        self.radioButton.toggled.connect(self.annotateData)
        self.radioButton_2.toggled.connect(self.annotateData)
        self.radioButton_3.toggled.connect(self.annotateData)
        self.radioButton_4.toggled.connect(self.annotateData)
        self.radioButton_5.toggled.connect(self.annotateData)
        self.radioButton_6.toggled.connect(self.annotateData)
        self.radioButton_7.toggled.connect(self.annotateData)

        # CSV로 저장
        self.exportButton.clicked.connect(self.exportToCsv)

        # prev, next 버튼클릭
        self.prevButton.clicked.connect(self.clickedPrev)
        self.nextButton.clicked.connect(self.clickedNext)



    def clickedPrev(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.scrollbar.setValue(self.current_image_index)

    def clickedNext(self):
        if self.current_image_index < len(self.face_image_paths) - 1:
                self.current_image_index += 1
                self.scrollbar.setValue(self.current_image_index)
        

    def exportToCsv(self):
        if self.current_image_index < 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("알림")
            msg_box.setText("파일을 먼저 선택하세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        else:
            reply = QMessageBox.question(self, '알림', '현재까지 한 작업을 csv로 저장하시겠습니까?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if np.all(np.isnan(self.annotateList)):
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("알림")
                    msg_box.setText("Annotation이 진행되지 않았습니다.")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec()
                else:
                    csv_df = pd.DataFrame(self.annotateList, columns=['Frame Number', 'Level Value'])
                    csv_df.to_csv('result.csv', index=False)
    

    def annotateData(self):
        if self.radioButton.isChecked():
            annotate_value = -3
        elif self.radioButton_2.isChecked():
            annotate_value = -2
        elif self.radioButton_3.isChecked():
            annotate_value = -1
        elif self.radioButton_4.isChecked():
            annotate_value = 0
        elif self.radioButton_5.isChecked():
            annotate_value = 1
        elif self.radioButton_6.isChecked():
            annotate_value = 2
        elif self.radioButton_7.isChecked():
            annotate_value = 3

        self.annotateList[self.current_image_index] = [self.current_image_index+1, annotate_value]
        


    def show_search_dialog(self):
        if self.current_image_index < 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("알림")
            msg_box.setText("파일을 먼저 선택하세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        else:
            text, ok = QInputDialog.getText(self, '검색', f'찾으실 이미지를 입력하세요 (1~{self.scrollbar.maximum()+1})')
            
            if ok:
                self.changeImage(int(text)-1)
                self.scrollbar.setValue(self.current_image_index)
            self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')


    def convertToImage(self, file_list): #동영상 열어 이미지로 변환
        global video_name
        
        for faceOrBody in file_list:
            
            video_name = QFileDialog.getOpenFileName(self, 'Open File')
            
            if os.path.splitext(video_name[0])[1].lower() == '.mp4': #선택한 파일이 동영상일 때
                self.current_image_index = 0
                
                self.annotateList = np.full((len(self.face_image_paths), 2) ,np.nan)
                cap = cv2.VideoCapture(video_name[0])
                folder_path = os.path.dirname(video_name[0])+'/'+faceOrBody
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f'{folder_path} 폴더가 생성되었습니다.')
                
                # 프레임 수 초기화
                    frame_count = 0

                    while True:
                        # 프레임 읽기
                        ret, frame = cap.read()
                        
                        # 동영상 끝에 도달하면 종료
                        if not ret:
                            break
                        
                        # 이미지 파일로 저장
                        image_filename = f'frame_{frame_count:04d}.jpg'
                        cv2.imwrite(folder_path+'/'+image_filename, frame)
                    
                        # 다음 프레임으로 이동
                        frame_count += 1
                else:
                    print(f'{folder_path} 폴더는 이미 존재합니다.')

                if faceOrBody == 'face':
                    self.face_image_paths = glob.glob(os.path.join(folder_path, '*.jpg'))
                elif faceOrBody == 'body':
                    self.body_image_paths = glob.glob(os.path.join(folder_path, '*.jpg'))
                else:
                    print('file_list 에러')
                # 동영상 캡처 객체 해제
                cap.release()
                cv2.destroyAllWindows()
            # elif os.path.splitext(video_name[0])[1].lower() == '':
            #     print('File selection canceled')
            else:
                if os.path.splitext(video_name[0])[1].lower() != '':
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("알림")
                    msg_box.setText("mp4 파일을 선택해야 합니다.")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec()
        
        # 스크롤바 구현
        self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
        self.scrollbar.valueChanged.connect(self.changeImage)
        self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')
        self.loadImage(self.current_image_index)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A: #스페이스바도 할 수 있으면 하자. 방향키 왼쪽
            if self.current_image_index > 0:
                self.current_image_index -= 1
                self.scrollbar.setValue(self.current_image_index)
        elif event.key() == Qt.Key_D: #백스페이스바도 할 수 있으면 하자. 방향키 오른쪽
            if self.current_image_index < len(self.face_image_paths) - 1:
                self.current_image_index += 1
                self.scrollbar.setValue(self.current_image_index)
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_F: 
            self.show_search_dialog()


    def loadImage(self, index):
        # face_image_paths
        if 0 <= index < len(self.face_image_paths): 
            #face
            pixmap_t3 = QPixmap(self.face_image_paths[index])
            self.t_3_faceimage.setPixmap(pixmap_t3)
            self.t_3_faceimage.setScaledContents(True)
            # print(type(pixmap_t3.width()), pixmap_t3.height())
            if index > 1:
                pixmap_t1 = QPixmap(self.face_image_paths[index-2]) 
            else:
                pixmap_t1 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t1.fill(Qt.transparent)            
            self.t_1_faceimage.setPixmap(pixmap_t1)
            self.t_1_faceimage.setScaledContents(True)

            if index > 0:
                pixmap_t2 = QPixmap(self.face_image_paths[index-1]) 
            else:
                pixmap_t2 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t2.fill(Qt.transparent)            
            self.t_2_faceimage.setPixmap(pixmap_t2)
            self.t_2_faceimage.setScaledContents(True)

            if index+1 < len(self.face_image_paths):
                pixmap_t4 = QPixmap(self.face_image_paths[index+1])
            else:
                pixmap_t4 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t4.fill(Qt.transparent)                         
            self.t_4_faceimage.setPixmap(pixmap_t4)
            self.t_4_faceimage.setScaledContents(True)

            if index+2 < len(self.face_image_paths):
                pixmap_t5 = QPixmap(self.face_image_paths[index+2])
            else:
                pixmap_t5 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t5.fill(Qt.transparent)            
            self.t_5_faceimage.setPixmap(pixmap_t5)
            self.t_5_faceimage.setScaledContents(True)

            #body
            pixmap_t3 = QPixmap(self.body_image_paths[index])
            self.t_3_bodyimage.setPixmap(pixmap_t3)
            self.t_3_bodyimage.setScaledContents(True)
            # print(type(pixmap_t3.width()), pixmap_t3.height())
            if index > 1:
                pixmap_t1 = QPixmap(self.body_image_paths[index-2]) 
            else:
                pixmap_t1 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t1.fill(Qt.transparent)            
            self.t_1_bodyimage.setPixmap(pixmap_t1)
            self.t_1_bodyimage.setScaledContents(True)

            if index > 0:
                pixmap_t2 = QPixmap(self.body_image_paths[index-1]) 
            else:
                pixmap_t2 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t2.fill(Qt.transparent)            
            self.t_2_bodyimage.setPixmap(pixmap_t2)
            self.t_2_bodyimage.setScaledContents(True)

            if index+1 < len(self.body_image_paths):
                pixmap_t4 = QPixmap(self.body_image_paths[index+1])
            else:
                pixmap_t4 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t4.fill(Qt.transparent)                         
            self.t_4_bodyimage.setPixmap(pixmap_t4)
            self.t_4_bodyimage.setScaledContents(True)

            if index+2 < len(self.body_image_paths):
                pixmap_t5 = QPixmap(self.body_image_paths[index+2])
            else:
                pixmap_t5 = QPixmap(int(pixmap_t3.width()), int(pixmap_t3.height()))
                pixmap_t5.fill(Qt.transparent)            
            self.t_5_bodyimage.setPixmap(pixmap_t5)
            self.t_5_bodyimage.setScaledContents(True)
            
    
    def changeImage(self, value):
        self.current_image_index = value
        self.loadImage(self.current_image_index)
        self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')

        # self.radioButton.setCheckable(True)
        # self.radioButton_2.setCheckable(True)
        # self.radioButton_3.setCheckable(True)
        # self.radioButton_4.setCheckable(True)
        # self.radioButton_5.setCheckable(True)
        # self.radioButton_6.setCheckable(True)
        # self.radioButton_7.setCheckable(True)
        
        if self.annotateList[self.current_image_index][1] == -3:
            self.radioButton.setChecked(True)
        elif self.annotateList[self.current_image_index][1] == -2:
            self.radioButton_2.setChecked(True)
        elif self.annotateList[self.current_image_index][1] == -1:
            self.radioButton_3.setChecked(True)
        elif self.annotateList[self.current_image_index][1] == 0:
            self.radioButton_4.setChecked(True)
        elif self.annotateList[self.current_image_index][1] == 1:
            self.radioButton_5.setChecked(True)
        elif self.annotateList[self.current_image_index][1] == 2:
            self.radioButton_6.setChecked(True)
        elif self.annotateList[self.current_image_index][1] == 3:
            self.radioButton_7.setChecked(True)
        else:
            self.group.setExclusive(False)
            # print("다지워")
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(False)
            self.radioButton_7.setChecked(False)

            self.group.setExclusive(True)


            




if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # face_image_paths = []#["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg", "image6.jpg"]
    # body_image_paths = []#["image6.jpg", "image5.jpg", "image4.jpg", "image3.jpg", "image2.jpg", "image1.jpg"]
    #WindowClass의 인스턴스 생성
    # myWindow = WindowClass(face_image_paths, body_image_paths)
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()