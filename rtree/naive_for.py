import numpy as np
#import geopy
from geopy.point import Point
from geopy.distance import geodesic


#n_points = 10_000
n_points = 10
#np.random.seed(42)
#latitudes = np.random.randint(low=-90, high=90, size=(n_points,1), dtype=int)
#longitudes = np.random.randint(low=-180, high=180, size=(n_points,1), dtype=int)
from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence
rs = RandomState(MT19937(SeedSequence(42)))
latitudes = rs.randint(low=-90, high=90, size=(n_points,1), dtype=int)
longitudes = rs.randint(low=-180, high=180, size=(n_points,1), dtype=int)
#coordinates = np.hstack([latitudes, longitudes])
points_np = np.hstack([latitudes, longitudes])
points_geopy = [Point(pt) for pt in points_np]
#print(f"points_geopy[:5] = {points_geopy[:5]}")

dist_matrix = np.diag([np.inf]*n_points)
for i in range(n_points):
    for j in range(i+1, n_points):
        dist_matrix[i, j] = geodesic(points_geopy[i], points_geopy[j]).km
        # km above is essential because we cannot store a geopy.distance.geodesic object inside an ndarray
        #print(f"finished ({i}, {j})")

np.set_printoptions(precision=3)
#print(f"dist_matrix[:5, :5] =\n{dist_matrix[:5, :5]}")

dist_matrix += np.triu(dist_matrix, k=1).T
k = 5
print(f"dist_matrix[:{k}, :{k}] =\n{dist_matrix[:k, :k]}")

#print(f"np.argmin(dist_matrix[:5, :5], axis=0) =\n{np.argmin(dist_matrix[:5, :5], axis=0)}")
#print(f"np.argmin(dist_matrix[:5, :5], axis=1) =\n{np.argmin(dist_matrix[:5, :5], axis=1)}")

nearest_neighbor = np.argmin(dist_matrix, axis=1)
nearest_distance = dist_matrix[range(dist_matrix.shape[0]), nearest_neighbor]
# print the 10 first results
for i in range(10):
    #print(f"Point {i} = {points_geopy[i]}: nb = Point {nearest_neighbor[i]} = {points_geopy[nearest_neighbor[i]]}, dist = {dist_matrix[i, nearest_neighbor[i]]}")
    #print(f"Point {i} = {points_geopy[i].format_decimal()}: nb = Point {nearest_neighbor[i]} = {points_geopy[nearest_neighbor[i]].format_decimal()}, dist = {dist_matrix[i, nearest_neighbor[i]]}")
    print(f"Point {i}:  nb = Point {nearest_neighbor[i]}, dist = {dist_matrix[i, nearest_neighbor[i]]}")
    print(f"Point {i}:  nb = Point {nearest_neighbor[i]}, dist = {nearest_distance[i]}")


