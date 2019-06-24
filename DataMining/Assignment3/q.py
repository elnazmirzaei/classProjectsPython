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
	df2 = np.loadtxt('C2.txt')
	cumul=[]
	#print(df2)
	df=[]

	for i in range(0,len(df2)):
		df.append([df2[i]])	
	df=np.asarray(df).tolist()
	#print(df[0])
	#df=[[[10,10]],[[20,20]],[[30,30]],[[40,40]],[[50,50]],[[60,60]]]
	phicount=0
	for e in range(0,100):

		C=[]
		C.append(df[0][0])
		'''
		C.append(df[1][0])
		C.append(df[2][0])
		
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
		#Kmeans++

		X=df
		del(X[0])
		
		while(len(C)<4):
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
		C=C[0:3]
		#print("phi")
		#print(phi)
		startPhi=list(phi)
		

		#del(df[0])
		print("C is")
		print(C)
		
		Pre=list(C)
		#print("Pre is")
		#print(Pre)

		counter=0
		
		Delta=100.0
		
		print("Delta")
		print(Delta)
		
		#Lloyd

		while Delta>0.0:
			
			#print("Pre")
			#print(Pre)
			print(Delta)
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
			#print(C)
			#print(C)
			#print(phi)
			#del(df[np.argmax(dist)])
		#print(C)

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
			X2=[]
			Y2=[]
			for i in range (0,(len(C))):
				X2.append(C[i][1])
				Y2.append(C[i][2])
			#plt.scatter(X2,Y2, color="red")

			#plt.scatter(X,Y)
		#plt.show()


		print(np.sort(phi))
		#print(dist)
		#C=C[0:3]
		print(C)

		print(" the 3-center cost ")
		print(np.max(dist))
		print(" the 3-means cost")
		sum=0
		for w in range (0,len(dist)):
			dist[w]=dist[w]**2
		sum=np.mean(dist)
		print(np.sqrt(sum))
		cumul.append(np.sqrt(sum))

		print("phi")
		print(phi)
		#if startPhi==phi:
		#	phicount=phicount+1
		flag=1
		for ii in range(0,len(phi)):
			if phi[ii] != startPhi[ii]:
				flag=0
		if flag==1:
			phicount=phicount+1
		print(counter)
	Cu=np.cumsum(cumul)
	print("phicount")
	print(phicount/100.0)
	plt.plot(Cu)
	plt.show()

main()