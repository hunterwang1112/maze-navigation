import matplotlib.pyplot as plt
import umap
import pandas as pd
import glob


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

    standard_embedding = umap.UMAP().fit_transform(feature_list)
    umapDF = pd.DataFrame(standard_embedding)

    # display the scatter plot
    plt.scatter(umapDF[0], umapDF[1], alpha=0.1, color='black')
    plt.show()


main()
