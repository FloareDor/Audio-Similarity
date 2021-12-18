import timeit
start = timeit.default_timer()
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import librosa as lr
from scipy import spatial
import difflib

import collections



data_dir = 'E:\CS mini projects\Audio_Classification\Data\Test'
audio_files = glob(data_dir + '/*.wav')
arr = []
for j in audio_files:
	audio, sfreq = lr.load(j)
	print(j)
	time = np.arange(0, len(audio)) / sfreq
	#fig, ax = plt.subplots()
	#ax.plot(time, audio)
	#ax.set(xlabel = 'Time (s)', ylabel = "Amplitude")
	#print(time, audio)
	arr.append(j)
	arr.append(time)
	arr.append(audio)

path_to_sample = 'E:\CS mini projects\Audio_Classification\Data\Test\Cymatics - LIFE - Rain - Dripping 3.wav'
n = 0
points = {}
print(n)
st = arr[n+1].tolist()
sa = arr[n+2].tolist()
print(len(arr))
for i in range(0,len(arr),3):
	#fig, ax = plt.subplots()
	#ax.plot(arr[i+1], arr[i+2])
	#ax.set(xlabel = 'Time (s)', ylabel = "Amplitude")
	#plt.show()
	tt = arr[i+1]
	ta = arr[i+2]
	rt = difflib.SequenceMatcher(None, st, tt)
	ra = difflib.SequenceMatcher(None, sa, ta)
	score = (rt.ratio() + ra.ratio())/2
	points[score] = arr[i]
	#print(f"Score: {score}")
	print("Done")
	if i == len(arr) - 1:
		break
od = collections.OrderedDict(sorted(points.items(), reverse = True))
for k, v in od.items():
	print(f"{k}: {v}")

stop = timeit.default_timer()
print('Time: ', stop - start)