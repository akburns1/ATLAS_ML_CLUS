import pandas as pd
import sys
import csv

print("-----------------------------------------------------")
print("----------------clus INCL + JAPU----------------------")
print("-----------------------------------------------------")
print("-----------------y=abs(3.2-4.9)----------------------")
data = pd.read_csv('clus_ij_training_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ij_test_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(2.5-3.2)----------------------")

data = pd.read_csv('clus_ij_training_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ij_test_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(1.5-2.5)----------------------")

data = pd.read_csv('clus_ij_training_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ij_test_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(0-1.5)-----------------------")

data = pd.read_csv('clus_ij_training_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ij_test_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------------------------------------------")
print("----------------clus TIME + JAPU----------------------")
print("-----------------------------------------------------")
print("-----------------y=abs(3.2-4.9)----------------------")
data = pd.read_csv('clus_tj_training_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tj_test_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(2.5-3.2)----------------------")

data = pd.read_csv('clus_tj_training_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tj_test_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(1.5-2.5)----------------------")

data = pd.read_csv('clus_tj_training_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tj_test_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(0-1.5)-----------------------")

data = pd.read_csv('clus_tj_training_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tj_test_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------------------------------------------")
print("----------------clus INCL + CSPU----------------------")
print("-----------------------------------------------------")
print("-----------------y=abs(3.2-4.9)----------------------")
data = pd.read_csv('clus_ic_training_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ic_test_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(2.5-3.2)----------------------")

data = pd.read_csv('clus_ic_training_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ic_test_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(1.5-2.5)----------------------")

data = pd.read_csv('clus_ic_training_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ic_test_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(0-1.5)-----------------------")

data = pd.read_csv('clus_ic_training_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ic_test_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------------------------------------------")
print("----------------clus TIME + CSPU----------------------")
print("-----------------------------------------------------")
print("-----------------y=abs(3.2-4.9)----------------------")
data = pd.read_csv('clus_tc_training_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tc_test_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(2.5-3.2)----------------------")

data = pd.read_csv('clus_tc_training_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tc_test_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(1.5-2.5)----------------------")

data = pd.read_csv('clus_tc_training_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tc_test_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(0-1.5)-----------------------")

data = pd.read_csv('clus_tc_training_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_tc_test_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------------------------------------------")
print("----------------clus INCL + CSSK----------------------")
print("-----------------------------------------------------")
print("-----------------y=abs(3.2-4.9)----------------------")
data = pd.read_csv('clus_is_training_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().to_dict()
print(count)
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_is_test_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)


print("-----------------y=abs(2.5-3.2)----------------------")

data = pd.read_csv('clus_is_training_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_is_test_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(1.5-2.5)----------------------")

data = pd.read_csv('clus_is_training_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_is_test_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(0-1.5)-----------------------")

data = pd.read_csv('clus_is_training_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_is_test_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------------------------------------------")
print("----------------clus TIME + CSSK----------------------")
print("-----------------------------------------------------")
print("-----------------y=abs(3.2-4.9)----------------------")
data = pd.read_csv('clus_ts_training_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ts_test_4.9_3.2.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(2.5-3.2)----------------------")

data = pd.read_csv('clus_ts_training_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ts_test_3.2_2.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(1.5-2.5)----------------------")

data = pd.read_csv('clus_ts_training_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ts_test_2.5_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)

print("-----------------y=abs(0-1.5)-----------------------")

data = pd.read_csv('clus_ts_training_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of training samples:")
print(count[0]+count[1]-1)

data = pd.read_csv('clus_ts_test_0_1.5.csv')
df = pd.DataFrame(data)
count = df['background/signal'].value_counts().tolist()
print("#of test samples:")
print(count[0]+count[1]-1)