import numpy as np

def save_to_pcd(file_path, data):
    header = """# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z
SIZE 4 4 4
TYPE F F F
COUNT 1 1 1
WIDTH {}
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS {}
DATA ascii
""".format(data.shape[0], data.shape[0])
    
    with open(file_path, 'w') as f:
        f.write(header)
        np.savetxt(f, data, fmt='%f')

# 파일 경로 설정
input_file_path = 'ransac.txt'  # 필터링된 데이터 파일 경로
output_pcd_file_path = 'filtered_output.pcd'  # 저장할 PCD 파일 경로

# 필터링된 데이터 로드
filtered_data = np.loadtxt(input_file_path)

# PCD 파일로 저장
save_to_pcd(output_pcd_file_path, filtered_data)

print(f'PCD file saved to: {output_pcd_file_path}')

