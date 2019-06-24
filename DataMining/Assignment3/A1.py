import numpy as np
import codecs
import pandas
import matplotlib.pyplot as plt

def eucludian(A,B):

	dis=0.0
	
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
	df2 = np.loadtxt('C1.txt')

	#print(df2)
	df=[]

	for i in range(0,len(df2)):
		df.append([df2[i]])	
	df=np.asarray(df).tolist()
	#print(df)
	ind=[-1,-1]
	#print(ind) 
	min=10000000.00

	while len(df)>4:
		min=10000000.00
		ind=[-1,-1]
		for i in range(0,len(df)):
			for j in range(i+1,len(df)):
				tmp=CompleteLink(df[i],df[j])
				if min>tmp:
					min=tmp
					ind[0]=i
					ind[1]=j
		for w in range(0,len(df[ind[1]])):
			df[ind[0]].append(df[ind[1]][w])
		#np.concatenate(df2[0],df2[2])
		#print(len(df[ind[1]]))
		#print("delete")
		#print(df[ind[1]])
		del(df[ind[1]])
	
	print(len(df))

	print(df)
	#SingleLingColor=[]
	#print(df[2][3])


	for j in range(0,len(df)):
		A=df[j]
		X=[]
		Y=[]
		for i in range (0,len(A)):
			X.append(A[i][1])
			Y.append(A[i][2])
		#print(len(A))
		#print(A[:][1])
		#print(X)
		#print(Y)
		plt.scatter(X,Y)

	
	plt.show()

	index=df
	for i in range (0,len(index)):
		for j in range(0,len(index[i])):
			del(index[i][j][1])
			del(index[i][j][1])
	print(index)

	#print(SingleLink(A,B))
	#print(CompleteLink(A,B))

	#print(MeanLink(A,B))
	
main()