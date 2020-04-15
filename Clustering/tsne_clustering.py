import pandas as pd
from sklearn.decomposition import PCA
import glob
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE


def main():
    feature_list = []
    subject_list = []
    directoryPath = '/Users/wangyan/Desktop/Research/Maze_Research/Parsed_Data/'

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
            feature_list.append(feature)
            subject_list.append(file_name[58:62])

    # pca = PCA(n_components=50)

    # principalComponents = pca.fit_transform(feature_list)

    # X_std = StandardScaler().fit_transform(feature_list)
    # principalComponents = pca.fit_transform(X_std)
    # X_std = StandardScaler().fit_transform(feature_list)

    X_embedded = TSNE(n_components=2).fit_transform(feature_list)

    tsneDF = pd.DataFrame(X_embedded)

    plt.scatter(tsneDF[0], tsneDF[1], alpha=0.1, color='black')
    plt.show()


main()
