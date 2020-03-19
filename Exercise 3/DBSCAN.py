import pandas as pd
import numpy as np
import utils
from matplotlib import pyplot as plt

def cluster(point, clusters, cluster_number, core_points, distances, min_distance):
    if clusters[point] != 0:
        return
    clusters[point] = cluster_number
    point_distances = distances[point,:]
    for cp in core_points:
        if point_distances[cp] <= min_distance and clusters[cp] == 0: # it is within min distance and it is not part of a cluster
            cluster(cp, clusters, cluster_number, core_points, distances, min_distance) # cluster this point



def DBSCAN(data, min_distance, min_points):
    distances = np.zeros((data.shape[0], data.shape[0]))
    for p in range(data.shape[0]):
        distances[p:,] = utils.euclidean(data[p], data)

    df1 = pd.DataFrame(distances)
    df1.to_excel('data\distances.xlsx')
    point_indexes = [i for i in range(data.shape[0])] # list of indexes of all points

    # Get core points
    core_points = []
    other_points = []
    for p in point_indexes:
        point_distances = distances[p,:]
        if point_distances[point_distances <= min_distance].shape[0] >= min_points:
            core_points.append(p)
        else:
            other_points.append(p)
    print(np.array(core_points) + 1)

    # Get border points
    border_points = []
    noise_points = []
    for p in other_points:
        border_point = False
        point_distances = distances[p,:]
        for cp in core_points:
            if point_distances[cp] <= min_distance:
                border_points.append((p, cp))
                border_point = True
                break # this is a border point to some core point
        if not border_point:
            noise_points.append(p)
    print(np.array(border_points)[:,0] + 1)
    print(np.array(noise_points) + 1)

    # Put an edge between all core points within min_distance, and make each group of connected points into a cluster
    clusters = [0 for i in range(data.shape[0])]

    cluster_num = 1
    for point in core_points:
        cluster(point, clusters, cluster_num, core_points, distances, min_distance)
        cluster_num += 1


    # Add each border point to the cluster of it's associated core point
    for bp_cp_pair in border_points: # each border point is on the form (point, associated core point)
        border_point = bp_cp_pair[0]
        assoc_core_point = bp_cp_pair[1]
        clusters[border_point] = clusters[assoc_core_point]

    print(clusters)

    return clusters
data = pd.read_csv('data\dbscan_dataset.csv').to_numpy()[:,1:3].astype(float)
clusters = DBSCAN(data, 2, 3)
x = data[:,0]
y = data[:,1]
plt.scatter(x, y, c = clusters)
plt.show()