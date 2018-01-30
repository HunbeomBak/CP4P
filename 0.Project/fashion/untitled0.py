import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import random
tf.reset_default_graph()

#load data
df_train=pd.read_csv('fashion-mnist_train.csv')
df_test =pd.read_csv('fashion-mnist_test.csv')

# train_set
train_set=df_train.as_matrix(None)

x_train=train_set[:,1:]
y_train=train_set[:,[0]]

# fot batch
x_bt = tf.train.input_producer(tf.constant(np.asarray(x_train)), num_epochs= 1)
y_bt = tf.train.input_producer(tf.constant(np.asarray(y_train)), num_epochs= 1)
x_bt =x_bt.dequeue()
y_bt =y_bt.dequeue()
batch_size=100
train_x_batch, train_y_batch = tf.train.batch([x_bt,y_bt] , batch_size=100)

# test_set
test_set=df_test.as_matrix(columns=None)

x_test=test_set[:,1:]
y_test=test_set[:,[0]]

#Make model
X= tf.placeholder(tf.float32, [None,784])
X_img=tf.reshape(X, [-1,28,28,1])

Y = tf.placeholder(tf.int32, [None, 1])  
Y_one_hot = tf.one_hot(Y, 10)  # one hot
Y_one_hot = tf.reshape(Y_one_hot, [-1, 10])


W1=tf.Variable(tf.random_normal([3,3,1,32],stddev=0.01))
L1= tf.nn.conv2d(X_img,W1,strides=[1,1,1,1],padding='SAME')
L1=tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

W2=tf.Variable(tf.random_normal([3,3,32,64],stddev=0.01))
L2=tf.nn.conv2d(L1,W2,strides=[1,1,1,1],padding='SAME')
L2=tf.nn.relu(L2)
L2= tf.nn.max_pool(L2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

L2= tf.reshape(L2,[-1,7*7*64])

W3=tf.get_variable("W3",shape=[7*7*64,10],initializer=tf.contrib.layers.xavier_initializer())
b=tf.Variable(tf.random_normal([10]))

hypothesis = tf.matmul(L2,W3)+b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y_one_hot))
optimizer =tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

sess= tf.Session()
sess.run(tf.initialize_all_variables())

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

learning_rate = 0.001
training_epochs = 15
batch_size=100
total_batch= int(len(x_train)/batch_size)

for epoch in range(training_epochs):
    avg_cost=0
    for i in range(total_batch):
        x_batch, y_batch = sess.run([train_x_batch, train_y_batch])
        c, _ = sess.run([cost, optimizer],feed_dict={X:x_batch, Y:y_batch })
        avg_cost += c/ total_batch
    print('Epoch:','%04d'%(epoch+1),'cost=','{:.9f}'.format(avg_cost))

    
print('Learning finish')    

















