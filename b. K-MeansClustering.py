from numpy import random, array
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)
    return X

# 5 clusters 
data = createClusteredData(100, 5)

# building a model
model = KMeans(n_clusters=5)

# scaling the data to normalize it! Important for good results.
model = model.fit(scale(data))

# we can look at the clusters each data point was assigned to
print(model.labels_)

# visualize it:
plt.figure(figsize=(10, 8))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()
