import os 
from obspy import read, UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
from obspy.core.inventory import read_inventory
from obspy.signal.trigger import classic_sta_lta
import pandas as pd

inv = read_inventory("") # output data
path = "" #file path

st = read(path)
st = st.detrend('linear')
st = st.remove_response(inventory = inv,output = 'DISP')
st = st.filter('bandpass', freqmin=0.5, freqmax=5)
st = st.filter('bandpass', freqmin=0.5, freqmax=5)
st[2].plot()
