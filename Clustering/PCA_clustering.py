import pandas as pd
from sklearn.decomposition import PCA
import glob
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def main():
    feature_list = []

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

    # PCA
    pca = PCA(n_components=2)

    # Option 1: Directly do the PCA
    # principalComponents = pca.fit_transform(feature_list)

    # Option 2: First standardize the data, then do the PCA
    X_std = StandardScaler().fit_transform(feature_list)
    principalComponents = pca.fit_transform(X_std)

    principalDF = pd.DataFrame(principalComponents)

    # display the scatter plot
    plt.scatter(principalDF[0], principalDF[1], alpha=1)
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.show()


main()
