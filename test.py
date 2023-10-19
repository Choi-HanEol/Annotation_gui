import numpy as np

# 비어 있는 NumPy 배열 생성
empty_array = np.full((2, 2) ,np.nan)
# 또는
empty_array = np.empty(0)

# 배열 크기 확인
print(empty_array.shape)  # 출력: (0,)