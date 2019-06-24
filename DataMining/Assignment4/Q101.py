import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt
import random
C=[0 for i in range (9)]
#print(len(C))
L=["0" for i in range (9)]
#print(len(C))
i=0
counter=0

with open('test.txt') as f:
  while True:
    s = f.read(1)
    #print(s)
    if not s:
      print "End of file"
      break
    counter+=1
    flag=1
    for j in range (9):
    	if s == L[j]:
    		C[j]+=1
    		flag=0
    		#print("if1")
    		break
    	elif C[j]==0:
    		L[j]=s
    		C[j]=1
    		flag=0
    		#print("elif")
    		break
    if flag==1:
    	#print("flag=1")
    	for j in range (9):
    		C[j]-=1
    
print(L)
print(C)
print("counter is:")
print(counter)

    

