import pandas as pd
import glob
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def main():
    feature_list = []
    subject_list = []
    directoryPath = '/Users/wangyan/Desktop/Research/Maze_Research/Parsed_Data/'

    for file_name in glob.glob(directoryPath + '*.csv'):
        df = pd.read_csv(file_name)
        feature = list(df['posX'].values[0:30000])
        feature2 = list(df['posZ'].values[0:30000])
        feature3 = list(df['rotX'].values[0:30000])
        feature4 = list(df['rotZ'].values[0:30000])
        feature.extend(feature2)
        feature.extend(feature3)
        feature.extend(feature4)
        if len(feature) == 120000:
            feature_list.append(feature)
            subject_list.append(file_name[58:62])

    x_kmeans = KMeans(n_clusters=10, random_state=0)
    y_kmeans = x_kmeans.fit_predict(feature_list)

    print(y_kmeans)
    print(subject_list)

    clusters = dict()
    for i in range(len(y_kmeans)):
        if y_kmeans[i] in clusters:
            clusters[y_kmeans[i]].append(subject_list[i])
        else:
            clusters[y_kmeans[i]] = [subject_list[i]]

    print(clusters)


main()
