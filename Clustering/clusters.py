import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import levene


# This path may not work, since it begin legacy code.
file_path = "/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Chrastil Warren data.csv"
df = pd.read_csv(file_path)
data = df.values


# Clusters derived from the umap_clustering method.
cluster1 = ['GGWU', 'TYJR', 'FMKJ', 'ACGN', 'SIUT', 'WJJU', 'MTXB', 'NUAO', 'CGWN', 'AELV', 'WONG', 'SFUG', 'MCCO', 'ONVA', 'LMUU', 'ZDGH', 'LAWW', 'VZYX', 'YPGZ']
cluster2 = ['YPQL', 'GGMO', 'BQHT', 'LQKJ', 'UPGW', 'FPIT', 'XQJO', 'OUWM', 'RCEH', 'UREH', 'TEYQ', 'NGVO', 'WOKD', 'WMKQ', 'EUDK', 'UFNF', 'DXJP', 'ANAV', 'JBXP', 'WTIY', 'XKAL', 'DRDQ', 'ZTAL', 'EMBJ', 'YYTZ', 'PGJC', 'GZTO', 'FXXV', 'FWDA', 'DBQH', 'VPQA', 'VKPD', 'RTBV', 'IQMQ', 'FIVC', 'QQTV', 'YFDE', 'ODJH', 'UICN', 'URXR', 'SSNK', 'CBDG', 'QHTL', 'QMGI', 'UZMT', 'EGRU', 'AAAA', 'XPRU', 'BVEH', 'UING', 'BPPX', 'YNRZ', 'OWHE', 'RGYJ', 'MPOB', 'AOXY', 'VNWM', 'OVOW', 'WGNY', 'TMPJ', 'FQGS', 'QVFJ', 'IXRA', 'BYOU', 'OGBK', 'YJKM', 'EODT', 'HTLW', 'RTUG', 'PGBB', 'IHGX', 'HASK', 'HRGF', 'FMRE', 'UVRZ', 'JVRV', 'MRPD', 'SGLD', 'CXQX', 'GJJJ', 'RIKR', 'KSQU', 'BFJK', 'CPSL', 'CXIJ']

# Create 4 metrics for both clusters
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

# DO 2 independent samples t-test for 4 metrics, if set equal_var = False, then it's Welch's test.
# It depends on the result from Levene's test.
# For Levene's test, since our data is not heavy-tailed, use the median version for all 4 metrics.
print('SBSOD:')
print(SBSOD1)
print(SBSOD2)
levene_SBSOD, p_levene_SBSOD = levene(SBSOD1, SBSOD2, center='median')
print('stat=%.3f, p=%.3f' % (levene_SBSOD, p_levene_SBSOD))
if p_levene_SBSOD > 0.05:
    print('Treat the two SBSOD samples with equal variance')
else:
    print('Treat the two SBSOD samples with different variances')
stat_SBSOD, p_SBSOD = ttest_ind(SBSOD1, SBSOD2, equal_var=True)
print('stat=%.3f, p=%.3f' % (stat_SBSOD, p_SBSOD))
if p_SBSOD > 0.05:
    print('Probably the same distribution for SBSOD data')
else:
    print('Probably different distributions for SBSOD data\n')

print('\nDistance:')
print(dist1)
print(dist2)
levene_dist, p_levene_dist = levene(dist1, dist2, center='median')
print('stat=%.3f, p=%.3f' % (levene_dist, p_levene_dist))
if p_levene_dist > 0.05:
    print('Treat the two distance samples with equal variance')
else:
    print('Treat the two distance samples with different variances')
stat_dist, p_dist = ttest_ind(dist1, dist2, equal_var=True)
print('stat=%.3f, p=%.3f' % (stat_dist, p_dist))
if p_dist > 0.05:
    print('Probably the same distribution for distance data')
else:
    print('Probably different distributions for distance data\n')

print('\nDirection:')
print(direct1)
print(direct2)
levene_direct, p_levene_direct = levene(direct1, direct2, center='median')
print('stat=%.3f, p=%.3f' % (levene_direct, p_levene_direct))
if p_levene_direct > 0.05:
    print('Treat the two direction samples with equal variance')
else:
    print('Treat the two direction samples with different variances')
stat_direct, p_direct = ttest_ind(direct1, direct2, equal_var=True)
print('stat=%.3f, p=%.3f' % (stat_direct, p_direct))
if p_direct > 0.05:
    print('Probably the same distribution for direction data')
else:
    print('Probably different distributions for direction data\n')

print('\nMRT:')
print(MRT1)
print(MRT2)
levene_MRT, p_levene_MRT = levene(MRT1, MRT2, center='median')
print('stat=%.3f, p=%.3f' % (levene_MRT, p_levene_MRT))
if p_levene_MRT > 0.05:
    print('Treat the two samples with equal variance')
else:
    print('Treat the two samples with different variances')
stat_MRT, p_MRT = ttest_ind(MRT1, MRT2, equal_var=True)
print('stat=%.3f, p=%.3f' % (stat_MRT, p_MRT))
if p_MRT > 0.05:
    print('Probably the same distribution for ')
else:
    print('Probably different distributions\n')
