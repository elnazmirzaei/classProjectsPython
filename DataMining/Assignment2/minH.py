import hashlib
import numpy as np
from random import *


def main():


	##For D1
	file = open("D1.txt", "r") 
	Data=file.read()
	l=list(Data)
	##print(l)

	D1=[]

	for i in range (0,(len(l)-2)):
		#tmp=[]
		#tmp.append(l[i])
		#tmp.append(l[i+1])
		#tmp.append(l[i+2])
		tmp=l[i]+l[i+1]+l[i+2]
		D1.append(tmp)

	###make Unique Data
	UniD1=[]
	UniD1.append(D1[0])

	##print(len(D1))
	counter=1
	for i in range (1,(len(D1)-1)):
		
		flag=1
		for j in range(0,counter):
			if D1[i][0]==UniD1[j][0] and D1[i][1]==UniD1[j][1] and D1[i][2]==UniD1[j][2]:
				flag=0
		if flag==1:
			UniD1.append(D1[i])
			counter=counter+1

	#print("D1:")
	#print(len(UniD1))
	##print(UniD1)

	##for D2

	file = open("D2.txt", "r") 
	Data=file.read()
	l=list(Data)
	##print(l)

	D2=[]

	for i in range (0,(len(l)-2)):
		#tmp=[]
		#tmp.append(l[i])
		#tmp.append(l[i+1])
		#tmp.append(l[i+2])
		tmp=l[i]+l[i+1]+l[i+2]
		D2.append(tmp)

	###make Unique Data
	UniD2=[]
	UniD2.append(D2[0])


	counter=1
	for i in range (1,(len(D2)-1)):
		
		flag=1
		for j in range(0,counter):
			if D2[i][0]==UniD2[j][0] and D2[i][1]==UniD2[j][1] and D2[i][2]==UniD2[j][2]:
				flag=0
		if flag==1:
			UniD2.append(D2[i])
			counter=counter+1


	UD1=UniD1
	UD2=UniD2
	minD1=10000000
	minD2=10000000
	JScounter=0
	t=900
	for i in range (0,t):
		minD1=100000
		minD2=100000
		x=randint(16,36)
		y=randint(0,10000)
		for j in range (1,len(UniD1)):
			UD1[j]=int(hashlib.sha1(str(UniD1[j])).hexdigest(), x) % (10 ** 4)+y
			if UD1[j] < minD1:
				minD1=UD1[j]
		for j in range (1, len(UniD2)):
			UD2[j]=int(hashlib.sha1(str(UniD2[j])).hexdigest(), x) % (10 ** 4)+y
			if UD2[j]<minD2:
				minD2=UD2[j]
		#print("minD1,D2")
		#print(minD1)
		#print(minD2)
		if minD1==minD2:		
			JScounter=JScounter+1
	average=float(JScounter)/(t)
	print("Average")
	print(average)


main()