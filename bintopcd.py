import numpy as np
import open3d as o3d

def read_bin_file(filename):
    # .bin 파일에서 점 구름 데이터를 읽어 numpy 배열로 반환
    points = np.fromfile(filename, dtype=np.float32).reshape(-1, 4)  # XYZ + intensity
    return points[:, :3]  # intensity 값을 제외한 XYZ만 사용

def main():
    filename = "1.bin"
    points = read_bin_file(filename)
    
    # Open3D의 PointCloud 객체 생성
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(points)
    
    # PCD 파일로 저장
    o3d.io.write_point_cloud("output.pcd", cloud)
    
    # TXT 파일로 저장 (선택적)
    np.savetxt("output.txt", points, fmt='%f %f %f')

if __name__ == "__main__":
    main()

