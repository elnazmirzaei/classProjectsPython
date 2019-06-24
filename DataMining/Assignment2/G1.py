###Q1 2gram Characters
import numpy as np


#####Q1PB
def jaccard(A,B):
	Jcounter=0
	for i in range (1,len(A)):
		for j in range(1,len(B)):
			if A[i]==B[j]:
				Jcounter=Jcounter+1
	JS=float(Jcounter)/(len(A)+len(B)-Jcounter)
	print(JS)






def main():
##For D1
	file = open("D1.txt", "r") 
	Data=file.read()
	l=list(Data)
	##print(l)

	D1=[]

	for i in range (0,(len(l)-1)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		D1.append(tmp)

	###make Unique Data
	UniD1=[]
	UniD1.append(D1[0])

	##print(len(D1))
	counter=1
	for i in range (1,(len(D1)-1)):
		
		flag=1
		for j in range(0,counter):
			if D1[i][0]==UniD1[j][0] and D1[i][1]==UniD1[j][1]:
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

	for i in range (0,(len(l)-1)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		D2.append(tmp)

	###make Unique Data
	UniD2=[]
	UniD2.append(D2[0])


	counter=1
	for i in range (1,(len(D2)-1)):
		
		flag=1
		for j in range(0,counter):
			if D2[i][0]==UniD2[j][0] and D2[i][1]==UniD2[j][1]:
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

	for i in range (0,(len(l)-1)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		D3.append(tmp)

	###make Unique Data
	UniD3=[]
	UniD3.append(D3[0])

	##print(len(D3))
	counter=1
	for i in range (1,(len(D3)-1)):
		
		flag=1
		for j in range(0,counter):
			if D3[i][0]==UniD3[j][0] and D3[i][1]==UniD3[j][1]:
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

	for i in range (0,(len(l)-1)):
		tmp=[]
		tmp.append(l[i])
		tmp.append(l[i+1])
		D4.append(tmp)

	###make Unique Data
	UniD4=[]
	UniD4.append(D4[0])

	##print(len(D4))
	counter=1
	for i in range (1,(len(D4)-1)):
		
		flag=1
		for j in range(0,counter):
			if D4[i][0]==UniD4[j][0] and D4[i][1]==UniD4[j][1]:
				flag=0
		if flag==1:
			UniD4.append(D4[i])
			counter=counter+1

	#print("D4:")
	#print(len(UniD4))
	#print(UniD3)
	print("Jaccard Similarity Between D1 & D2:")
	jaccard(UniD1,UniD2)
	print("Jaccard Similarity Between D1 & D3:")
	jaccard(UniD1,UniD3)
	print("Jaccard Similarity Between D1 & D4:")
	jaccard(UniD1,UniD4)
	print("Jaccard Similarity Between D2 & D3:")
	jaccard(UniD2,UniD3)
	print("Jaccard Similarity Between D2 & D4:")
	jaccard(UniD2,UniD4)
	print("Jaccard Similarity Between D3 & D4:")
	jaccard(UniD3,UniD4)


main()



