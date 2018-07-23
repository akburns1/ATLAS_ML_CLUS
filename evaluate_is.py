import pandas as pd
import csv
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("---------------------------------------------------------------")
print("--clusERS WITH CONSTITUENT SUBTRACTION AND SOFT KILLER, INITIAL-")

##################
## y=abs(0-1.5) ##
##################

#load learn output and test data
data = pd.read_csv('clus_is_out_0_15.csv')
test = pd.read_csv('clus_is_test_0_1.5.csv',skiprows=1)

#put in data data frames and drop all columns but 0/1 from test and column 1 	#from data
df = pd.DataFrame(data)
dft = pd.DataFrame(test)

df1 = df.drop(df.columns[1], axis=1)

cols = [1,2,3,4,5]
dft1 = dft.drop(dft.columns[cols], axis=1)

#merge test and out
merge = pd.merge(df1, dft1, on=df1.index, how='outer')
match = merge.drop(merge.columns[0], axis=1)

#split into +/- 50% 
back = match[match[match.columns[0]] >= .5]
sig = match[match[match.columns[0]] <= .5]

#count 0's and 1's 
count = dft.groupby(dft[dft.columns[0]]).size()
countb = back.groupby(back[back.columns[1]]).size()
counts = sig.groupby(sig[sig.columns[1]]).size()

back_correct = (float(countb[0])/float(count[0]))*100
sig_correct = (float(counts[1])/float(count[1]))*100
print("---------------------------------------------------------------")
print("% of background jets predicted correctly in y = abs(0-1.5):")
print(back_correct)
print("% of signal jets predicted correctly in y = abs(0-1.5):")
print(sig_correct)

####################
## y=abs(1.5-2.5) ##
####################

#load learn output and test data
data = pd.read_csv('clus_is_out_15_25.csv')
test = pd.read_csv('clus_is_test_2.5_1.5.csv',skiprows=1)

#put in data data frames and drop all columns but 0/1 from test and column 1 	#from data
df = pd.DataFrame(data)
dft = pd.DataFrame(test)

df1 = df.drop(df.columns[1], axis=1)

cols = [1,2,3,4,5]
dft1 = dft.drop(dft.columns[cols], axis=1)

#merge test and out
merge = pd.merge(df1, dft1, on=df1.index, how='outer')
match = merge.drop(merge.columns[0], axis=1)

#split into +/- 50% 
back = match[match[match.columns[0]] >= .5]
sig = match[match[match.columns[0]] <= .5]

#count 0's and 1's 
count = dft.groupby(dft[dft.columns[0]]).size()
countb = back.groupby(back[back.columns[1]]).size()
counts = sig.groupby(sig[sig.columns[1]]).size()

back_correct = (float(countb[0])/float(count[0]))*100
sig_correct = (float(counts[1])/float(count[1]))*100
print("---------------------------------------------------------------")
print("% of background jets predicted correctly in y = abs(1.5-2.5):")
print(back_correct)
print("% of signal jets predicted correctly in y = abs(1.5-2.5):")
print(sig_correct)

####################
## y=abs(2.5-3.2) ##
####################

#load learn output and test data
data = pd.read_csv('clus_is_out_25_32.csv')
test = pd.read_csv('clus_is_test_3.2_2.5.csv',skiprows=1)

#put in data data frames and drop all columns but 0/1 from test and column 1 	#from data
df = pd.DataFrame(data)
dft = pd.DataFrame(test)

df1 = df.drop(df.columns[1], axis=1)

cols = [1,2,3,4,5]
dft1 = dft.drop(dft.columns[cols], axis=1)

#merge test and out
merge = pd.merge(df1, dft1, on=df1.index, how='outer')
match = merge.drop(merge.columns[0], axis=1)

#split into +/- 50% 
back = match[match[match.columns[0]] >= .5]
sig = match[match[match.columns[0]] <= .5]

#count 0's and 1's 
count = dft.groupby(dft[dft.columns[0]]).size()
countb = back.groupby(back[back.columns[1]]).size()
counts = sig.groupby(sig[sig.columns[1]]).size()
print(counts[0])

back_correct = (float(countb[0])/float(count[0]))*100
sig_correct = (float(counts[0])/float(count[0]))*100
print("---------------------------------------------------------------")
print("% of background jets predicted correctly in y = abs(2.5-3.2):")
print(back_correct)
print("% of signal jets predicted correctly in y = abs(2.5-3.2):")
print(sig_correct)

####################
## y=abs(3.2-4.9) ##
####################

#load learn output and test data
data = pd.read_csv('clus_is_out_32_49.csv')
test = pd.read_csv('clus_is_test_4.9_3.2.csv',skiprows=1)

#put in data data frames and drop all columns but 0/1 from test and column 1 	#from data
df = pd.DataFrame(data)
dft = pd.DataFrame(test)

df1 = df.drop(df.columns[1], axis=1)

cols = [1,2,3,4,5]
dft1 = dft.drop(dft.columns[cols], axis=1)

#merge test and out
merge = pd.merge(df1, dft1, on=df1.index, how='outer')
match = merge.drop(merge.columns[0], axis=1)

#split into +/- 50% 
back = match[match[match.columns[0]] >= .5]
sig = match[match[match.columns[0]] <= .5]

#count 0's and 1's 
count = dft.groupby(dft[dft.columns[0]]).size()
countb = back.groupby(back[back.columns[1]]).size()
counts = sig.groupby(sig[sig.columns[1]]).size()

back_correct = (float(countb[0])/float(count[0]))*100
sig_correct = (float(counts[1])/float(count[1]))*100
print("---------------------------------------------------------------")
print("% of background jets predicted correctly in y = abs(3.2-4.9):")
print(back_correct)
print("% of signal jets predicted correctly in y = abs(3.2-4.9):")
print(sig_correct)
print("---------------------------------------------------------------")

