import pywt
import os
from obspy import read, UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
from obspy.core.inventory import read_inventory
from obspy.signal.trigger import classic_sta_lta
import pandas as pd

inv = read_inventory(r'C:\Users\Brian\Desktop\earthscience\output.dataless')


# 讀取地震數據
path = r"C:\Users\Brian\Desktop\earthscience\data"
files = os.listdir(path)


def check(st):
    st[2].detrend('linear')
    st[2].remove_response(inventory=inv, output='DISP')
    st[2].filter('bandpass', freqmin=2, freqmax=50)
    st[2].plot()


for i in files:
    ext = os.path.splitext(i)[-1]
    if (ext == '.mseed'):
        st = read(os.path.join(path, i))
        check(st)
