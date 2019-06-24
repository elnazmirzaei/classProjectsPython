import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt
import random

def eucludian(A,B):

	dis=0.0
	
	for i in range(1,len(A)):
		dis=dis+((B[i])-(A[i]))**2
		
	
	return (np.sqrt(dis)) 

def main():


	Gonzalez=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
	Gcounter=0

	cumul=[]
	#df = pandas.read_table('C1.txt', sep='\t', header=None)
	df2 = np.loadtxt('C2.txt')

	#print(df2)
	df=[]

	for i in range(0,len(df2)):
		df.append([df2[i]])	
	df=np.asarray(df).tolist()
	#print(df[0])
	#df=[[[10,10]],[[20,20]],[[30,30]],[[40,40]]]

	for e in range(0,100):

		C=[]
		C.append(df[0][0])
		#del(df[0])
		#print(C)
		X=df
		del(X[0])
		
		while(len(C)<3):
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


		#print(C)



						#print("changed")
			#print(np.argmax(dist))
			#print(dist[np.argmax(dist)])
			#print(np.sort(dist))
			#print(df[np.argmax(dist)])
			#C.append(df[np.argmax(dist)][0])
			#print(C)
			#print(phi)
			#del(df[np.argmax(dist)])
		#print(C)
		#print(np.sort(phi))
		#print(dist)
		#C=C[0:3]
		#print(C)
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
		#print(np.sort(dist))
		#print(phi)
		#print(C[0])
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
			#plt.scatter(X,Y)
		#plt.show()
		if Gonzalez==phi:
			Gcounter=Gcounter+1
		print(" the 3-center cost ")
		print(np.max(dist))
		print(" the 3-means cost")
		sum=0
		for w in range (0,len(dist)):
			dist[w]=dist[w]**2
		sum=np.mean(dist)
		print(np.sqrt(sum))
		cumul.append(np.sqrt(sum))
	Cu=np.cumsum(cumul)
	print("Gonzalez")
	print(Gcounter)
	plt.plot(Cu)
	plt.show()

	
main()