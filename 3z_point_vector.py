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

def calculate_and_save_z_normal_vectors(points, filename):
    """모든 연속적인 3점 조합에 대해 z 축 방향 벡터를 계산하고 파일에 저장합니다."""
    with open(filename, 'w') as file:
        file.write("# Z-Axis Normal Vectors:\n")
        for i in range(len(points) - 2):  # 모든 점에 대해 연속적인 3점을 선택
            p1, p2, p3 = points[i], points[i+1], points[i+2]
            z_normal = calculate_z_normal_vector(p1, p2, p3)
            if z_normal is not None:
                file.write(str(z_normal) + "\n")

points = read_point_cloud('output.txt')
calculate_and_save_z_normal_vectors(points, 'z_direction_vectors.txt')

print("Z-axis direction vectors saved to 'z_direction_vectors.txt'")

