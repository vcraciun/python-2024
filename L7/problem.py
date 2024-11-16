import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from tslearn.clustering import KShape
from sklearn.metrics import silhouette_score

# Load your JSON file
with open('serii.json', 'r') as file:
    data = json.load(file)

# Function to resample a series to a specified length
def resample_series(series, new_length=2000):
    original_length = len(series)
    x_original = np.linspace(0, 1, original_length)
    x_new = np.linspace(0, 1, new_length)
    interpolator = interp1d(x_original, series, kind='linear')
    return interpolator(x_new)

# Function to normalize a series between -1 and 1
def normalize_series(series):
    min_val = np.min(series)
    max_val = np.max(series)
    return 2 * (series - min_val) / (max_val - min_val) - 1

# Resample and normalize each series in the JSON data
resampled_normalized_data = np.array([
    normalize_series(resample_series(series)) for series in data
])

# Determine the best number of clusters using silhouette score
best_score = -1
best_k = 0
best_labels = None
silhouette_scores = []
best_kshape = None

for k in range(2, 10):  # Testing for 2 to 10 clusters
    kshape = KShape(n_clusters=k, random_state=0)
    labels = kshape.fit_predict(resampled_normalized_data)
    score = silhouette_score(resampled_normalized_data, labels, metric='euclidean')
    silhouette_scores.append(score)
    
    if score > best_score:
        best_score = score
        best_k = k
        best_labels = labels
        best_kshape = kshape
    print(f'Iteration {k}')


print(f'Best number of clusters: {best_k}, Silhouette Score: {best_score}')

# Plot silhouette scores
plt.figure(figsize=(10, 6))
plt.plot(range(2, 10), silhouette_scores, marker='o')
plt.title('Silhouette Scores for Different Numbers of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()

# Plot each cluster in a 5x3 grid
plt.figure(figsize=(15, 10))
grid_size = (3, 3)
colors = plt.cm.tab10.colors  # Use a colormap for colors

for cluster in range(best_k):
    ax = plt.subplot(grid_size[0], grid_size[1], cluster + 1)
    cluster_color = colors[cluster % len(colors)]
    for i, series in enumerate(resampled_normalized_data):
        if best_labels[i] == cluster:
            ax.plot(series, color=cluster_color, alpha=0.5)
    # Plot the centroid in a different color
    ax.plot(best_kshape.cluster_centers_[cluster].ravel(), color='black', linewidth=2)
    ax.set_title(f'Cluster {cluster + 1}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.grid(True)

plt.tight_layout()
plt.show()

