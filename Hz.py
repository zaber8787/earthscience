from obspy import read
import numpy as np
from scipy.fft import fft, fftfreq

# 读取数据
st = read(r'C:\Users\Brian\Desktop\earthscience\data\2022-09-17T13_43_40.mseed')
tr = st[2]  # 选择其中一路地震信号

# 预处理地震信号
tr.detrend('linear')
tr.filter('bandpass', freqmin=0.5, freqmax=5)

tr.trim(tr.stats.starttime + 175.3, tr.stats.starttime + 175.3 + 3)

# 获取信号数据并进行 FFT
signal = tr.data
spectrum = np.abs(fft(signal))
frequencies = fftfreq(len(signal), d=tr.stats.delta)

# 找到频谱中能量最高的位置
index_of_max_energy = np.argmax(spectrum)
center_frequency = frequencies[index_of_max_energy]

# 输出结果
print("中心频率:", center_frequency)

# 绘制信号波形
tr.plot(type='relative')
