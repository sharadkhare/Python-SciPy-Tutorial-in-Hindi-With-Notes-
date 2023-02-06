# Working with spatial data: it refers to data thzt is represented in a geometric space.
# Triangulation: one method to generate these triangulation through the point is delaunay() triangulation.

# here now we will create a triangualtion from some points:
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

sharad = np.array([[2,4], [3,4], [3,0], [2,2], [4,1]])
simplices = Delaunay(sharad).simplices
plt.triplot(sharad[:,0], sharad[:,1], simplices)
plt.scatter(sharad[:,0], sharad[:,1], color='r')
plt.show()

# Convex HUll: it is the smallest polygon that covers all of the given point:
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

sharad = np.array([[2,4], [3,4], [3,0], [2,2], [4,1], [1,2], [5,0], [3,1],[1,2],[0,2]])

hull = ConvexHull(sharad)
hull_points = hull.simplices
plt.scatter(sharad[:,0], sharad[:,1])
for simplex in hull_points:
    plt.plot(sharad[simplex,0], sharad[simplex,1], 'k-')
plt.show()

# KDTrees: they are a data structures optimized for the nearest neighbour queries.
from scipy.spatial import KDTree
sharad = [(1,-1), (2,3), (-2,3), (2,-3)]
tree = KDTree(sharad)
res = tree.query((1,1))
print(res)

# Distance matrix: it is used to find the various types of distance between 2 points . there are basically 2 types: Euclidean Distance, Cosine Distance.
# Euclidean Distance: 
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
sharad = euclidean(p1, p2)
print(sharad)

# Cosine Distance: 
from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
sharad = cosine(p1, p2)
print(sharad)