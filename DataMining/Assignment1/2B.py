import random

import timeit
ma=[300,2500,5000]

m=5000

ti = []
for i in range(0,11):
	ti.append(0)

for d in range(0,11):
	start = timeit.default_timer()
	n=(250+d*1975)
	cd = []
	for i in range(0,m):
		cd.append(0)


	for q in range (0,m):
		array = []
		for i in range(0,n+1):
			array.append(0)

		j=0
		k=0

		while j<n:
			value=random.randint(1,n)
			k=k+1
			if array[value]==0:
				array[value]=1
				j=j+1
		cd[q]=k

	for q2 in range(1,m-1):
		print(cd[q2])

	stop= timeit.default_timer()
	ti[d]=stop - start
	print stop - start

st1="new2result"
st2=".txt"
st=st1+str(m)+st2
fo = open(st, "wb")
for item in ti:
	fo.write("%s\n" % ti)
fo.close()
#import numpy as np
#import matplotlib.pyplot as plt


#plt.plot(np.cumsum(cd))
#plt.ylabel('cumulative density')
#plt.show()

#assignment 1 part c
#print("average")
#EN=np.mean(cd)
#print(EN)