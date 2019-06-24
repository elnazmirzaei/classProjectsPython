import random
n=4000
m=300


cd = []
for i in range(0,m):
	cd.append(0)


for q in range(1,m):
	variable = []
	for i in range(0,n+1):
		variable.append(0)

	flag=1
	k=0
	while flag:
		value=random.randint(0,n)
		variable[value]=variable[value]+1
		k=k+1
		if variable[value]==2:
			flag=0

	cd[q]=k

import matplotlib.pyplot as plt
import numpy as np


(a, b, c)=plt.hist(cd,bins=n, cumulative=1,
        label='Reversed emp.')

#plt.show()
print(len(a))

cDensity = []
for i in range(0,n):
	cDensity.append(0)
for i in range(1, n, 1):
  	cDensity[i]=(a[i]/m)

plt.clf()
plt.plot(cDensity)
plt.ylabel("Fraction ")
plt.xlabel("Number of trials required k")
plt.title("Question 1 Part B")
plt.show()
