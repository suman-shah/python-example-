import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import math, random
import matplotlib.pyplot as plt
from scipy import special

# Define the number of outputs and the learning rate
n_input = 1
n_nodes_hl1 = 400
n_nodes_hl2 = 400
n_nodes_hl3 = 500
n_output = 1
learn_rate = 0.00003

# Boundary Conditions
A = 1

# training data
N = 1000
a = 0
b = 1
x = np.arange(a, b, (b-a)/N).reshape((N,1))
y = np.zeros(N)

# Placeholders
x_ph = tf.placeholder('float', [None, 1],name='input')
y_ph = tf.placeholder('float')

# number of epochs
n_epochs = 800

# batchsize per epoch
batch_size= 200

#validation-data size
n_valid= 400

# Define standard deviation for initialising weights and biases from normal distribution.
hl_sigma = 0.02

def neural_network_model(data):
    data = tf.cast(data, tf.float32)
    hidden_1_layer = {'weights': tf.Variable(tf.random.normal([n_input, n_nodes_hl1],stddev=hl_sigma)),
                      'biases': tf.Variable(tf.random.normal([n_nodes_hl1], stddev=hl_sigma))}
    hidden_2_layer = {'weights': tf.Variable(tf.random.normal([n_nodes_hl1, n_nodes_hl2], stddev=hl_sigma)),
                      'biases': tf.Variable(tf.random.normal([n_nodes_hl2], stddev=hl_sigma))}
    output_layer = {'weights': tf.Variable(tf.random.normal([n_nodes_hl2, n_output], stddev=hl_sigma)),
                      'biases': tf.Variable(tf.random.normal([n_output], stddev=hl_sigma))}
       
        
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.tanh(l1)   
    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)
    output = tf.add(tf.matmul(l2, output_layer['weights']), output_layer['biases'], name='output')
    return output


def train_neural_network_batch():
    prediction = neural_network_model(x_ph)  
    pred_dx = tf.gradients(prediction, x_ph)
    
    u = A + (1-x_ph)*prediction
    dudx = -prediction + (1-x_ph)*pred_dx
    
    cost = tf.reduce_mean(tf.square(dudx + 2*x_ph))
    optimizer = tf.train.AdamOptimizer(learn_rate).minimize(cost)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        for epoch in range(n_epochs):
            _, l = sess.run([optimizer,cost], feed_dict={x_ph:x, y_ph:y})
            
            if(epoch % 100 == 0):
                print('loss:-',l,', epoch:-',epoch)

        # Validation
        return sess.run(tf.squeeze(prediction),{x_ph:x}), x
    
                
y_pred,x_pred = train_neural_network_batch()
y_pred = y_pred.reshape(N,1)
u = A+(1-x)*y_pred
plt.plot(x_pred, u,label ='NN')
plt.plot(x_pred, -x_pred*x_pred+2,label ='Analytical')
plt.legend()
plt.show()
