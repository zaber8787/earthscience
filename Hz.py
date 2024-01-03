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


for file in files:
    # 獲取檔案名稱和擴展名
    name, ext = os.path.splitext(file)

    if ext != ".mseed":
        # 獲取檔案名稱
        new_name = name + '.mseed'

        # 修改檔案名稱
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
