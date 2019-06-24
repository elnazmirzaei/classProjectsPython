import hashlib
import numpy as np
from random import *
import math



def main():


	##For D1
	file = open("D1.txt", "r") 
	Data=file.read()
	l=list(Data)
	##print(l)

	D1=[]

	for i in range (0,(len(l)-2)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		tmp.append(l[i+2])
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
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		tmp.append(l[i+2])
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

	#print("D2:")
	#print(len(UniD2))


	##for D3

	file = open("D3.txt", "r") 
	Data=file.read()
	l=list(Data)
	##print(l)

	D3=[]

	for i in range (0,(len(l)-2)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		tmp.append(l[i+2])
		D3.append(tmp)

	###make Unique Data
	UniD3=[]
	UniD3.append(D3[0])

	##print(len(D3))
	counter=1
	for i in range (1,(len(D3)-1)):
		
		flag=1
		for j in range(0,counter):
			if D3[i][0]==UniD3[j][0] and D3[i][1]==UniD3[j][1] and D3[i][2]==UniD3[j][2]:
				flag=0
		if flag==1:
			UniD3.append(D3[i])
			counter=counter+1

	#print("D3:")
	#print(len(UniD3))


	##for D4

	file = open("D4.txt", "r") 
	Data=file.read()
	l=list(Data)
	##print(l)

	D4=[]

	for i in range (0,(len(l)-2)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		tmp.append(l[i+2])
		D4.append(tmp)

	###make Unique Data
	UniD4=[]
	UniD4.append(D4[0])

	##print(len(D4))
	counter=1
	for i in range (1,(len(D4)-1)):
		
		flag=1
		for j in range(0,counter):
			if D4[i][0]==UniD4[j][0] and D4[i][1]==UniD4[j][1] and D4[i][2]==UniD4[j][2]:
				flag=0
		if flag==1:
			UniD4.append(D4[i])
			counter=counter+1

	#print("D4:")
	#print(len(UniD4))
	##print(UniD3)

	####D1D2
	b=16
	r=10
	UD1=UniD1
	UD2=UniD2
	minD1=10000000
	minD2=10000000
	JScounter=0
	t=160
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
	print("D1 & D2: ")
	f=1-(math.pow((1-math.pow((average),b)),r))
	print(f)


	####D1D3
	b=16
	r=10
	UD1=UniD1
	UD3=UniD3
	minD1=10000000
	minD3=10000000
	JScounter=0
	t=160
	for i in range (0,t):
		minD1=100000
		minD3=100000
		x=randint(16,36)
		y=randint(0,10000)
		for j in range (1,len(UniD1)):
			UD1[j]=int(hashlib.sha1(str(UniD1[j])).hexdigest(), x) % (10 ** 4)+y
			if UD1[j] < minD1:
				minD1=UD1[j]
		for j in range (1, len(UniD3)):
			UD3[j]=int(hashlib.sha1(str(UniD3[j])).hexdigest(), x) % (10 ** 4)+y
			if UD3[j]<minD3:
				minD3=UD3[j]
		#print("minD1,D3")
		#print(minD1)
		#print(minD3)
		if minD1==minD3:		
			JScounter=JScounter+1
	average=float(JScounter)/(t)
	print("D1 & D3: ")
	f=1-(math.pow((1-math.pow((average),b)),r))
	print(f)

	####D1D4
	b=16
	r=10
	UD1=UniD1
	UD4=UniD4
	minD1=10000000
	minD4=10000000
	JScounter=0
	t=160
	for i in range (0,t):
		minD1=100000
		minD4=100000
		x=randint(16,36)
		y=randint(0,10000)
		for j in range (1,len(UniD1)):
			UD1[j]=int(hashlib.sha1(str(UniD1[j])).hexdigest(), x) % (10 ** 4)+y
			if UD1[j] < minD1:
				minD1=UD1[j]
		for j in range (1, len(UniD4)):
			UD4[j]=int(hashlib.sha1(str(UniD4[j])).hexdigest(), x) % (10 ** 4)+y
			if UD4[j]<minD4:
				minD4=UD4[j]
		#print("minD1,D4")
		#print(minD1)
		#print(minD4)
		if minD1==minD4:		
			JScounter=JScounter+1
	average=float(JScounter)/(t)
	print("D1 & D4: ")
	f=1-(math.pow((1-math.pow((average),b)),r))
	print(f)


####D2D4
	b=16
	r=10
	UD2=UniD2
	UD3=UniD3
	minD2=10000000
	minD3=10000000
	JScounter=0
	t=160
	for i in range (0,t):
		minD2=100000
		minD3=100000
		x=randint(16,36)
		y=randint(0,10000)
		for j in range (1,len(UniD2)):
			UD2[j]=int(hashlib.sha1(str(UniD2[j])).hexdigest(), x) % (10 ** 4)+y
			if UD2[j] < minD2:
				minD2=UD2[j]
		for j in range (1, len(UniD3)):
			UD3[j]=int(hashlib.sha1(str(UniD3[j])).hexdigest(), x) % (10 ** 4)+y
			if UD3[j]<minD3:
				minD3=UD3[j]
		#print("minD2,D3")
		#print(minD2)
		#print(minD3)
		if minD2==minD3:		
			JScounter=JScounter+1
	average=float(JScounter)/(t)
	print("D2 & D3: ")
	f=1-(math.pow((1-math.pow((average),b)),r))
	print(f)
	####D2D4
	b=16
	r=10
	UD2=UniD2
	UD4=UniD4
	minD2=10000000
	minD4=10000000
	JScounter=0
	t=160
	for i in range (0,t):
		minD2=100000
		minD4=100000
		x=randint(16,36)
		y=randint(0,10000)
		for j in range (1,len(UniD2)):
			UD2[j]=int(hashlib.sha1(str(UniD2[j])).hexdigest(), x) % (10 ** 4)+y
			if UD2[j] < minD2:
				minD2=UD2[j]
		for j in range (1, len(UniD4)):
			UD4[j]=int(hashlib.sha1(str(UniD4[j])).hexdigest(), x) % (10 ** 4)+y
			if UD4[j]<minD4:
				minD4=UD4[j]
		#print("minD2,D4")
		#print(minD2)
		#print(minD4)
		if minD2==minD4:		
			JScounter=JScounter+1
	average=float(JScounter)/(t)
	print("D2 & D4: ")
	f=1-(math.pow((1-math.pow((average),b)),r))
	print(f)
	####D3D4
	b=16
	r=10
	UD3=UniD3
	UD4=UniD4
	minD3=10000000
	minD4=10000000
	JScounter=0
	t=160
	for i in range (0,t):
		minD3=100000
		minD4=100000
		x=randint(16,36)
		y=randint(0,10000)
		for j in range (1,len(UniD3)):
			UD3[j]=int(hashlib.sha1(str(UniD3[j])).hexdigest(), x) % (10 ** 4)+y
			if UD3[j] < minD3:
				minD3=UD3[j]
		for j in range (1, len(UniD4)):
			UD4[j]=int(hashlib.sha1(str(UniD4[j])).hexdigest(), x) % (10 ** 4)+y
			if UD4[j]<minD4:
				minD4=UD4[j]
		#print("minD3,D4")
		#print(minD3)
		#print(minD4)
		if minD3==minD4:		
			JScounter=JScounter+1
	average=float(JScounter)/(t)
	print("D3 & D4: ")
	f=1-(math.pow((1-math.pow((average),b)),r))
	print(f)

main()