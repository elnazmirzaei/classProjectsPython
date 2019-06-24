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


	b=16
	r=10

	H12=0
	H13=0
	H14=0
	H23=0
	H24=0
	H34=0

	max=100000000
	for x in range (0, b):
		HD1=[max for i in range(1,r+1)]
		HD2=[max for i in range(1,r+1)]
		HD3=[max for i in range(1,r+1)]
		HD4=[max for i in range(1,r+1)]
		for i in range (0,r):
			x=randint(16,36)
			y=randint(0,10000)
			for j in range (1,len(UniD1)):
				UD1=int(hashlib.sha1(str(UniD1[j])).hexdigest(), x) % (10 ** 4)+y
				if UD1 < HD1[i]:
					HD1[i]=UD1
			for j in range (1, len(UniD2)):
				UD2=int(hashlib.sha1(str(UniD2[j])).hexdigest(), x) % (10 ** 4)+y
				if UD2 < HD2[i]:
					HD2[i]=UD2
			for j in range (1,len(UniD3)):
				UD3=int(hashlib.sha1(str(UniD3[j])).hexdigest(), x) % (10 ** 4)+y
				if UD3 < HD3[i]:
					HD3[i]=UD3
			for j in range (1, len(UniD4)):
				UD4=int(hashlib.sha1(str(UniD4[j])).hexdigest(), x) % (10 ** 4)+y
				if UD4 < HD4[i]:
					HD4[i]=UD4
		if(HD1==HD2):
			H12=H12+1
		if(HD1==HD3):
			H13=H13+1
		if(HD1==HD4):
			H14=H14+1
		if(HD2==HD3):
			H23=H23+1
		if(HD2==HD4):
			H24=H24+1
		if(HD3==HD4):
			H34=H34+1
	print("D1 and D2: ")
	print(float(H12)/b)
	print("D1 and D3: ")
	print(float(H13)/b)
	print("D1 and D4: ")
	print(float(H14)/b)
	print("D2 and D3: ")
	print(float(H23)/b)
	print("D2 and D4: ")
	print(float(H24)/b)
	print("D3 and D4: ")
	print(float(H34)/b)


	


'''
	print(math.log10(160)/math.log10(0.7))
	print(160/14)
	print(11*14)
'''
main()




