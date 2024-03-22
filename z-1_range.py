import numpy as np

def read_point_cloud(filename):
    """포인트 클라우드 데이터를 파일에서 읽어 numpy 배열로 반환합니다."""
    points = np.loadtxt(filename, delimiter=' ')
    return points

def adjust_sensor_center(points, z_offset=-1.3):
    """센서의 중앙값을 조정합니다. 여기서는 모든 점의 Z값에서 1을 뺍니다."""
    adjusted_points = np.copy(points)
    adjusted_points[:, 2] -= z_offset  # 모든 점의 Z값 조정
    return adjusted_points

def calculate_distance_and_elevation(point):
    """점의 거리와 고도각을 계산합니다."""
    distance = np.linalg.norm(point)
    elevation = np.arctan2(point[2], np.sqrt(point[0]**2 + point[1]**2))
    return distance, np.degrees(elevation)

def filter_points_within_distance_and_elevation(points, max_distance=100.0):
    """원점으로부터 주어진 거리 이내 및 고도각이 음수인 모든 점들을 제거합니다."""
    filtered_points = []
    for point in points:
        distance, elevation = calculate_distance_and_elevation(point)
        # 거리가 max_distance 이내이면서 고도각이 음수인 점을 제거
        if not (distance <= max_distance and elevation < 0):
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
# 센서의 중앙값 조정
adjusted_points = adjust_sensor_center(points)
# 20미터 이내에 있는 고도각이 음수인 점들을 제거
filtered_points = filter_points_within_distance_and_elevation(adjusted_points, 100.0)
# 결과 저장
save_point_cloud(output_filename, filtered_points)

print(f"Filtered point cloud saved to '{output_filename}'.")

