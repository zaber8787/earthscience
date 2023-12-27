import pywt
import os
from obspy import read, UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
from obspy.core.inventory import read_inventory
from obspy.signal.trigger import classic_sta_lta
import pandas as pd

import obspy
import pywt

inv = read_inventory(r'C:\Users\Brian\Desktop\earthscience\output.dataless')


# 讀取地震數據
st = obspy.read(
    r"C:\Users\Brian\Desktop\earthscience\data\2022-09-17 135708GDMSdata (1).mseed")

st.detrend('linear')
st.remove_response(inventory=inv, output='DISP')
st.filter('bandpass', freqmin=2, freqmax=50)

# 計算小波變換
cwt = pywt.cwt(st[0].data, 'haar', widths=np.arange(1, 20, 1))


# 計算 P 波到達時間
p_arrival_time = np.argmax(cwt[0, :])

# 輸出 P 波到達時間
print(p_arrival_time)
