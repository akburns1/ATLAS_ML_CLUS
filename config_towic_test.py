import pandas as pd
import sys
import csv
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv('clus_test_ic.csv')

df = pd.DataFrame(data)
df.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_test_ic.csv', encoding='utf-8', index=False)

#############################
## y=abs(3.2-4.9) data set ##
#############################

df1 = df[df['y'].abs() >= 3.2]
dfa = df1.drop(['y'], axis=1)

dfa.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_test_4.9_3.2.csv', encoding='utf-8', index=False)

df2 = df[df['y'].abs() <= 3.2]

#############################
## y=abs(2.5-3.2) data set ##
#############################

df3 = df2[df2['y'].abs() >= 2.5]
dfb = df3.drop(['y'], axis=1)

dfb.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_test_3.2_2.5.csv', encoding='utf-8', index=False)

df4 = df2[df2['y'].abs() <= 2.5]

#############################
## y=abs(1.5-2.5) data set ##
#############################

df5 = df4[df4['y'].abs() >= 1.5]
dfc = df5.drop(['y'], axis=1)

dfc.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_test_2.5_1.5.csv', encoding='utf-8', index=False)

###########################
## y=abs(0-1.5) data set ##
###########################

df6 = df4[df4['y'].abs() <= 1.5]
dfd = df6.drop(['y'], axis=1)

dfd.to_csv('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ic_test_0_1.5.csv', encoding='utf-8', index=False)

