import matplotlib.pyplot as plt
import numpy as np
import math

b=16
r=10

f=[]

for i in range(0,100):
	f.append(1-math.pow((1-math.pow((i*0.01),b)),r))
print(f)

fx=[]
fx1=[]
for i in range(0,100):
	fx.append(i*0.01)
	fx1.append(i)
print(fx)

plt.plot(f)
plt.xticks(fx1,fx,rotation='vertical',size=5)
plt.show()