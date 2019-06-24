
########################################
##persistence Image
##########################################


#Dim0

import numpy as np
from persim import PersImage

s=(80,100)
Persims=np.zeros(s)

import glob
#by changing Dim0 to Dim1 you can read the other Dim data
txt_files = glob.glob("Dim1-resized/*.txt")
len(txt_files)
for i in range(0, len(txt_files), 1):
    print(txt_files[i])
    D=np.genfromtxt(txt_files[i],skip_header=1)
    D=np.array(D)
    D=D[:,[1, 2]]
    pim = PersImage(pixels=(10,10))
    img = pim.transform(D)
    Persims[i][:] = img.flatten()

	
Persims

#for 8classes
#c=np.array([1,2,3,4,5,6,7,8])
#ccol=np.repeat(c,10)


#for 4 classes
c=np.array([1,2,3,4])
ccol=np.repeat(c,20)



cname=np.array(["Apple","Bell","Bird","Bottle","Brick","Children","Key","Rat"])
ccolnames=np.repeat(cname,10)


s=(80,80)
Distance=np.zeros(s)
for i in range(0, 80, 1):
    for j in range(0, 80, 1):
        Distance[i][j]=np.linalg.norm(Persims[i][:]-Persims[j][:])



from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

X =Persims
#X =Distance
y = ccol


score=0.0

for i in range(0, 100, 1):
	x = X
	indices = np.random.permutation(x.shape[0])
	training_idx, test_idx = indices[:64], indices[64:]
	X_train, X_test = x[training_idx,:], x[test_idx,:]
	y_train, y_test = y[training_idx], y[test_idx]
	X_train.shape, y_train.shape
	X_test.shape, y_test.shape
	clf = SVC(kernel='linear', C=10).fit(X_train, y_train)
	score=score+clf.score(X_test, y_test)
	print(clf.score(X_test, y_test))

score
score/100

#eucludian distance
X =Distance
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

clf = SVC(kernel='precomputed', C=1).fit(X_train, y_train)
    
print("Dim0")
print(clf.score(X_test, y_test))


