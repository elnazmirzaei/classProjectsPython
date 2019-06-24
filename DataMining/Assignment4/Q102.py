import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt
import random
import hashlib


k=10
t=5
C=[[0 for i in range (10)]for j in range(5)]
#print(C)
#print(len(C))
#L=["0" for i in range (9)]
#print(len(C))
i=0
counter=0

with open('S2.txt') as f:
  while True:
    s = f.read(1)
    #print(s)
    if not s:
      #print "End of file"
      break
    counter+=1
    for j in range (t):
    	Z=int(hashlib.sha1(s).hexdigest(), 16+j) % (10 ** 4)
    	Zth=(Z%10)
    	#print(Zth)
    	C[j][Zth]+=1

print(C)



s=['a','b','c']
for i in range (len(s)):
	h=[0 for f in range (t)]
	print(s[i])
	for j in range (t):
		Z=int(hashlib.sha1(s[i]).hexdigest(), 16+j) % (10 ** 4)
		Zth=(Z%10)
		h[j]=C[j][Zth]
	print(min(h))



