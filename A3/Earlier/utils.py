import random
import numpy as np

def initialize_centroids(data, k):
    """
    Randomly select k centroids from the dataset.
    Args:
    data: List of datapoints (each datapoint is also a list).
    k: Number of centroids to initialize.

    Returns:
    List of k centroids.
    """
    # Ensure the data list is shuffled to randomize centroid selection
    random.shuffle(data)
    # Select the first k elements as initial centroids
    centroids = data[:k]
    return centroids

def partition_data(data, num_partitions):
    """
    Partition the data into roughly equal parts.
    Args:
    data: List of datapoints.
    num_partitions: Number of parts to divide the data into.

    Returns:
    List of lists, where each sublist represents data for one partition.
    """
    # Calculate the size of each partition
    partition_size = len(data) // num_partitions
    # Remaining items to distribute after integer division
    remainder = len(data) % num_partitions
    partitions = []

    start = 0
    for i in range(num_partitions):
        end = start + partition_size + (1 if i < remainder else 0)
        partitions.append(data[start:end])
        start = end

    return partitions