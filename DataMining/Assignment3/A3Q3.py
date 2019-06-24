import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt
import math
import scipy

C=[]
for d in range(2,22):
	F=math.gamma(d/2.0+1)
	print(d)
	D=math.pow(math.pi,d/2.0)

	A=2**d

	B=A*F/D

	C.append(math.pow(B,1.0/d))
	print(math.pow(B,1.0/d))
plt.plot(range(2,22),C)
plt.show()
d=4
F=math.gamma(d/2.0+1)
print(d)
D=math.pow(math.pi,d/2.0)

A=2**d

B=A*F/D

	#C.append(math.pow(B,1.0/d))
print("C")
print(math.pow(B,1.0/d))


print(C)