#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import tensorflow as tf
tf.__version__

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#normalize
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train.shape)

plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()
print(x_train[0])

#define model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

#training the model
model.fit(x_train, y_train, epochs=5)#3

#evaluar modelo
val_loss, val_acc = model.evaluate(x_test, y_test)

#save the model
model.save('my_model')

#use model
new_model = tf.keras.models.load_model('my_model')
predictions = new_model.predict([x_test])
print(predictions)

#prediction
import numpy as np

np.argmax(predictions[200])


#check
plt.imshow(x_test[200])
plt.show()

#IN JUPYTER NOTEBOOK
#for i in range(120):
    #predicted_number = np.argmax(predictions[i])
    #plt.imshow(x_test[i])
    #plt.title("This is a {}".format(predicted_number))
    #plt.show()
