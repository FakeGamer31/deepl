import pandas as pd
import seaborn as sns
import keras
import matplotlib.pyplot as plt
import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

monitor = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy',
                                           mode='max',
                                           restore_best_weights=True,
                                           patience=5)
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir='logs', histogram_freq=1)

history = model.fit(x_train, y_train,
                    epochs=20,
                    validation_data=(x_test, y_test),
                    callbacks=[monitor, tensorboard_callback])

plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.legend()

plt.show()

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test Genauigkeit: {test_acc}')
