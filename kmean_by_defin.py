import ast
import os.path

import numpy as np
import openpyxl

from cluster import average_vecto
from get_verb import read_file
from kmean import k_means, hierarchial_cluster, write_clusters
from silhouette import kmeans_cluster, hierarchy_cluster
from get_file import read_text


def read_excel(pathFile, sheet):
    wb = openpyxl.load_workbook(pathFile)
    sheet = wb[sheet]
    max_row = sheet.max_row

    defin = []
    verb = []
    example = []
    vector = {}
    for row in range(2, max_row + 1):
        str_df = str(sheet[f"A{row}"].value).split("\n")[0]
        vb = str(sheet[f"C{row}"].value).split("_")[0]
        vt = str(sheet[f"D{row}"].value).split("\n")[0]
        ex = str(sheet[f"B{row}"].value).split("\n")[0]
        if str_df.strip() == "" or str_df.strip() == "None":
            # print(str_df)
            vector[len(defin) - 1].append(ast.literal_eval(vt))
            str_exp = str(example[len(defin) - 1]) + ";" + ex
            example[len(defin) - 1] = str_exp
        else:
            defin.append(str_df.strip())
            vector[len(defin) - 1] = [ast.literal_eval(vt)]
            verb.append(vb)
            example.append(ex)

    # print(len(vector))
    vector_list = []
    for i in list(vector.values()):
        vector_list.append(list(average_vecto(i)))

    return example, vector_list, verb




# examples, vectors, verbs = read_excel("Data/verb_vn_phoBert.xlsx", "Sheet1")
# print(len(examples), len(vectors), len(verbs))
# #  Tìm số cụm tốt nhất = kmean
# # kmeans_cluster(vectors)   #4450
# cluster_num = 4450
# clusters, centers = k_means(cluster_num, vectors)
# # Tìm số cụm tốt nhất = hierarchy
# # hierarchy_cluster(centers)
# #10
# height = 12
# cluster_kmean_hierarchy = hierarchial_cluster(clusters, centers, height)
# write_clusters(f"Data/Output/verb_examples/{height}", cluster_kmean_hierarchy, verbs, examples)

# ids, vectors, verbs, sentences = read_file('Data/1M-sentences.txt')
# #  Tìm số cụm tốt nhất = kmean
# # kmeans_cluster(vectors)   #4450
# cluster_num = 10000
# clusters, centers = k_means(cluster_num, vectors)
# # # Tìm số cụm tốt nhất = hierarchy
# # # hierarchy_cluster(centers)
# # #10
# height = 50
# cluster_kmean_hierarchy = hierarchial_cluster(clusters, centers, height)
# write_clusters(f"Data/1M_Sentences/{height}", cluster_kmean_hierarchy, verbs, sentences)


verbs, vectors, sentences, centor  = read_text('/home/linhhm/data_output_kmeans6')
cluster_num = 3000
#clusters, centers = k_means(cluster_num, centor)
height = 32
cluster_kmean_hierarchy = hierarchial_cluster(vectors, centor, height)
write_clusters(f"/home/linhhm/Kmean/Data/kmean6/{height}", cluster_kmean_hierarchy, verbs, sentences)