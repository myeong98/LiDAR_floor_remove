import numpy as np
from scipy.optimize import least_squares

# 파일에서 포인트 클라우드 데이터를 읽는 함수
def read_point_cloud(filename):
    points = np.loadtxt(filename, delimiter=' ')
    return points

# RANSAC 알고리즘을 이용해 평면 모델 찾기
def ransac_plane_fitting(points, threshold=0.01, max_iterations=1000):
    best_inliers = []
    for _ in range(max_iterations):
        # 무작위로 3개의 점을 선택하여 평면 모델을 생성
        sample_points = points[np.random.choice(points.shape[0], 3, replace=False), :]
        # 평면의 방정식 ax + by + cz + d = 0의 계수 [a, b, c, d]를 계산
        v1 = sample_points[1] - sample_points[0]
        v2 = sample_points[2] - sample_points[0]
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)
        d = -np.dot(normal, sample_points[0])
        plane_coefficients = np.append(normal, d)
        
        # 모든 점에 대해 평면으로부터의 거리 계산
        distances = np.abs(np.dot(points, plane_coefficients[:3]) + plane_coefficients[3])
        inliers = points[distances < threshold]
        
        # 최대 인라이어 수를 가진 모델을 찾음
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_plane = plane_coefficients
            
    return best_inliers, best_plane

# 인라이어가 아닌 점들(즉, 바닥이 제거된 점들)을 찾아서 저장하는 함수
def save_filtered_points(points, plane, threshold=0.01, filename='ransac.txt'):
    distances = np.abs(np.dot(points, plane[:3]) + plane[3])
    filtered_points = points[distances >= threshold]
    np.savetxt(filename, filtered_points, delimiter=' ')
    print(f"Filtered points saved to {filename}")

# 포인트 클라우드 데이터 로드
points = read_point_cloud('output.txt')

# RANSAC으로 바닥 제거
inliers, plane = ransac_plane_fitting(points)

# 바닥이 제거된 포인트 클라우드 저장
save_filtered_points(points, plane)
