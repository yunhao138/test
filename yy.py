import mysql.connector
import tensorflow as tf
import numpy as np

a=np.array([12,3])
a1=tf.convert_to_tensor(a)
print(a,a1)
with tf.Session() as sess:

    print(sess.run(a1))




