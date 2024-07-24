from obspy import read, UTCDateTime
import numpy as np
from scipy.fft import fft, fftfreq
import json
import os

with open('starttime.json', 'r', encoding='utf-8')as file:
    f = json.load(file)

tmp = f.keys()
res = {}
for i in tmp:
    st = read("data/" + i)
    tr = st[2]

    # 预处理地震信号
    tr.detrend('linear')
    tr.filter('bandpass', freqmin=0.5, freqmax=5)
    delta = UTCDateTime(f[i]) - UTCDateTime(tr.stats.starttime)
    tr.trim(tr.stats.starttime + delta, tr.stats.starttime + delta + 3)

    # 获取信号数据并进行 FFT
    signal = tr.data
    spectrum = np.abs(fft(signal))
    frequencies = fftfreq(len(signal), d=tr.stats.delta)

    # 找到频谱中能量最高的位置
    index_of_max_energy = np.argmax(spectrum)
    center_frequency = frequencies[index_of_max_energy]
    res[i] = center_frequency
    # 输出结果
    print("中心频率:", center_frequency)

    # 绘制信号波形
    # tr.plot(type='relative')
with open('result.json', 'w', encoding='utf-8')as file:
    json.dump(res, file,indent=2,ensure_ascii=False)