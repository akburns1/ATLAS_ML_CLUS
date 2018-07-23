import numpy as np
import tflearn
import csv

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labelsA = load_csv('clus_is_training_2.5_1.5.csv', target_column=0,
                        categorical_labels=True, n_classes=2)
input, labelsB = load_csv('clus_is_test_2.5_1.5.csv', target_column=0,
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

predict = model.predict(input)

with open('/Users/Anne-Katherine/Desktop/ATLAS_ML/clus_is_out_15_25.csv','wb') as f:
	csv_writer = csv.writer(f, delimiter=',')
	for x in predict:
		csv_writer.writerow(x)