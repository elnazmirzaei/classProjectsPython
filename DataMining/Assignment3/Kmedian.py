import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt
import random

def eucludian(A,B):

	dis=0.0
	#print(A)
	for i in range(1,len(A)):
		dis=dis+((B[i])-(A[i]))**2
		
	return (np.sqrt(dis)) 


def SingleLink(A,B):
	min=100000000.00
	for i in range(0,len(A)):
		for j in range(0 , len(B)):
			if min>eucludian(A[i],B[j]):
				min=eucludian(A[i],B[j])
				

	return min

def CompleteLink(A,B):
	max=0.0
	for i in range(0,len(A)):
		for j in range(0 , len(B)):
			if max<eucludian(A[i],B[j]):
				max=eucludian(A[i],B[j])
	return max

def MeanLink(A,B):
	meanA=np.mean(A,axis=0)
	meanB=np.mean(B,axis=0)
	return eucludian(meanA,meanB)

def main():

	#df = pandas.read_table('C1.txt', sep='\t', header=None)
	df2 = np.loadtxt('C3.txt')

	#print(df2)
	df=[]

	for i in range(0,len(df2)):
		df.append([df2[i]])	
	df=np.asarray(df).tolist()
	#print(df[0])
	#df=[[[10,10]],[[20,20]],[[30,30]],[[40,40]],[[50,50]],[[60,60]]]
	C=[]
	z=len(df)
	rz=random.randint(0,z)
	rz2=random.randint(0,z)
	while rz2 == rz:
		rz2=random.randint(0,z)
	rz3=random.randint(0,z)
	while rz3==rz | rz3==rz2:
		rz3=random.randint(0,z)
	'''
	C.append(df[rz][0])
	
	C.append(df[rz2][0])
	C.append(df[rz3][0])
	
	#Gonzalez
	phi=[0 for i in range(0,len(df))]

	while(len(C)<3):
		
		dist=[100000000000.00 for i in range(0,len(df))]
		for i in range(0,len(df)):
			#print("\n")
			#print(i)
			for j in range(0,len(C)):
				print(j)
				print(dist[i])
				print(eucludian(C[j],df[i][0]))
				if dist[i]>eucludian(C[j],df[i][0]):
					phi[i]=j
					dist[i]=eucludian(C[j],df[i][0])
					#print("changed")
		#print(np.argmax(dist))
		#print(dist[np.argmax(dist)])
		#print(np.sort(dist))
		#print(df[np.argmax(dist)])
		C.append(df[np.argmax(dist)][0])
	'''

	###this is Kmeans++ that has been commeented
	
		#Kmeans++
	C.append(df[rz][0])	

	X=df
	del(X[rz])
	
	while(len(C)<5):
		ra=[0 for i in range(len(X))]
		phi=[1 for i in range(0,len(df))]
		dist=[100000000000.00 for i in range(0,len(df))]
		for i in range(0,len(X)):
			#print("\n")
			#print(i)
			for j in range(0,len(C)):
			#	print(j)
			#	print(dist[i])
			#	print(eucludian(C[j],df[i][0]))
				if dist[i]>eucludian(C[j],X[i][0]):
					phi[i]=j
					dist[i]=eucludian(C[j],X[i][0])
			
			ra[i]=((dist[i])**2)
		t=[]
		t=np.cumsum(ra)
		#print("in")
		#print(t[len(t)-1])
		tm=np.sum(t)
		#print("sum")
		#print(tm)
		#print()
			#print(tm)
		for z in range(0,len(t)):
			t[z]=np.divide(t[z],t[len(t)-1])
		ci=random.uniform(0, 1)
		#print("random")
		#print(ci)
		next=0
		for w in range(0,len(t)):
			if ci<t[w]:
				#print("inja")
				#print(t[w])
				next=w
				break
		#print(next)
		#print("len")
		#print(len(X))
		#print(X[next][0])
		C.append(X[next][0])
		del(X[next])
	####
	
	#this is the C calculated from Kmeans++
	#C=[[218.0, 0.0432563, 0.9044537, -0.0936556, -0.0266388, -0.164665], [913.0, 1.0068492, 2.0544349, -0.1629941, 0.2176896, 1.0458533], [580.0, -0.0815326, 0.0627782, 1.1938728, -0.0675838, -0.0997421], [241.0, 0.0845196, 1.1774418, 0.2345251, 0.0003289, -0.0241566]]
	#0.420343621759
	'''
	#Lloyd
	counter=0
	Pre=list(C)
	Delta=100.0

	while Delta>0.0:
		
		#print("Pre")
		#print(Pre)
		print(Delta)
		#Pre=list(C)
		phi=[0 for i in range(0,len(df))]
		dist=[100000000000.00 for i in range(0,len(df))]
		for i in range(0,len(df)):
			#print("\n")
			#print(i)
			for j in range(0,len(C)):
				#print(j)
				#print(dist[i])
				#print(eucludian(C[j],df[i][0]))
				if dist[i]>eucludian(C[j],df[i][0]):
					phi[i]=j
					dist[i]=eucludian(C[j],df[i][0])
					#print("changed")
		#print(np.argmax(dist))
		#print(dist[np.argmax(dist)])
		#print(np.sort(dist))
		#print(df[np.argmax(dist)])
		print(Pre)
		print(Delta)
		for i in range(0,len(C)):
			tmp=[]
			for j in range(0,len(phi)):
				if phi[j]==i:
					tmp.append(df[j][0])
			C[i]=(np.mean(tmp,axis=0)).tolist()
			#print(np.mean(tmp,axis=0))
		print(Pre)
		print(C)
		Delta=MeanLink(Pre,C)
		print(Delta)
		Pre=list(C)
		#print("C")
		#print(C)
		print("Delta")
		print(Delta)

		counter=counter+1
	################
	'''


	
	#del(df[0])
	print("C is")
	print(C)
	
	Pre=list(C)
	#print("Pre is")
	#print(Pre)

	counter=0
	
	Delta=100.0
	
	#print("Delta")
	#print(Delta)
	
	while Delta>0.0:
	#while counter<50:
		
		#print("Pre")
		#print(Pre)
		#print(Delta)
		#Pre=list(C)
		phi=[1 for i in range(0,len(df))]
		dist=[100000000000.00 for i in range(0,len(df))]
		for i in range(0,len(df)):
			#print("\n")
			#print(i)
			for j in range(0,len(C)):
				#print(j)
				#print(dist[i])
				#print(eucludian(C[j],df[i][0]))
				if dist[i]>eucludian(C[j],df[i][0]):
					phi[i]=j
					dist[i]=eucludian(C[j],df[i][0])
					#print("changed")
		#print(np.argmax(dist))
		#print(dist[np.argmax(dist)])
		#print(np.sort(dist))
		#print(df[np.argmax(dist)])
		#print(Pre)
		#print(Delta)
		for i in range(0,len(C)):
			tmp=[]
			for j in range(0,len(phi)):
				if phi[j]==i:
					tmp.append(df[j][0])
			C[i]=(np.median(tmp,axis=0)).tolist()
			#print(np.mean(tmp,axis=0))
		#print(Pre)
		#print(C)
		Delta=MeanLink(Pre,C)
		#print(Delta)
		Pre=list(C)
		#print("C")
		#print(C)
		#print("Delta")
		#print(Delta)

		counter=counter+1
		#print(C)
		#print(C)
		#print(phi)
		#del(df[np.argmax(dist)])
	print("new C")
	print(C)

	for i in range(0,len(C)):
		tmp=[]
		for j in range(0,len(phi)):
			if phi[j]==i:
				tmp.append(df[j][0])
		X=[]
		Y=[]
		for i in range (0,len(tmp)):
			X.append(tmp[i][1])
			Y.append(tmp[i][2])

		plt.scatter(X,Y)
	#plt.show()


	#print(np.sort(phi))
	#print(dist)
	#C=C[0:3]
	#print(C)

	print(" the 3-center cost ")
	print(np.max(dist))
	print(" the 3-means cost")
	sum=0
	
	sum=np.mean(dist)
	print(sum)
	
	#print(C)
	print(counter)
main()