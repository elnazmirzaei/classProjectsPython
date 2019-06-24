#######################################################
##Project2 Part 2
#######################################################
#Bottleneck
#Barcodes-Combined
import numpy as np


BB=np.loadtxt("../Barcode-Bottleneck-distance.txt")
BB.shape

c=np.array([1,2,3,4,5,6,7,8])
ccol=np.repeat(c,10)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

X =BB
y = ccol
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

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
	clf = SVC(kernel='precomputed', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))



#Bottleneck
#Barcodes-Dim0
import numpy as np


BB=np.loadtxt("Dim1-Bottleneck-distance-resized.txt")
BB.shape

#for 8classes
#c=np.array([1,2,3,4,5,6,7,8])
#ccol=np.repeat(c,10)

#for 4 classes
c=np.array([1,2,3,4])
ccol=np.repeat(c,20)


#cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
#ccolnames=np.repeat(cname,10)

X =BB
y = ccol
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

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
	clf = SVC(kernel='linear', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))


#Bottleneck
#Barcodes-Dim1
import numpy as np


BB=np.loadtxt("../Dim1-Bottleneck-distance-resized.txt")
BB.shape

c=np.array([1,2,3,4,5,6,7,8])
ccol=np.repeat(c,10)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

X =BB
y = ccol
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

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
	clf = SVC(kernel='precomputed', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))

###########

#Wasserstein
#Barcodes-Dim0
import numpy as np


BB=np.loadtxt("../Dim0-wasserstein-distance-resized.txt")
BB.shape

c=np.array([1,2,3,4,5,6,7,8])
ccol=np.repeat(c,10)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

X =BB
y = ccol
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

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
	clf = SVC(kernel='precomputed', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))


#Wasserstein
#Barcodes-Dim1
import numpy as np


BB=np.loadtxt("../Dim1-wasserstein-distance-resized.txt")
BB.shape

c=np.array([1,2,3,4,5,6,7,8])
ccol=np.repeat(c,10)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

X =BB
y = ccol
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

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
	clf = SVC(kernel='precomputed', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))

#########################
#ImageFlattened
###########################
import numpy as np


BB=np.loadtxt("../ImageFlattened.txt")
BB.shape

#for 8classes
#c=np.array([1,2,3,4,5,6,7,8])
#ccol=np.repeat(c,10)

#for 4 classes
c=np.array([1,2,3,4])
ccol=np.repeat(c,20)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

X =BB
y = ccol
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

score=0.0

for i in range(0, 100, 1):
	x = X
	indices = np.random.permutation(x.shape[0])
	training_idx, test_idx = indices[:64], indices[64:]
	X_train, X_test = x[training_idx,:], x[test_idx,:]
	y_train, y_test = y[training_idx], y[test_idx]
	X_train.shape, y_train.shape
	X_test.shape, y_test.shape
	clf = SVC(kernel='linear', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))



########################################
##persistence Image
##########################################

import sklearn_tda as tda
import matplotlib.pyplot as plt
import numpy as np
from sklearn.kernel_approximation import RBFSampler

s=(80,100)
Persims=np.zeros(s)

import glob
txt_files = glob.glob("../Barcodes-resized/*.txt")
len(txt_files)
for i in range(0, len(txt_files), 1):
	print(txt_files[i])
	D=np.genfromtxt(txt_files[i],skip_header=1)
	D=np.array(D)
	diags = [D]
	diagsT = tda.DiagramPreprocessor(use=True, scalers=[([1,2], tda.BirthPersistenceTransform())]).fit_transform(diags)
	PI = tda.PersistenceImage(bandwidth=1., weight=lambda x: x[1], im_range=[0,10,0,10], resolution=[10,10])
	Persims[i][:] = PI.fit_transform(diagsT)


c=np.array([1,2,3,4,5,6,7,8])
ccol=np.repeat(c,10)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

X =Persims
y = ccol	

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train.shape, y_train.shape

X_test.shape, y_test.shape

clf = SVC(kernel='linear', C=1).fit(X_train, y_train)
	
print(clf.score(X_test, y_test))



########################################
##PersistenceScaleSpaceKernel
##########################################
import sklearn_tda as tda
import matplotlib.pyplot as plt
import numpy as np
from sklearn.kernel_approximation import RBFSampler


c=np.array([1,2,3,4,5,6,7,8])
ccol=np.repeat(c,10)

cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)

s=(80,80)
Perscale=np.zeros(s)

import glob
txt_files = glob.glob("../Dim1-resized/*.txt")
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
	clf = SVC(kernel='precomputed', C=1).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))






x = X
indices = np.random.permutation(x.shape[0])
training_idx, test_idx = indices[:64], indices[64:]
X_train, X_test = x[training_idx,:], x[test_idx,:]
y_train, y_test = y[training_idx], y[test_idx]
X_train=X_train[:,training_idx]
X_test=X_test[:,training_idx]
X_train.shape, y_train.shape
X_test.shape, y_test.shape
clf = SVC(kernel='precomputed',C=10).fit(X_train, y_train)
score=score+clf.score(X_test, y_test)
print(clf.score(X_test, y_test))