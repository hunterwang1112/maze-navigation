import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd

FILE_PATH = '/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Parsed_Data/'
OUTPUT_PATH1 = '/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Trace_plots/cluster1/'
OUTPUT_PATH2 = '/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Trace_plots/cluster2/'


def generate_plot(id, cluster):
    # The path may not work, since it being legacy code
    file_name = FILE_PATH + id + '.csv'
    df = pd.read_csv(file_name)
    # read in the data on X and Z position
    x = list(df['posX'].values[::10])
    y = list(df['posZ'].values[::10])

    fig = plt.figure()
    ax = plt.axes(projection="3d")

    time = list(range(3000, 0, -1))
    t_size = len(x)

    # colorGrad customized
    colorGrad = []
    for i in range(0, t_size):
        colorGrad.append([i / t_size, 0, 1 - i / t_size])

    z_points = time
    x_points = x
    y_points = y

    if cluster == 1:
        output_path = OUTPUT_PATH1 + id + '.png'
    else:
        output_path = OUTPUT_PATH2 + id + '.png'

    ax.scatter3D(x_points, y_points, z_points, c=colorGrad, cmap='hsv')
    ax.set_xlabel('X position')
    ax.set_ylabel('Z position')
    ax.set_zlabel('time')
    plt.title(id)
    plt.savefig(output_path)
    # plt.show()
    print(f'{id} is successfully generated')


# Clusters derived from the umap_clustering method.
cluster1 = ['GGWU', 'TYJR', 'FMKJ', 'ACGN', 'SIUT', 'WJJU', 'MTXB', 'NUAO', 'CGWN', 'AELV', 'WONG', 'SFUG', 'MCCO', 'ONVA', 'ZDGH', 'LAWW', 'VZYX', 'YPGZ']
cluster2 = ['YPQL', 'GGMO', 'BQHT', 'LQKJ', 'UPGW', 'FPIT', 'XQJO', 'OUWM', 'RCEH', 'UREH', 'TEYQ', 'NGVO', 'WOKD', 'WMKQ', 'EUDK', 'UFNF', 'DXJP', 'ANAV', 'JBXP', 'WTIY', 'XKAL', 'DRDQ', 'ZTAL', 'EMBJ', 'YYTZ', 'PGJC', 'GZTO', 'FXXV', 'DBQH', 'VPQA', 'VKPD', 'RTBV', 'IQMQ', 'FIVC', 'QQTV', 'YFDE', 'ODJH', 'UICN', 'URXR', 'SSNK', 'CBDG', 'QHTL', 'QMGI', 'UZMT', 'EGRU', 'AAAA', 'XPRU', 'BVEH', 'UING', 'BPPX', 'YNRZ', 'OWHE', 'RGYJ', 'MPOB', 'AOXY', 'VNWM', 'OVOW', 'WGNY', 'TMPJ', 'FQGS', 'QVFJ', 'IXRA', 'BYOU', 'OGBK', 'YJKM', 'EODT', 'HTLW', 'RTUG', 'PGBB', 'IHGX', 'HASK', 'HRGF', 'FMRE', 'UVRZ', 'JVRV', 'MRPD', 'SGLD', 'CXQX', 'GJJJ', 'RIKR', 'KSQU', 'BFJK', 'CPSL', 'CXIJ']

# These two ids produce errors when generating their trace plots.
error_cluster1 = ['LMUU']
error_cluster2 = ['FWDA']

for id in cluster1:
    generate_plot(id, 1)

for id in cluster2:
    generate_plot(id, 2)


