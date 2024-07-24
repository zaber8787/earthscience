import os
from obspy import read, UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
from obspy.core.inventory import read_inventory
from obspy.signal.trigger import classic_sta_lta
import pandas as pd
import json
file = os.listdir("data")
for i in file:
    with open('starttime.json', 'r', encoding='utf-8')as temp:
        f = json.load(temp)
    inv = read_inventory("output.stationXML")  # output data
    path = i  # file path
    st = read("data/" + path)
    st = st.detrend('linear')
    st = st.remove_response(inventory=inv, output='DISP')
    st = st.filter('bandpass', freqmin=0.5, freqmax=5)
    st = st.filter('bandpass', freqmin=0.5, freqmax=5)
    st[2].plot()
    while True:
        tmp = input("格式:y-m-dTh:m:s")
        print(tmp)
        a = input("Is that the right time?")
        if (a == 'y' or a == 'yes'):
            f[i] = tmp
            with open('starttime.json', 'w', encoding='utf-8')as b:
                json.dump(f, b, indent=2, ensure_ascii=False)
            break
