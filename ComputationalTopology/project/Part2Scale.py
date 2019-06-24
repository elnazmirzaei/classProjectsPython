

########################################
##PersistenceScaleSpaceKernel
##########################################
import sklearn_tda as tda
import matplotlib.pyplot as plt
import numpy as np
from sklearn.kernel_approximation import RBFSampler


#for 8classes
#c=np.array([1,2,3,4,5,6,7,8])
#ccol=np.repeat(c,10)


#for 4 classes
c=np.array([1,2,3,4])
ccol=np.repeat(c,20)


cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

s=(80,80)
Perscale=np.zeros(s)

import glob
txt_files = glob.glob("../Dim0-resized/*.txt")
len(txt_files)

i=1
j=8
			
D=np.genfromtxt(txt_files[i],skip_header=1)
D1=D[:,[1,2]]
diags = [D1]
Dj=np.genfromtxt(txt_files[j],skip_header=1)
Dj1=Dj[:,[1,2]]
diags2 = [Dj1]
PSS = tda.PersistenceScaleSpaceKernel(bandwidth=10.)
X = PSS.fit(diags)
Y = PSS.transform(diags2)



for i in range(0, len(txt_files), 1):
	for j in range(0, len(txt_files), 1):
		if i!=j:
			D=np.genfromtxt(txt_files[i],skip_header=1)
			D=np.array(D)
			D1=D[:,[1,2]]
			diags = [D1]
			Dj=np.genfromtxt(txt_files[j],skip_header=1)
			Dj=np.array(Dj)
			Dj1=Dj[:,[1,2]]
			diags2 = [Dj1]
			PSS = tda.PersistenceScaleSpaceKernel(bandwidth=10.)
			X = PSS.fit(diags)
			Y = PSS.transform(diags2)
			Perscale[i][j]=Y[0,0]


from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

X =Perscale
y = ccol	

score=0.0

for i in range(0, 100, 1):
	x = X
	indices = np.random.permutation(x.shape[0])
	training_idx, test_idx = indices[:64], indices[64:]
	X_train, X_test = x[training_idx,:], x[test_idx,:]
	y_train, y_test = y[training_idx], y[test_idx]
	X_train=X_train[:,training_idx]
	X_test=X_test[:,training_idx]
	X_train.shape, y_train.shape
	X_test.shape, y_test.shape
	clf = SVC(kernel='precomputed', C=10).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))



score
score/100


