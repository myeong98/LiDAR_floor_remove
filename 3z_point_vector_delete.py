import numpy as np

def read_point_cloud(filename):
    """포인트 클라우드 데이터를 파일에서 읽어 numpy 배열로 반환합니다."""
    points = np.loadtxt(filename, delimiter=' ')
    return points

def calculate_z_normal_vector(p1, p2, p3):
    """3개의 점으로부터 z 축에 대한 방향 벡터를 계산합니다."""
    v1 = p2 - p1
    v2 = p3 - p1
    normal = np.cross(v1, v2)
    normal_norm = np.linalg.norm(normal)
    if normal_norm == 0:  # 세 점이 일직선 상에 있어 법선이 정의되지 않는 경우
        return None
    normal = normal / normal_norm  # 법선 벡터를 정규화
    return normal[2]  # z 축 방향 벡터 반환

def filter_points_by_z_normal(points):
    """z 방향 벡터가 양수인 부분들을 제거하여 새로운 포인트 클라우드 데이터를 생성합니다."""
    filtered_points_indices = set()  # 중복을 방지하기 위한 집합
    for i in range(len(points) - 2):  # 모든 점에 대해 연속적인 3점을 선택
        p1, p2, p3 = i, i+1, i+2
        z_normal = calculate_z_normal_vector(points[p1], points[p2], points[p3])
        if z_normal is not None and z_normal <= 0:  # 양수인 경우 필터링
            filtered_points_indices.update([p1, p2, p3])  # 집합에 인덱스 추가

    # 집합에 저장된 인덱스를 사용하여 점들을 선택
    filtered_points = points[list(filtered_points_indices)]
    return filtered_points

def save_point_cloud(filename, points):
    """포인트 클라우드 데이터를 파일에 저장합니다."""
    np.savetxt(filename, points, delimiter=' ')

# 파일 경로는 실제 환경에 맞게 조정해야 합니다.
points = read_point_cloud('output.txt')
filtered_points = filter_points_by_z_normal(points)
save_point_cloud('filtered_output.txt', filtered_points)

print("Filtered point cloud saved to 'filtered_output.txt'")

