import numpy as np
import matplotlib.pyplot as plt

# 데이터
data = np.random.rand(5, 5)  # 5x5 크기의 랜덤 데이터

# 히트맵 그리기
plt.imshow(data, cmap='hot')

# 컬러 바 추가
plt.colorbar()

# x축 레이블 설정
plt.xlabel('X')
# y축 레이블 설정
plt.ylabel('Y')

# 그래프 제목 설정
plt.title('Heatmap')

# 그래프 출력
plt.show()
