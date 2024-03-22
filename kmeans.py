from sklearn.cluster import KMeans
import numpy as np

# 파일 경로 설정 (여기서는 'output.txt'를 '/mnt/data' 디렉토리에 위치한다고 가정)
file_path = 'output.txt'

# 파일에서 데이터 로드
data = np.loadtxt(file_path)

# z값(높이)만 추출
z_values = data[:, 2].reshape(-1, 1)

# KMeans 군집화 실행
kmeans = KMeans(n_clusters=2, random_state=0).fit(z_values)
labels = kmeans.labels_

# 가장 많은 데이터 포인트를 포함하는 군집 식별
values, counts = np.unique(labels, return_counts=True)
ground_cluster_label = values[np.argmax(counts)]

# 바닥 군집 데이터 제거
filtered_data = data[labels != ground_cluster_label]

# 결과 저장
output_file_path = 'filtered_output.txt'
np.savetxt(output_file_path, filtered_data, fmt='%f')

# 저장된 파일 경로 출력 (사용자에게 파일 위치 안내)
print(f'Filtered data saved to: {output_file_path}')

