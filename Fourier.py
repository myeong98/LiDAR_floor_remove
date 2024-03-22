import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal import find_peaks

# 신호의 주기를 분석하기 위한 함수
def analyze_periodicity(signal, sampling_rate):
    # 신호의 Fast Fourier Transform (FFT) 계산
    yf = rfft(signal)
    xf = rfftfreq(len(signal), 1 / sampling_rate)

    # 주파수 스펙트럼에서 peak를 찾아서 주기성 분석
    peaks, _ = find_peaks(np.abs(yf), height=0)
    peak_freqs = xf[peaks]
    
    # 가장 높은 peak의 주기 반환
    dominant_frequency = peak_freqs[0]
    period = 1 / dominant_frequency
    return period

# 데이터에서 중간값을 찾고 필터링하는 함수
def filter_data(data, period):
    # 주기별로 데이터를 분할
    num_periods = int(len(data) / period)
    filtered_data = []
    
    for i in range(num_periods):
        # 주기 범위 내의 데이터 추출
        period_data = data[int(i*period):int((i+1)*period), 2]
        # 중간값 계산
        median_value = np.median(period_data)
        # 중간값이 아닌 데이터만 유지
        filtered_data.extend(data[int(i*period):int((i+1)*period)][period_data != median_value])
    
    return np.array(filtered_data)

# 데이터 로드
file_path = 'output.txt'
def load_data(file_path):
    return np.loadtxt(file_path)
data = load_data(file_path)

# 주기성 분석 (샘플링 레이트는 데이터에 맞게 설정해야 함)
period = analyze_periodicity(data[:, 2], sampling_rate=1)

# 데이터 필터링
filtered_data = filter_data(data, period)

# 필터링된 데이터 저장
np.savetxt('filtered_data1.txt', filtered_data, fmt='%f')

