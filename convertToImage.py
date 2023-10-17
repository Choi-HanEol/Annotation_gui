import cv2
import os
# 동영상 파일 경로
video_path = 'test.mp4'
folder_path = '새로운_폴더'
# 동영상 캡처 객체 생성
cap = cv2.VideoCapture(video_path)

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
    cv2.imwrite(image_filename, frame)
    
    # 다음 프레임으로 이동
    frame_count += 1

# 동영상 캡처 객체 해제
cap.release()
cv2.destroyAllWindows()
