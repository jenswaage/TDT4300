import numpy as np
import utils

def euclidean(cluster_1, cluster_2, link):
    if link == 'min':
        min_distance = np.Inf
        for p in range(cluster_1.shape[0]):
            point_1 = cluster_1[p]
            distances = np.sqrt(np.sum(np.square(point_1 - cluster_2), axis=1))
            this_distance = np.amin(distances)
            if this_distance < min_distance:
                min_distance = this_distance
        return min_distance
    elif link == 'max':
        max_distance = 0
        for p in range(cluster_1.shape[0]):
            point_1 = cluster_1[p]
            distances = np.sqrt(np.sum(np.square(point_1 - cluster_2), axis=1))
            this_distance = np.amax(distances)
            if this_distance > max_distance:
                max_distance = this_distance
        return max_distance
    else:
        print("Did not recognize link keyword")


data = np.array([[4,3],
                 [5,8],
                 [5,7],
                 [9,3],
                 [11,6],
                 [13,8]])



def HAC(data, link):
    # Setup with each point as a cluster
    clusters = [[i] for i in range(data.shape[0])]
    utils.print_cluster_config(clusters, data)
    print()

    # Main loop running until we only have one cluster left
    while len(clusters) != 1:
        distance_matrix = np.zeros((len(clusters), len(clusters)))
        min_distance = np.Inf
        for i,c1 in enumerate(clusters):
            cluster_1 = np.array(data[c1], ndmin=2)
            for j, c2 in enumerate(clusters):
                if j != i:
                    cluster_2 = np.array(data[c2], ndmin=2)
                    distance_matrix[i][j] = utils.get_distance(cluster_1, cluster_2, link)
                    if i != j: # If we're looking at the same clusters, distance will be 0
                        if distance_matrix[i][j] < min_distance: # get the clusters with the smallest distance
                            min_distance = distance_matrix[i][j]
                            min_clusters = [i, j] # indices of clusters to be merged

        # Show the new distances
        print("New distance matrix")
        print(f"{distance_matrix}\n")

        # Merge clusters
        min_cluster_1 = min_clusters[0]
        min_cluster_2 = min_clusters[1]
        print(f"Joining clusters {min_cluster_1 + 1} and {min_cluster_2 + 1}")
        clusters[min_cluster_1] += clusters[min_cluster_2]
        del(clusters[min_cluster_2])

        # Show new clusters
        utils.print_cluster_config(clusters, data)
        print()

HAC(data, 'max')