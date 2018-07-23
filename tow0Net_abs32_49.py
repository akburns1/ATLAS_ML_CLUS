import numpy as np
import tflearn
import csv
 

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labelsA = load_csv('clus_ij_training_4.9_3.2.csv', target_column=0,
                        categorical_labels=True, n_classes=2)
input, labelsB = load_csv('clus_ij_test_4.9_3.2.csv', target_column=0,
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
model.fit(data, labelsA, n_epoch=100, batch_size=10, show_metric=True, validation_set=0.1)

# Test Data
BJet = [30.99439118, 6.474163573, 0.1842020447, 0.215243745, 45.95238095]
SJet = [54.36127427, 8.948606884, 0.1412519494, 0.2647294972, 45.41866093]


#Predict signal jet likelihood 
pred = model.predict([BJet, SJet])

print("Likelihood that Average Background Jet is a Background Jet:", pred[0][0])
print("Likelihood that Average Signal Jet is a Signal Jet:", pred[1][1])

predict = model.predict(input)
#print("Jet signal jet likelihood:", pred)

with open('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_ij_out_32_49.csv','wb') as f:
	csv_writer = csv.writer(f, delimiter=',')
	for x in predict:
		csv_writer.writerow(x)