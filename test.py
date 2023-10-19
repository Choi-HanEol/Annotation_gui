from PySide6.QtGui import QImage
from PySide6.QtCore import Qt

# 이미지 파일 경로
image_path = './body/frame_0000.jpg'

# QImage로 이미지 로드
image = QImage(image_path)

if not image.isNull():
    # 이미지의 너비와 높이 확인
    width = image.width()
    height = image.height()
    
    print(f"이미지의 너비: {width}")
    print(f"이미지의 높이: {height}")
else:
    print('이미지를 로드할 수 없습니다.')
