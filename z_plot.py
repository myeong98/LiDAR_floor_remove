import numpy as np
import matplotlib.pyplot as plt

# 파일에서 데이터를 로드하는 함수
file_path = 'filtered_points.txt'
def load_data(file_path):
    return np.loadtxt(file_path)

# z값을 시각화하는 함수
def plot_z_values(data):
    plt.figure(figsize=(10, 6))
    # 군집화 없이 모든 점을 동일한 색상으로 표현
    plt.scatter(range(len(data)), data[:, 2], color='blue', marker='o', s=1)  # 점 크기를 조정
    plt.title('Z Values in Point Cloud Data')
    plt.xlabel('Point Index')
    plt.ylabel('Z Value')
    plt.show()

# 메인 코드 실행 부분
file_path = 'filtered_output.txt'  # 파일 경로 설정, 실제 경로로 변경해야 함
data = load_data(file_path)  # 데이터 로드
plot_z_values(data)  # z값 시각화

