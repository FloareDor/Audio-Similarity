import timeit
start = timeit.default_timer()
from typing import Collection
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import collections
import librosa as lr
from scipy import spatial
import difflib

import threading

count = 0
arr = []
points = {}
data_dir = 'E:\CS mini projects\Audio_Classification\Data\Test'
audio_files = glob(data_dir + '/*.wav')
for j in audio_files:
	audio, sfreq = lr.load(j)
	print(j)
	time = np.arange(0, len(audio)) / sfreq
	#fig, ax = plt.subplots()
	#ax.plot(time, audio)
	#ax.set(xlabel = 'Time (s)', ylabel = "Amplitude")
	#print(time, audio)			arr.append(j)
	arr.append(j)
	arr.append(time)
	arr.append(audio)


#print(arr)
n = 0
print(n)
st = arr[n+1].tolist()
sa = arr[n+2].tolist()
print(len(arr))

def solve(i):
	#fig, ax = plt.subplots()
	#ax.plot(arr[i+1], arr[i+2])
	#ax.set(xlabel = 'Time (s)', ylabel = "Amplitude")
	# plt.show()
	tt = arr[i+1]
	ta = arr[i+2]
	rt = difflib.SequenceMatcher(None, st, tt)
	ra = difflib.SequenceMatcher(None, sa, ta)
	score = (rt.ratio() + ra.ratio())/2
	points[score] = arr[i]
	print("Done")
	return 0

	#print(f"Score: {score}")
if __name__ == "__main__":
	from multiprocessing import Process
	p = ""
	processes = []
	for i in range(0,len(arr),3):
		p = Process(target = solve, args = (i,))
		processes.append(p)
		p.start()
	p.join()
	#print(points)
	od = collections.OrderedDict(sorted(points.items(), reverse = True))
	for k, v in od.items():
		print(f"{k}: {v}")
	stop = timeit.default_timer()
	print('Time: ', stop-start)

#sm=difflib.SequenceMatcher(None,s1,s2)
#print(sm.ratio())
#print(dataSetI)

#result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
#print(result)