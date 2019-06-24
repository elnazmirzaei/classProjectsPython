import sys
try:
    import pandas as pd
except ImportError as e:
    print("pandas is required for this example. Please install with `pip install pandas` and then try again.")
    sys.exit()

import numpy as np
import kmapper as km
import sklearn
from sklearn import ensemble

# For data we use the Wisconsin Breast Cancer Dataset
# Via: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
df = pd.read_csv("C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/BostonHousing.csv")


X = df.iloc[:,1:]


################################
##Tax as filter function
#################################
lens1 = X.tax

mapper = km.KeplerMapper(verbose=2)
graph = mapper.map(lens1,
                   X,
                   clusterer=sklearn.cluster.KMeans(n_clusters=3),
                   cover=km.Cover(n_cubes=30,perc_overlap=0.4))


mapper.visualize(graph,
                 path_html="C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/BostonHousing_tax.html",
                 custom_tooltips=np.arange(len(lens1)))




################################
##crim as filter function
#################################
lens2 = X.crim

mapper = km.KeplerMapper(verbose=2)
graph = mapper.map(lens2,
                   X,
                   clusterer=sklearn.cluster.KMeans(n_clusters=3),
                   cover=km.Cover(n_cubes=30,perc_overlap=0.4))


mapper.visualize(graph,
                 path_html="C:/Users/lili/courses/ComputationalTopology/FinalProject/Mapper/BostonHousing_crim.html",
                 custom_tooltips=np.arange(len(lens2)))





#######################
##Combined
#####################

# Combine both lenses to create a 2-D [Isolation Forest, L^2-Norm] lens
lens = np.c_[lens1, lens2]

# Create the simplicial complex
graph = mapper.map(lens,
                   X,
                   cover=km.Cover(n_cubes=30, perc_overlap=0.4),
                   clusterer=sklearn.cluster.KMeans(n_clusters=3))

# Visualization
mapper.visualize(graph,
                 path_html="BostonHousing_combined.html",
)