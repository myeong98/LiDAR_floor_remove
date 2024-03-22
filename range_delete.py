import numpy as np

def read_point_cloud(filename):
    """포인트 클라우드 데이터를 파일에서 읽어 numpy 배열로 반환합니다."""
    points = np.loadtxt(filename, delimiter=' ')
    return points

def filter_points_within_distance(points, distance=10.0):
    """원점으로부터 주어진 거리 안에 있는 모든 점들을 제거합니다."""
    filtered_points = []
    for point in points:
        # 각 점의 원점으로부터의 거리 계산
        if np.linalg.norm(point) > distance:
            filtered_points.append(point)
    return np.array(filtered_points)

def save_point_cloud(filename, points):
    """포인트 클라우드 데이터를 파일에 저장합니다."""
    np.savetxt(filename, points, delimiter=' ')

# 파일 경로는 실제 환경에 맞게 조정해야 합니다.
input_filename = 'output.txt'
output_filename = 'filtered_output.txt'

# 포인트 클라우드 데이터 읽기
points = read_point_cloud(input_filename)
# 2미터 이내에 있는 점들을 제거
filtered_points = filter_points_within_distance(points)
# 결과 저장
save_point_cloud(output_filename, filtered_points)

print(f"Filtered point cloud saved to '{output_filename}'.")

