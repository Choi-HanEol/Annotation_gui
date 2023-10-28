# import torch
# from torchvision import transforms
# from PIL import Image
# import numpy as np

# # 이미지 로드
# image_path = 'C:/Users/USER/Desktop/pyqt5_design/images/1.jpg'  # 이미지 파일 경로를 지정하세요
# image = Image.open(image_path)



# # Flip 변환 정의
# flip_transforms = [
#     transforms.RandomVerticalFlip(),  # 상하 뒤집기
#     transforms.RandomHorizontalFlip(),  # 좌우 뒤집기
#     transforms.Compose([transforms.RandomVerticalFlip(), transforms.RandomHorizontalFlip()])  # 상하좌우 뒤집기
# ]

# # Flip 방향에 따라 이미지를 뒤집고 저장
# for flip_type, transform in zip(["vertical", "horizontal", "both"], flip_transforms):
#     # 이미지 뒤집기
#     flipped_image = transform(image)
#     output_filename = f'flipped_image_{flip_type}.jpg'
#     flipped_image.save(output_filename)
#     # 저장할 파일명 지정 (예: flipped_image_vertical_0.jpg, flipped_image_horizontal_1.jpg, ...)
    
import numpy as np

# 2차원 배열 생성 및 초기화
num_rows = 10  # 행의 수
num_cols = 2   # 열의 수

# 1열은 1부터 10까지의 숫자로 초기화하고 2열은 NaN으로 초기화
my_array = np.full((num_rows, num_cols), np.nan)
my_array[:, 0] = np.arange(1, 11)

print(my_array[1][0])
