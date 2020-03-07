import pandas as pd
import numpy as np
import utils

def get_core_points(data):
    core_points = None
    return

def get_border_points(data):
    border_points = None
    return border_points

def get_noise_points(data):
    noise_points = None
    return noise_points

def DBSCAN(data, min_distance, min_points):
    distances = np.zeros((data.shape[0], data.shape[0]))
    for p in range(data.shape[0]):
        distances[p:,] = utils.euclidean(data[p], data)

    point_counts =

    clusters = []
    return clusters
data = pd.read_csv('data\dbscan_dataset.csv').to_numpy()[:,1:3].astype(float)
DBSCAN(data, 2, 3)