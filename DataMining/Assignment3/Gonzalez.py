
import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt

def eucludian(A,B):

	dis=0.0
	
	for i in range(1,len(A)):
		dis=dis+((B[i])-(A[i]))**2
		
	
	return (np.sqrt(dis)) 

def main():

	#df = pandas.read_table('C1.txt', sep='\t', header=None)
	df2 = np.loadtxt('C2.txt')

	#print(df2)
	df=[]

	for i in range(0,len(df2)):
		df.append([df2[i]])	
	df=np.asarray(df).tolist()
	#print(df[0])
	#df=[[[10,10]],[[20,20]],[[30,30]],[[40,40]]]
	C=[]
	C.append(df[0][0])
	#del(df[0])
	#print(C)
	phi=[0 for i in range(0,len(df))]
	while(len(C)<4):
		
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
		#print(C)
		#print(phi)
		#del(df[np.argmax(dist)])
	#print(C)
	print(np.sort(phi))
	#print(dist)
	#C=C[0:3]
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

		X2=[]
		Y2=[]
		for i in range (0,(len(C)-1)):
			X2.append(C[i][1])
			Y2.append(C[i][2])
		plt.scatter(X2,Y2, color="red")

	plt.show()
	print(phi)
	print(" the 3-center cost ")
	print(np.max(dist))
	print(" the 3-means cost")
	sum=0
	for w in range (0,len(dist)):
		dist[w]=dist[w]**2
	sum=np.mean(dist)
	print(np.sqrt(sum))

	print(phi)

main()