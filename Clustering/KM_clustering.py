import pandas as pd
import glob
from sklearn.cluster import KMeans


def main():
    feature_list = []
    subject_list = []

    directoryPath = '/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Parsed_Data/'

    for file_name in glob.glob(directoryPath + '*.csv'):
        df = pd.read_csv(file_name)

        # read in the data on X and Z position plus the rotation
        feature = list(df['posX'].values[0:30000:10])
        feature2 = list(df['posZ'].values[0:30000:10])
        feature3 = list(df['rotX'].values[0:30000:10])
        feature4 = list(df['rotZ'].values[0:30000:10])
        feature5 = list(df['rotZ'].values[0:30000:10])

        feature.extend(feature2)
        feature.extend(feature3)
        feature.extend(feature4)
        feature.extend(feature5)

        # Select the data with 15000 frames; the other subjects not with 15000 frames are not considered
        if len(feature) == 15000:
            feature_list.append(feature)
            # Each csv file is named with 4 letters, so take the 4 letters as their names.
            subject_list.append(file_name[74:78])

    x_kmeans = KMeans(n_clusters=10, random_state=0)
    y_kmeans = x_kmeans.fit_predict(feature_list)

    clusters = dict()
    for i in range(len(y_kmeans)):
        if y_kmeans[i] in clusters:
            clusters[y_kmeans[i]].append(subject_list[i])
        else:
            clusters[y_kmeans[i]] = [subject_list[i]]

    # The output is a dictionary where the keys are the cluster number and their corresponding values are the elements
    # in each clusters
    print(clusters)


main()
