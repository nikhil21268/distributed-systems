import random

def load_data_points(filename):
    """
    Load data points from a file where each line contains two numeric values separated by a comma.
    """
    data_points = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                try:
                    point = (float(parts[0]), float(parts[1]))
                    data_points.append(point)
                except ValueError:
                    print(f"Error converting data {parts} to floats.")
    return data_points

def initialize_centroids(data, k):
    """
    Randomly select k centroids from the dataset and return them as a list of comma-separated strings.
    """
    selected_centroids = random.sample(data, k)
    # Convert each tuple to a string in the format "x,y"
    centroids_as_strings = [f"{centroid[0]},{centroid[1]}" for centroid in selected_centroids]
    return centroids_as_strings

# Usage example:
filename = "points.txt"  # Adjust the path to where your data file is located
data_points = load_data_points(filename)
number_of_centroids = 4  # Set the number of centroids you need
centroids = initialize_centroids(data_points, number_of_centroids)
print(centroids)
