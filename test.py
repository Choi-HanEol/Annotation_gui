import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# 이미지 로드
image_path = 'C:/Users/USER/Desktop/pyqt5_design/images/1.jpg'  # 이미지 파일 경로를 지정하세요
image = Image.open(image_path)

# 대비 조절 범위 설정
contrast_range = list(range(-50, 51, 10))  # -50부터 50까지 10씩 증가

# 이미지를 대비 조절하고 저장
for contrast in contrast_range:
    # 대비 조절 변환을 정의
    contrast_adjust = transforms.functional.adjust_contrast(img=image, contrast_factor=contrast)
    
    # 이미지 대비 조절
    # adjusted_image = contrast_adjust(image)
    
    # 대비 조절 값을 파일명에 추가하여 저장 (예: adjusted_image_-50.jpg, adjusted_image_-40.jpg, ...)
    output_filename = f'adjusted_image_{contrast}.jpg'
    
    # 이미지 저장
    contrast_adjust.save(output_filename)

print("이미지 대비 조절 및 저장이 완료되었습니다.")
