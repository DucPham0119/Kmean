import ast
import os.path

import numpy as np
import openpyxl
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import squareform, pdist
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def read_excel(pathFile, sheet):
    wb = openpyxl.load_workbook(pathFile)
    sheet = wb[sheet]
    max_row = sheet.max_row

    defin = []
    example = []
    verb = []
    vector = []
    for row in range(2, max_row + 1):
        str_df = str(sheet[f"A{row}"].value).split("\n")[0]
        examp = str(sheet[f"B{row}"].value).split("\n")[0]
        vb = str(sheet[f"C{row}"].value).split("_")[0]
        vt = str(sheet[f"D{row}"].value).split("\n")[0]
        vector.append(ast.literal_eval(vt))
        defin.append(str_df)
        example.append(examp)
        verb.append(vb)

    return defin, example, verb, vector


def k_means(clusters_nm, vector):
    kmeans = KMeans(n_clusters=clusters_nm)
    kmeans.fit(vector)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Tạo một từ điển để lưu trữ các điểm thuộc cùng một cụm
    clusters_km = {i: [] for i in range(clusters_nm)}
    for i, label in enumerate(labels):
        clusters_km[label].append(i)
    return clusters_km, centroids


def hierarchial_cluster(clusters_kmean, center, threshold):
    linkage_matrix = linkage(center, method='ward')
    cluster_hierarchy = fcluster(linkage_matrix, threshold, criterion='distance')
    dendrogram(linkage_matrix)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.show()

    positions = {label: [] for label in set(cluster_hierarchy)}
    for i, label in enumerate(cluster_hierarchy):
        positions[label].append(i)

    cluster_positions = {i: [] for i in set(cluster_hierarchy)}
    for idx, cluster_id in enumerate(cluster_hierarchy):
        for i in positions[cluster_id]:
            cluster_positions[cluster_id] += (clusters_kmean[i])
            cluster_positions[cluster_id] = list(set(cluster_positions[cluster_id]))
    print(cluster_positions)
    return cluster_positions

    # Vẽ dendrogram


def write_clusters(pathFile, clusters, verbs, examples):
    for cluster, idx in clusters.items():
        filename = os.path.join(pathFile, "cluster" + str(cluster) + ".txt")

        if idx:
            with open(filename, 'w', encoding="utf-8") as file:
                file.write("Verb \t Examples\n")
                for i in idx:
                    file.write(verbs[i] + "\t" + examples[i] + "\n")
                file.write("\n")


# defins, examples, verbs, vectors = read_excel("Data/verb_vn_phoBert.xlsx", "Sheet1")
# cluster_num = 4376
# clusters, centers = k_means(cluster_num, vectors)
#
# height = 12
# cluster_kmean_hierarchy = hierarchial_cluster(clusters, centers, height)
# write_clusters(f"Data/Output/kmean_hierarchy/{height}", cluster_kmean_hierarchy, verbs, examples)
