import matplotlib.pyplot as plt
import umap
import pandas as pd
import glob


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
        feature6 = list(df['rotY'].values[0:30000:10])
        feature4 = list(df['rotZ'].values[0:30000:10])
        feature.extend(feature2)
        feature.extend(feature3)
        feature.extend(feature6)
        feature.extend(feature4)

        # Select the data with 12000 frames; the other subjects not with 120000 frames are not considered
        if len(feature) == 15000:
            feature_list.append(feature)
            # Each csv file is named with 4 letters, so take the 4 letters as their names.
            subject_list.append(file_name[74:78])

    standard_embedding = umap.UMAP().fit_transform(feature_list)
    umapDF = pd.DataFrame(standard_embedding)

    cluster1 = []
    cluster2 = []
    for i in range(len(standard_embedding)):
        if standard_embedding[i][1] > 1:
            cluster1.append(subject_list[i])
        else:
            cluster2.append(subject_list[i])

    print(cluster1)
    print(cluster2)

    # display the scatter plot
    plt.scatter(umapDF[0], umapDF[1], alpha=1)
    plt.show()


main()
