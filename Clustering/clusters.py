import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import levene
import statistics


file_path = "/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Chrastil Warren data.csv"
df = pd.read_csv(file_path)
data = df.values


cluster1 = ['GGWU', 'TYJR', 'FMKJ', 'ACGN', 'SIUT', 'WJJU', 'MTXB', 'NUAO', 'CGWN', 'AELV', 'WONG', 'SFUG', 'MCCO', 'ONVA', 'LMUU', 'ZDGH', 'LAWW', 'VZYX', 'YPGZ']
cluster2 = ['YPQL', 'GGMO', 'BQHT', 'LQKJ', 'UPGW', 'FPIT', 'XQJO', 'OUWM', 'RCEH', 'UREH', 'TEYQ', 'NGVO', 'WOKD', 'WMKQ', 'EUDK', 'UFNF', 'DXJP', 'ANAV', 'JBXP', 'WTIY', 'XKAL', 'DRDQ', 'ZTAL', 'EMBJ', 'YYTZ', 'PGJC', 'GZTO', 'FXXV', 'FWDA', 'DBQH', 'VPQA', 'VKPD', 'RTBV', 'IQMQ', 'FIVC', 'QQTV', 'YFDE', 'ODJH', 'UICN', 'URXR', 'SSNK', 'CBDG', 'QHTL', 'QMGI', 'UZMT', 'EGRU', 'AAAA', 'XPRU', 'BVEH', 'UING', 'BPPX', 'YNRZ', 'OWHE', 'RGYJ', 'MPOB', 'AOXY', 'VNWM', 'OVOW', 'WGNY', 'TMPJ', 'FQGS', 'QVFJ', 'IXRA', 'BYOU', 'OGBK', 'YJKM', 'EODT', 'HTLW', 'RTUG', 'PGBB', 'IHGX', 'HASK', 'HRGF', 'FMRE', 'UVRZ', 'JVRV', 'MRPD', 'SGLD', 'CXQX', 'GJJJ', 'RIKR', 'KSQU', 'BFJK', 'CPSL', 'CXIJ']

SBSOD1 = []
SBSOD2 = []
dist1 = []
dist2 = []
direct1 = []
direct2 = []
MRT1 = []
MRT2 = []

for row in data:
    if row[0] in cluster1:
        SBSOD1.append(row[1])
        dist1.append(row[2])
        direct1.append(row[3])
        MRT1.append(row[6])
    elif row[0] in cluster2:
        SBSOD2.append(row[1])
        dist2.append(row[2])
        direct2.append(row[3])
        MRT2.append(row[6])

print(SBSOD1)
print(SBSOD2)
stat_SBSOD, p_SBSOD = ttest_ind(SBSOD1, SBSOD2, equal_var=False)
print('stat=%.3f, p=%.3f' % (stat_SBSOD, p_SBSOD))
if p_SBSOD > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions\n')

print(dist1)
print(dist2)
stat_dist, p_dist = ttest_ind(dist1, dist2, equal_var=False)
print('stat=%.3f, p=%.3f' % (stat_dist, p_dist))
if p_dist > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions\n')

print(direct1)
print(direct2)
stat_direct, p_direct = ttest_ind(direct1, direct2, equal_var=False)
print('stat=%.3f, p=%.3f' % (stat_direct, p_direct))
if p_direct > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions\n')

print(MRT1)
print(MRT2)
print(statistics.mean(MRT1))
print(statistics.mean(MRT2))
print(statistics.stdev(MRT1))
print(statistics.stdev(MRT2))
levene_MRT, p_levene = levene(MRT1, MRT2, center='trimmed')
print(p_levene)
stat_MRT, p_MRT = ttest_ind(MRT1, MRT2, equal_var=False)
print('stat=%.3f, p=%.3f' % (stat_MRT, p_MRT))
if p_MRT > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions\n')
