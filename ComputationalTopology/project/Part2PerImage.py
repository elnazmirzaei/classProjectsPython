
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

