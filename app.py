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
        self.initUI()

    def initUI(self):
        file_list = ['face', 'body']
        
        self.file_name = None
        self.face_image_paths = ''
        self.body_image_paths = ''
        self.current_image_index = -1    #현재 보고있는 이미지의 인덱스, t번째 이미지
        self.annotateList = []   #anntate리스트 초기화
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

        self.group.addButton(self.radioButton_8)

        # # 스크롤바 구현
        
        self.line_3.setStyleSheet("background-color: red;")
        self.line_11.setStyleSheet("background-color: red;")
        self.line_6.setStyleSheet("background-color: red;")
        self.line_12.setStyleSheet("background-color: red;")
        
        # 툴바 액션
        self.actionOpenVedioFile.triggered.connect(lambda: self.convertToImage(file_list))
        self.actionSearch.triggered.connect(self.show_search_dialog)
        self.actionOpenNpyFile.triggered.connect(self.run_actionOpenNpyFile)
        self.actionSave_2.triggered.connect(self.run_actionSave_2)
        self.actionSave_As_2.triggered.connect(self.run_actionSave_As_2)
        self.actionOpenImageFolder.triggered.connect(lambda: self.run_actionOpenImageFolder(file_list))
        
        # Data Annotation
        self.radioButton.toggled.connect(self.annotateData)
        self.radioButton_2.toggled.connect(self.annotateData)
        self.radioButton_3.toggled.connect(self.annotateData)
        self.radioButton_4.toggled.connect(self.annotateData)
        self.radioButton_5.toggled.connect(self.annotateData)
        self.radioButton_6.toggled.connect(self.annotateData)
        self.radioButton_7.toggled.connect(self.annotateData)
        self.radioButton_8.toggled.connect(self.annotateData)

        # CSV로 저장
        self.exportButton.clicked.connect(self.exportToCsv)

        # prev, next 버튼클릭
        self.prevButton.clicked.connect(self.clickedPrev)
        self.nextButton.clicked.connect(self.clickedNext)

    def run_actionSave_2(self):
        if self.current_image_index < 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("알림")
            msg_box.setText("파일을 먼저 선택하세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        else:
            if self.file_name == None:
                self.run_actionSave_As_2()
            else:
                np.save(self.file_name, self.annotateList)

    def run_actionSave_As_2(self):   
        if self.current_image_index < 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("알림")
            msg_box.setText("파일을 먼저 선택하세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            self.file_name, _ = QFileDialog.getSaveFileName(self, "NumPy 배열 저장", "", "NumPy 파일 (*.npy)", options=options)

            if self.file_name:
                # NumPy 배열을 생성하고 저장
                np.save(self.file_name, self.annotateList)

    def run_actionOpenNpyFile(self):
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getOpenFileName(self, "NumPy 배열 불러오기", "", "NumPy 파일 (*.npy)", options=options)
        
        if self.scrollbar.maximum() <= 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("오류")
            msg_box.setText("이미지를 먼저 불러오세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        else:
            if self.file_name:
                try:
                    # NumPy 배열 불러오기
                    loaded_array = np.load(self.file_name)
                    if len(loaded_array) != self.scrollbar.maximum()+1:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        print(self.scrollbar.maximum()+1)
                        print(len(self.annotateList))
                        msg_box.setWindowTitle("오류")
                        msg_box.setText("불러온 이미지 파일의 개수와 npy의 크기가 일치하지 않습니다. \n다시 시도해주세요.")
                        msg_box.setStandardButtons(QMessageBox.Ok)
                        msg_box.exec()
                    else:
                        self.annotateList = loaded_array
                        
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
                        elif self.annotateList[self.current_image_index][1] == None:
                            self.radioButton_8.setChecked(True)
                        else:
                            self.group.setExclusive(False)
                            
                            self.radioButton.setChecked(False)
                            self.radioButton_2.setChecked(False)
                            self.radioButton_3.setChecked(False)
                            self.radioButton_4.setChecked(False)
                            self.radioButton_5.setChecked(False)
                            self.radioButton_6.setChecked(False)
                            self.radioButton_7.setChecked(False)
                            self.radioButton_8.setChecked(False)

                            self.group.setExclusive(True)
                except Exception as e:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("오류")
                    msg_box.setText("npy파일을 선택하세요")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec()

            # if len(self.annotateList) != self.scrollbar.maximum()+1:
            #     msg_box = QMessageBox()
            #     msg_box.setIcon(QMessageBox.Information)
            #     print(self.scrollbar.maximum()+1)
            #     print(len(self.annotateList))
            #     msg_box.setWindowTitle("오류")
            #     msg_box.setText("불러온 이미지 파일의 개수와 npy의 크기가 일치하지 않습니다. \n다시 시도해주세요.")
            #     msg_box.setStandardButtons(QMessageBox.Ok)
            #     msg_box.exec()
            #     sys.exit()

    def run_actionOpenImageFolder(self , file_list):      
        
        for faceOrBody in file_list:
            options = QFileDialog.Options()
            folder_path = QFileDialog.getExistingDirectory(self, f'Open {faceOrBody} Folder' ,options=options)
            
            if folder_path:
                
                try:
                    # NumPy 배열 불러오기
                    self.current_image_index = 0
                    if faceOrBody == 'face':
                        self.face_image_paths = glob.glob(os.path.join(folder_path, '*.jpg'))
                    elif faceOrBody == 'body':
                        self.body_image_paths = glob.glob(os.path.join(folder_path, '*.jpg'))
                    else:
                        print('file_list 에러')
                    # 스크롤바 구현
                    self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
                    # self.scrollbar.valueChanged.connect(self.changeImage)
                    self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')
                    # self.loadImage(self.current_image_index)

                except Exception as e:
                    print(e)
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("오류")
                    msg_box.setText("이미지 폴더를 선택하세요")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec()
                
        # 스크롤바 구현
        # self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
        self.scrollbar.valueChanged.connect(self.changeImage)
        # self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')
        self.loadImage(self.current_image_index)
        
        # if len(self.annotateList) != 0:
        #     if self.annotateList[self.current_image_index][1] == -3:
        #         self.radioButton.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == -2:
        #         self.radioButton_2.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == -1:
        #         self.radioButton_3.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == 0:
        #         self.radioButton_4.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == 1:
        #         self.radioButton_5.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == 2:
        #         self.radioButton_6.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == 3:
        #         self.radioButton_7.setChecked(True)
        #     elif self.annotateList[self.current_image_index][1] == None:
        #         self.radioButton_8.setChecked(True)
        #     else:
        #         self.group.setExclusive(False)
                
        #         self.radioButton.setChecked(False)
        #         self.radioButton_2.setChecked(False)
        #         self.radioButton_3.setChecked(False)
        #         self.radioButton_4.setChecked(False)
        #         self.radioButton_5.setChecked(False)
        #         self.radioButton_6.setChecked(False)
        #         self.radioButton_7.setChecked(False)
        #         self.radioButton_8.setChecked(False)

        #         self.group.setExclusive(True)        
        

    def clickedPrev(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.scrollbar.setValue(self.current_image_index)

    def clickedNext(self):
        if self.current_image_index < len(self.face_image_paths) - 1:
                self.current_image_index += 1
                self.scrollbar.setValue(self.current_image_index)
        

    def exportToCsv(self):
        try:
            if self.current_image_index < 0:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("알림")
                msg_box.setText("파일을 먼저 선택하세요")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()
            else:
                reply = QMessageBox.question(self, '알림', '현재까지 한 작업을 csv로 저장하시겠습니까?\nnpy파일 또한 같이 저장됩니다.',
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
                        self.run_actionSave_2()
        except PermissionError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("에러")
            msg_box.setText("해당 csv파일이 열려있습니다. 파일을 닫고 export하세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
            
    

    def annotateData(self):
        if len(self.annotateList) <= 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("알림")
            msg_box.setText("이미지 파일을 먼저 불러오거나 npy 파일을 불러오세요")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
           
        else:    

            annotate_value = 0
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
            elif self.radioButton_8.isChecked():
                annotate_value = None

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
            
            if ok and (int(text)>0 and int(text)<=self.scrollbar.maximum()+1):
                self.changeImage(int(text)-1)
                self.scrollbar.setValue(self.current_image_index)
            elif (int(text)<=0 and int(text)>self.scrollbar.maximum()+1): 
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("알림")
                msg_box.setText(f"범위를 벗어난 인덱스\n범위: (1~{self.scrollbar.maximum()+1})")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()
            self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')


    def convertToImage(self, file_list): #동영상 열어 이미지로 변환
        
        for faceOrBody in file_list:
            
            video_name = QFileDialog.getOpenFileName(self, f'Open {faceOrBody} File')
            
            if os.path.splitext(video_name[0])[1].lower() == '.mp4': #선택한 파일이 동영상일 때
                self.current_image_index = 0
                self.annotateList = np.full((len(self.face_image_paths), 2) ,np.nan)
                cap = cv2.VideoCapture(video_name[0])
                folder_path = os.path.dirname(video_name[0])+'/'+os.path.splitext(video_name[0])[0].split('/')[-1]+'_'+faceOrBody
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
                self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
                self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')
                # 동영상 캡처 객체 해제
                cap.release()
                cv2.destroyAllWindows()
                # 스크롤바 구현
                
            else:
                if os.path.splitext(video_name[0])[1].lower() != '':
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("알림")
                    msg_box.setText("mp4 파일을 선택해야 합니다.")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.exec()
        # self.scrollbar.setMaximum(len(self.face_image_paths) - 1)
        self.scrollbar.valueChanged.connect(self.changeImage)
        # self.statusbar.showMessage(f'{self.current_image_index+1} / {self.scrollbar.maximum()+1}')
        self.loadImage(self.current_image_index)
        
        

        if len(self.face_image_paths) != len(self.body_image_paths):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("오류")
            msg_box.setText("face 이미지 개수와 body 이미지 개수가 일치하지 않습니다. \n다시 시도해주세요.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
            sys.exit()

        
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
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_S: 
            self.run_actionSave_2()
        elif event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_O: 
            self.run_actionOpenNpyFile()
        # RadioButton 단축키
        elif event.key() == Qt.Key_1: 
            self.radioButton.setChecked(True)
        elif event.key() == Qt.Key_2: 
            self.radioButton_2.setChecked(True)
        elif event.key() == Qt.Key_3: 
            self.radioButton_3.setChecked(True)
        elif event.key() == Qt.Key_4: 
            self.radioButton_4.setChecked(True)
        elif event.key() == Qt.Key_5: 
            self.radioButton_5.setChecked(True)
        elif event.key() == Qt.Key_6: 
            self.radioButton_6.setChecked(True)
        elif event.key() == Qt.Key_7: 
            self.radioButton_7.setChecked(True)
        elif event.key() == Qt.Key_0: 
            self.radioButton_8.setChecked(True)
        


    def loadImage(self, index):
        # face_image_paths
        if 0 <= index < len(self.face_image_paths): 
            #face
            pixmap_t3 = QPixmap(self.face_image_paths[index])
            self.t_3_faceimage.setPixmap(pixmap_t3)
            self.t_3_faceimage.setScaledContents(True)
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

        if len(self.annotateList) != 0:
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
            elif self.annotateList[self.current_image_index][1] == None:
                self.radioButton_8.setChecked(True)
            else:
                self.group.setExclusive(False)
            
                self.radioButton.setChecked(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_3.setChecked(False)
                self.radioButton_4.setChecked(False)
                self.radioButton_5.setChecked(False)
                self.radioButton_6.setChecked(False)
                self.radioButton_7.setChecked(False)
                self.radioButton_8.setChecked(False)

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