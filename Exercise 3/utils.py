import numpy as np

def get_distance(cluster_1, cluster_2, link):
    distances = np.zeros((cluster_1.shape[0], cluster_2.shape[0]))
    for p in range(cluster_1.shape[0]):
        distances[p,:] = euclidean(cluster_1[p], cluster_2)
    return get_min_max(distances, link)

def euclidean(point, cluster_2):
    distances = np.sqrt(np.sum(np.square(point - cluster_2), axis=1))
    return distances

def get_min_max(distances, link):
    if link == 'min':
        return np.amin(distances)
    elif link == 'max':
        return np.amax(distances)

def print_cluster_config(clusters, data):
    print(f"Cluster configuration: ")
    for cluster_number, cluster in enumerate(clusters):
        print(f"    Cluster {cluster_number + 1}: {data[cluster].tolist()}")