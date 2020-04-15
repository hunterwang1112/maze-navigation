import matplotlib.pyplot as plt
import umap
import hdbscan
import sklearn.cluster as cluster
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score


import pandas as pd
import glob
from sklearn.cluster import KMeans


def main():
    feature_list = []
    subject_list = []
    directoryPath = '/Users/wangyan/Desktop/Research/Maze_Research/Parsed_Data/'

    count = 0
    for file_name in glob.glob(directoryPath + '*.csv'):
        df = pd.read_csv(file_name)
        feature = list(df['posX'].values[0:30000:10])
        feature2 = list(df['posZ'].values[0:30000:10])
        feature3 = list(df['rotX'].values[0:30000:10])
        feature4 = list(df['rotZ'].values[0:30000:10])
        feature.extend(feature2)
        feature.extend(feature3)
        feature.extend(feature4)
        if len(feature) == 12000:
            count += 1
            feature_list.append(feature)
            subject_list.append(file_name[58:62])

    standard_embedding = umap.UMAP().fit_transform(feature_list)
    umapDF = pd.DataFrame(standard_embedding)
    print(count)

    plt.scatter(umapDF[0], umapDF[1], alpha=0.1, color='black')
    plt.show()

main()
