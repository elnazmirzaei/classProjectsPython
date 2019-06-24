import random


m=300
n=250


	
	
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

#import matplotlib.pyplot as plt
import numpy as np


#(a, b, c)=plt.hist(cd,bins=n, cumulative=1,
 #       label='Reversed emp.')

#plt.show()
#print(len(a))

#cDensity = []
#for i in range(0,n):
#	cDensity.append(0)
#for i in range(1, n, 1):
 # 	cDensity[i]=(a[i]/m)

#plt.clf()
#plt.plot(cDensity)
#plt.ylabel("Fraction ")
#plt.xlabel("Number of trials required k")
#plt.title("Question 1 Part B")
#plt.show()
	


print("average")
EN=np.mean(cd)
print(EN)