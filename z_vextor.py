import numpy as np

def read_point_cloud(filename):
    points = np.loadtxt(filename, delimiter=' ')
    return points

def ransac_plane_fitting_with_direction_filtering(points, threshold=0.01, max_iterations=1000, direction='up'):
    best_inliers_count = 0
    best_plane = None
    for _ in range(max_iterations):
        sample_points = points[np.random.choice(points.shape[0], 3, replace=False), :]
        v1 = sample_points[1] - sample_points[0]
        v2 = sample_points[2] - sample_points[0]
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)
        d = -np.dot(normal, sample_points[0])
        plane_coefficients = np.append(normal, d)
        
        distances = np.abs(np.dot(points, plane_coefficients[:3]) + plane_coefficients[3])
        inliers = distances < threshold
        
        if inliers.sum() > best_inliers_count:
            best_inliers_count = inliers.sum()
            best_plane = plane_coefficients
            best_inliers_mask = inliers

    # 법선 벡터의 z-성분이 방향 조건과 일치하는지 확인
    if best_plane is not None:
        if (direction == 'up' and best_plane[2] > 0) or (direction == 'down' and best_plane[2] < 0):
            # 방향 조건과 일치하는 평면의 점들을 제외하고 필터링
            filtered_points = points[~best_inliers_mask]
        else:
            # 방향 조건과 일치하지 않으면 원본 포인트 반환
            filtered_points = points
        return filtered_points, best_plane
    else:
        return points, None

points = read_point_cloud('output.txt')
filtered_points, plane = ransac_plane_fitting_with_direction_filtering(points, direction='up')

if filtered_points is not None:
    np.savetxt('filtered_points_directional.txt', filtered_points, delimiter=' ')
    print("Filtered points with directional filtering saved to 'filtered_points_directional.txt'")
else:
    print("No points were filtered based on the directional criteria.")

