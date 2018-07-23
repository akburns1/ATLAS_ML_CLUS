import numpy as np
import tflearn
import csv
 

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labelsA = load_csv('clus_ij_training_0_1.5.csv', target_column=0,
                        categorical_labels=True, n_classes=2)
input, labelsB = load_csv('clus_ij_test_0_1.5.csv', target_column=0,
                        categorical_labels=True, n_classes=2)

# Build neural network
#Data has 5 features
net = tflearn.input_data(shape=[None, 5]) 
net = tflearn.fully_connected(net, 32)
dropout1 = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(dropout1, 2, activation='softmax', bias=False, weights_init='truncated_normal')

net = tflearn.regression(net)


# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data, labelsA, n_epoch=10, batch_size=1, show_metric=True, validation_set=0.1)

# Test Data
BJet = [43.77117348, 8.078303179, 0.2001286104, 0.3167207993, 26.44940963]
SJet = [300.6603933, 21.72258017, 0.1094483385, 0.5737259851, 27.69220991]


#Predict signal jet likelihood 
pred = model.predict([BJet, SJet])

print("Likelihood that Average Background Jet is a Background Jet:", pred[0][0])
print("Likelihood that Average Signal Jet is a Signal Jet:", pred[1][1])

predict = model.predict(input)
#print("Jet signal jet likelihood:", pred)

with open('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ij_out_0_15.csv','wb') as f:
	csv_writer = csv.writer(f, delimiter=',')
	for x in predict:
		csv_writer.writerow(x)