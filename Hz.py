import pywt
import os
from obspy import read, UTCDateTime
import numpy as np
import matplotlib.pyplot as plt
from obspy.core.inventory import read_inventory
from obspy.signal.trigger import classic_sta_lta
import pandas as pd

inv = read_inventory(r'C:\Users\Brian\Desktop\earthscience\output.dataless')


path = r"C:\Users\Brian\Desktop\earthscience\data\2022-09-17T13_43_40.mseed"

st = read(path)
tr = st[2]

'''
# Filtering with a lowpass on a copy of the original Trace
tr_filt = tr.copy()
tr_filt.filter('lowpass', freq=1.0, corners=2, zerophase=True)
# Now let's plot the raw and filtered data...
t = np.arange(0, tr.stats.npts / tr.stats.sampling_rate,
              tr.stats.delta)
plt.subplot(211)
plt.plot(t, tr.data, 'k')
plt.ylabel('Raw Data')
plt.subplot(212)
plt.plot(t, tr_filt.data, 'k')
plt.ylabel('Lowpassed Data')
plt.xlabel('Time [s]')
plt.suptitle(tr.stats.starttime)
plt.show()
'''