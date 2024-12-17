import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import squareform, pdist
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

from get_file import read_text
from kmean import read_excel, k_means



def kmeans_cluster(X):
    best_k = 0
    best_silhouette = -1

    for k in range(800, 8400, 50):  # Chọn khoảng giá trị k
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(X, labels)

        if silhouette_avg > best_silhouette:
            best_silhouette = silhouette_avg
            best_k = k

    print(f"Best number of clusters (K-means): {best_k}")


def hierarchy_cluster(X):
    print(X.shape)
    # distance_matrix = squareform(pdist(X, metric='euclidean'))
    # print(distance_matrix.shape)
    linkage_matrix = linkage(X, method='ward')
    dendrogram(linkage_matrix)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.show()
    best_silhouette = -1
    best_cut = None
    # 80,
    for height in range(3, 80):  # Chọn khoảng giá trị chiều cao
        print(height, "=====================================================")
        labels = fcluster(linkage_matrix, height, criterion='distance')
        print(labels)
        silhouette_avg = silhouette_score(X, labels)

        if silhouette_avg > best_silhouette:
            best_silhouette = silhouette_avg
            best_cut = height

    print(f"Best cut height (Hierarchical): {best_cut}")


_, vectors, _ , centor = read_text("/home/linhhm/data_output_kmeans6")
# kmeans_cluster(vectors)
# distance_matrix = squareform(pdist(vectors, metric='euclidean'))
# cluster_num = 4376
_, centers = k_means(3000, centor )
# print(vectors[0])
# print(centers[0])
hierarchy_cluster(centers)
