import pandas as pd
from sklearn.decomposition import PCA
import glob
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE


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
        feature.extend(feature2)
        feature.extend(feature3)
        feature.extend(feature4)

        # Select the data with 12000 frames; the other subjects not with 120000 frames are not considered
        if len(feature) == 12000:
            feature_list.append(feature)

    # Option 1: First do the PCA without standardization to reduce the dimension to 50, then do the tsne
    pca = PCA(n_components=50)
    principalComponents = pca.fit_transform(feature_list)
    X_embedded = TSNE(n_components=2).fit_transform(principalComponents)

    # Option 2: First do the PCA with standardization to reduce the dimension to 50, then do the tsne
    # pca = PCA(n_components=50)
    # X_std = StandardScaler().fit_transform(feature_list)
    # principalComponents = pca.fit_transform(X_std)
    # X_embedded = TSNE(n_components=2).fit_transform(principalComponents)

    # Option 3: Directly do the tsne with original feature data
    # X_embedded = TSNE(n_components=2).fit_transform(feature_list)

    tsneDF = pd.DataFrame(X_embedded)

    # display the scatter plot
    plt.scatter(tsneDF[0], tsneDF[1], alpha=0.1, color='black')
    plt.show()


main()
