import pandas as pd
import sys
import csv
from sklearn.utils import shuffle
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv('clus_training_ic.csv')

df = pd.DataFrame(data)

########################################
## y=abs(3.2-4.9) data set -- 50% b/s ##
########################################

df1 = df[df['y'].abs() >= 3.2]

sort1 = df1.sort_values('background/signal')
count = sort1['background/signal'].value_counts().tolist()
a = count[0] - count[1]

sort2 = sort1[a:]
sort2 = shuffle(sort2)

dfa = sort2.drop(['y'], axis=1)

dfa.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_training_4.9_3.2.csv', encoding='utf-8', index=False)

df2 = df[df['y'].abs() <= 3.2]

########################################
## y=abs(2.5-3.2) data set -- 50% b/s ##
########################################

df3 = df2[df2['y'].abs() >= 2.5]

sort3 = df3.sort_values('background/signal')
count1 = sort3['background/signal'].value_counts().tolist()
b = count1[0] - count1[1]

sort4 = sort3[b:]
sort4 = shuffle(sort4)

dfb = sort4.drop(['y'], axis=1)

dfb.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_training_3.2_2.5.csv', encoding='utf-8', index=False)

df4 = df2[df2['y'].abs() <= 2.5]

########################################
## y=abs(1.5-2.5) data set -- 50% b/s ##
########################################

df5 = df4[df4['y'].abs() >= 1.5]

sort5 = df5.sort_values('background/signal')
count2 = sort5['background/signal'].value_counts().tolist()
c = count2[0] - count2[1]

sort6 = sort5[c:]
sort6 = shuffle(sort6)

dfc = sort6.drop(['y'], axis=1)

dfc.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_training_2.5_1.5.csv', encoding='utf-8', index=False)


######################################
## y=abs(0-1.5) data set -- 50% b/s ##
######################################

df6 = df4[df4['y'].abs() <= 1.5]

sort7 = df5.sort_values('background/signal')
count3 = sort7['background/signal'].value_counts().tolist()
d = count3[0] - count3[1]

sort8 = sort7[d:]
sort8 = shuffle(sort8)

dfd = sort8.drop(['y'], axis=1)

dfd.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_training_0_1.5.csv', encoding='utf-8', index=False)


