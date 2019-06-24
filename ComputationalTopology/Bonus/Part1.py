#####################################################################################
##Horse
######################################################################################
import numpy as np
import sklearn
import kmapper as km

data = np.genfromtxt('C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/kepler-mapper/examples/horse/horse-reference.csv', delimiter=',')

mapper = km.KeplerMapper(verbose=2)



lens = mapper.fit_transform(data)


graph = mapper.map(lens,
                   data,
                   clusterer=sklearn.cluster.DBSCAN(eps=0.1, min_samples=5),
                   cover=km.Cover(n_cubes=30,perc_overlap=0.2))


mapper.visualize(graph,
                 path_html="C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/horse_keplermapper_output.html",
                 custom_tooltips=np.arange(len(lens)))

# You may want to visualize the original point cloud data in 3D scatter too
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0],data[:,1],data[:,2])
plt.savefig("horse-reference.csv.png")
plt.show()
"""


#####################################################################################
##Modify horse example so that the overlapping parameter is changed to 50%. (1 points)
######################################################################################
import numpy as np
import sklearn
import kmapper as km

data = np.genfromtxt('C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/kepler-mapper/examples/horse/horse-reference.csv', delimiter=',')

mapper = km.KeplerMapper(verbose=2)



lens = mapper.fit_transform(data)


graph = mapper.map(lens,
                   data,
                   clusterer=sklearn.cluster.DBSCAN(eps=0.1, min_samples=5),
                   cover=km.Cover(n_cubes=30,perc_overlap=0.5))


mapper.visualize(graph,
                 path_html="C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/horse_keplermapper_output_ChangeOverlap.html",
                 custom_tooltips=np.arange(len(lens)))


#####################################################################################
##Modify horse example by replacing the mapper clustering method with K-means clustering from scikit-lean, 
##with parameter n clusters set to 2 or 3. (2 points)
######################################################################################
import numpy as np
import sklearn
import kmapper as km

data = np.genfromtxt('C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/kepler-mapper/examples/horse/horse-reference.csv', delimiter=',')

mapper = km.KeplerMapper(verbose=2)

'''
# Project by first three UMAP components
X_projected = mapper.project(
    data,
    projection="l2norm"
)
'''

lens = mapper.fit_transform(data)


graph = mapper.map(lens,
                   data,
                   clusterer=sklearn.cluster.KMeans(n_clusters=2),
                   cover=km.Cover(n_cubes=30,perc_overlap=0.5))


mapper.visualize(graph,
                 path_html="C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/horse_keplermapper_output_Kmeans.html",
                 custom_tooltips=np.arange(len(lens)))

################################################################################
##Modify makecircles example by replacing the lens to a different projection
##direction; and explain what this modification mean to the data (2 points)
###############################################################################
# Import the class
import kmapper as km
import pandas as pd
# Some sample data
from sklearn import datasets
data, labels = datasets.make_circles(n_samples=5000, noise=0.03, factor=0.3)

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Fit to and transform the data
projected_data = mapper.fit_transform(data, projection="median") # X-Y axis

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, nr_cubes=10)

# Visualize it
mapper.visualize(graph, path_html="C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/make_circles_keplermapper_output-changedProjection.html",
                 title="make_circles(n_samples=5000, noise=0.03, factor=0.3)")

"""
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()

ax.scatter(data[:,0],data[:,1])
plt.savefig("C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/circle.png")
plt.show()
"""
